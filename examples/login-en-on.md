🤔 I didn't look at your code: the working directory is a temp folder, not your repo. Below is the standard GitHub OAuth web flow, which most "Sign in with GitHub" buttons use. Your site may differ (for example, if it uses Auth0 or NextAuth).

**In short:** the browser bounces to GitHub and back with a one-time `code`. Your backend then trades that code, plus its client secret, for an access token, server to server.

```
Browser                    Your backend                     GitHub
   |                            |                              |
1  |-- click "Sign in" -------->|                              |
   |                            | make random `state`,         |
   |                            | save it in session/cookie    |
2  |<-- 302 redirect -----------|                              |
   |    github.com/login/oauth/authorize?client_id&            |
   |    redirect_uri&scope&state                               |
3  |---------------------------------------------------------->|
   |                     user logs in + approves scopes        |
4  |<-- 302 to redirect_uri?code=XYZ&state=... ----------------|
5  |-- GET /callback?code&state>|                              |
   |                            | check state == saved state   |
6  |                            |-- POST /login/oauth/access_token
   |                            |   client_id, client_secret, code -->|
   |                            |<-- access_token -------------|
7  |                            |-- GET api.github.com/user -->|
   |                            |   (+ /user/emails if needed) |
   |                            |<-- id, login, email ---------|
   |                            | find or create user by GitHub id
8  |<-- Set-Cookie: session ----|                              |
   |    redirect to app         |                              |
```

These 4 points matter most for security:

- **`state`**: a random value that blocks CSRF. A login attacker can't forge the callback without it.
- **Client secret**: it lives only on the backend. The browser never sees it or the access token.
- **`code`**: it works once and expires in about 10 minutes.
- **User identity**: key users by GitHub's numeric `id`, not `login` or email. Users can rename `login`, and emails may be private or unverified.

💡 If you point me at the repo, I can trace your actual callback handler and check these 4 points against it.
