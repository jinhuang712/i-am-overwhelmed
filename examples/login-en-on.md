Assuming the standard OAuth 2.0 "authorization code" flow (I haven't looked at your code, so this is the textbook version):

```
Browser            Your backend             GitHub
   |  1. click        |                        |
   |----------------->|                        |
   |  2. 302 redirect to GitHub (client_id, scope, state)
   |<-----------------|                        |
   |  3. user logs in and approves             |
   |------------------------------------------>|
   |  4. 302 back to your callback (code, state)
   |<------------------------------------------|
   |  5. GET /callback?code&state              |
   |----------------->|                        |
   |                  |  6. code + client_secret
   |                  |----------------------->|
   |                  |  7. access_token       |
   |                  |<-----------------------|
   |                  |  8. GET /user (token)  |
   |                  |----------------------->|
   |                  |  9. profile            |
   |                  |<-----------------------|
   |  10. Set-Cookie session, redirect home    |
   |<-----------------|                        |
```

- **Steps 2-5**: the browser is only a messenger between you and GitHub, and it never sees the token.
- **Step 6**: this is the one secret step. The `client_secret` stays on your backend.
- **`state`**: a random value you save before step 2 and compare at step 5. It blocks login-CSRF (an attacker tricking a user into logging in as the attacker). ⚠️ This is the check most often forgotten.
- **`code`**: single-use and short-lived, so it is useless without your `client_secret`.

💡 My opinion: after step 9, create your own session and discard the GitHub token unless you need to call the GitHub API later.

Next step: want me to check your repo for where each of these steps lives and whether `state` is verified?
