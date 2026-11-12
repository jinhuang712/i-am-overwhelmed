I don't see your site's code in this working directory, so this is the standard GitHub OAuth flow (authorization code grant) that almost every "Sign in with GitHub" button uses. If you point me at your auth code, I can map each step to the actual files.

## The flow, step by step

```
Browser                    Your Backend                     GitHub
   |                            |                              |
1  |--- click "Sign in" ------->|                              |
2  |<-- 302 to github.com ------|  (sets state cookie)         |
3  |------------------------- GET /login/oauth/authorize ----->|
4  |<------------------------ login + consent page ------------|
5  |------------------------- user approves ------------------>|
6  |<-- 302 to your callback ?code=...&state=... --------------|
7  |--- GET /callback?code&state ->|                           |
8  |                            |--- POST /login/oauth/access_token -->|
9  |                            |<-- access_token -------------|
10 |                            |--- GET api.github.com/user ->|
11 |                            |<-- profile / emails ---------|
12 |<-- set session cookie, 302 to app                         |
```

### 1–2. Your backend starts the flow
The button hits a route like `/auth/github`. The backend:
- Generates a random **`state`** value and stores it in a short-lived cookie or the server session (CSRF protection).
- Optionally generates a **PKCE** `code_verifier` and derives a `code_challenge`.
- Redirects the browser to:
  ```
  https://github.com/login/oauth/authorize
    ?client_id=YOUR_CLIENT_ID
    &redirect_uri=https://yoursite.com/auth/github/callback
    &scope=read:user user:email
    &state=RANDOM
    [&code_challenge=...&code_challenge_method=S256]
  ```

### 3–5. User authenticates at GitHub
This happens entirely between the browser and GitHub. Your site never sees the user's GitHub password or 2FA. If the user has already authorized your app, GitHub may skip the consent screen.

### 6. GitHub redirects back
GitHub sends the browser to your `redirect_uri` with a one-time **`code`** (valid ~10 minutes) and the `state` you sent. The `redirect_uri` must match what's registered in your OAuth App settings.

### 7. Callback validation
Your backend checks that `state` matches what it stored. If it doesn't, it rejects the request, because that is a possible CSRF or login-injection attempt.

### 8–9. Code to token exchange (server to server)
Your backend POSTs to `https://github.com/login/oauth/access_token` with `client_id`, **`client_secret`**, `code`, `redirect_uri` (and `code_verifier` if you use PKCE). GitHub returns an `access_token`. This is the only step where the client secret is used, which is why it has to happen on the backend.

### 10–11. Fetch identity
Your backend calls `GET https://api.github.com/user` (and often `/user/emails`, since the primary email may be private) with `Authorization: Bearer <token>`.

### 12. Create your own session
Your backend finds or creates a local user, keyed on GitHub's **numeric user `id`** (not username or email, since those can change). It then issues *your* session cookie or JWT and redirects to the app. From this point, your site uses its own session. The GitHub token is only needed again if you call GitHub APIs on the user's behalf. If you do keep it, store it encrypted.

## Things worth checking in your implementation
- The `state` is generated, stored, and verified, not just passed through.
- The client secret exists only on the server and never in frontend bundles.
- Users are identified by GitHub `id`. Auto-linking to existing accounts by email should only happen for verified emails.
- Scopes are minimal. `read:user user:email` is usually enough for login.
- If it's actually a **GitHub App** instead of an OAuth App, the flow is the same, but tokens expire after 8 hours and come with refresh tokens.

Want me to look at your code and trace where each of these steps happens?
