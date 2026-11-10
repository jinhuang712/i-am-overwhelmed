Here is the standard OAuth 2.0 authorization code flow that "Sign in with GitHub" uses. I haven't looked at your code, so check the details (endpoints, scopes, session handling) against your implementation.

## Step by step

**1. Browser → your backend: start login**
The user clicks the button, which goes to something like `GET /auth/github`.

**2. Backend → browser: redirect to GitHub**
Your backend generates a random `state` value, stores it (in the session or a signed cookie), and replies with a `302` to:
```
https://github.com/login/oauth/authorize
  ?client_id=<your client id>
  &redirect_uri=https://yoursite.com/auth/github/callback
  &scope=read:user user:email
  &state=<random>
```
Optionally, it also sends a PKCE `code_challenge`.

**3. Browser ↔ GitHub: login and consent**
The browser follows the redirect. The user logs in to GitHub if needed and approves the requested scopes. Your backend is not involved here, and your site never sees the user's GitHub password.

**4. GitHub → browser → your backend: callback**
GitHub redirects the browser to your `redirect_uri`:
```
GET /auth/github/callback?code=<short-lived code>&state=<same state>
```
The `code` is single-use and expires quickly, and it is not an access token.

**5. Backend: verify `state`**
Your backend compares the `state` in the URL with the one it stored. If they don't match, it rejects the request. This protects against login CSRF.

**6. Backend → GitHub: exchange the code for a token** (server to server)
```
POST https://github.com/login/oauth/access_token
  client_id, client_secret, code, redirect_uri  (+ code_verifier if PKCE)
```
GitHub responds with an `access_token`. The `client_secret` is sent only here, from your server, never through the browser.

**7. Backend → GitHub API: fetch the user's identity**
```
GET https://api.github.com/user
Authorization: Bearer <access_token>
```
If you need the email, also call `GET /user/emails`. Use the numeric `id` as the stable identifier, since usernames and emails can change.

**8. Backend: create or link the local account**
Look up the user by GitHub `id`, creating a record if none exists. Then create your own session.

**9. Backend → browser: log the user in**
Your backend sets a session cookie (`HttpOnly`, `Secure`, `SameSite=Lax`) and redirects to your app, for example `302 /dashboard`. From then on the browser authenticates to your backend with that cookie. GitHub is no longer involved unless you store the access token to call its API later.

## Diagram

```
Browser            Your backend              GitHub
  | --click------->  |                         |
  | <--302 + state-- |                         |
  | ------------------authorize?client_id...-->|
  | <-----------------login/consent------------>|
  | <-----------------302 ?code&state----------|
  | --callback?code&state-->|                  |
  |                  | --POST access_token---->|
  |                  | <--access_token---------|
  |                  | --GET /user------------>|
  |                  | <--profile--------------|
  | <--Set-Cookie, 302 /app--|                 |
```

## Common pitfalls
- Skipping the `state` check.
- Treating the email or username as the identity key instead of the GitHub `id`.
- Exposing `client_secret` to frontend code.
- Using a `redirect_uri` that doesn't exactly match the one registered in the GitHub OAuth app.
- Storing the access token unencrypted if you keep it.

If you'd like, I can point to where each step lives in your codebase. I'd need you to open or point me at the project, since the current directory doesn't contain it.
