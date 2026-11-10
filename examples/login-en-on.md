Here is the standard OAuth 2.0 "authorization code" flow. I'm guessing your site uses it and haven't checked your code.

```
Browser              Backend                GitHub
   |                    |                      |
1  |--- click --------->|                      |
2  |<-- 302 to GitHub --|                      |
   |    (client_id, scope, state)              |
3  |------------ login + consent ------------->|
4  |<----------- 302 to /callback -------------|
   |             (code, state)                 |
5  |--- /callback ----->|                      |
   |    (code, state)   |                      |
6  |                    |--- code + secret --->|
7  |                    |<-- access_token -----|
8  |                    |--- GET /user ------->|
9  |                    |<-- profile ----------|
10 |<-- session cookie -|                      |
```

- **Steps 1-4**: the browser is only a messenger. It carries redirects between your backend and GitHub.
- **Step 6**: the one that matters. The `code` is short-lived and useless alone. Your backend swaps it for a token using `client_secret`, which never reaches the browser ✅
- **Step 5**: the backend must check that `state` matches what it issued in step 2. Skipping this opens a CSRF hole (forged login) ⚠️
- **Step 10**: your backend creates its own session. GitHub's token usually stays server-side.

💡 If your app is a SPA or mobile app with no secret, use PKCE (a one-time proof sent with the code) instead.

Want me to check your code against these steps, especially the `state` check? Answer yes or no.
