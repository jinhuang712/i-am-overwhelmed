这是标准的 **OAuth 2.0 授权码流程**：浏览器只负责来回跳转，真正拿 token 和查用户信息的是后端对 GitHub 的直连请求，`client_secret` 不经过浏览器。

> ⚠️ 我没看你们的代码，下面是 GitHub OAuth App 的标准流程。你们的实现可能有差异，比如用了 Passport、NextAuth 之类的库。

完整交互分 6 步：

```
Browser                     Our Backend                         GitHub
   |                             |                                  |
   | 1. click "Login w/ GitHub"  |                                  |
   |---------------------------->|                                  |
   |                             | gen state, save in session       |
   | 302 -> github.com/login/oauth/authorize                        |
   |     ?client_id&redirect_uri&scope&state                        |
   |<----------------------------|                                  |
   |                                                                |
   | 2. user logs in + clicks "Authorize"                           |
   |--------------------------------------------------------------->|
   |                                                                |
   | 3. 302 -> our /callback?code=XXX&state=YYY                     |
   |<---------------------------------------------------------------|
   |                             |                                  |
   |---------------------------->|                                  |
   |                             | check state == session.state     |
   |                             |                                  |
   |                             | 4. POST /login/oauth/access_token|
   |                             |    client_id + client_secret     |
   |                             |    + code                        |
   |                             |--------------------------------->|
   |                             |<-------- access_token -----------|
   |                             |                                  |
   |                             | 5. GET api.github.com/user       |
   |                             |    (+ /user/emails)              |
   |                             |--------------------------------->|
   |                             |<-------- id, login, email -------|
   |                             |                                  |
   |                             | 6. find/create user by GitHub id |
   | Set-Cookie: our session     |    issue OUR session             |
   | 302 -> home                 |                                  |
   |<----------------------------|                                  |
```

4 个容易出错的点：

- **state**：后端生成随机值并存入 session，回调时必须比对，用来防 CSRF 登录攻击。
- **code**：它只能用一次，大约 10 分钟内过期。它出现在浏览器 URL 里，所以本身不能当凭证用。
- **client_secret**：它只在第 4 步由后端发出，绝对不能出现在前端代码里。
- **用户匹配**：要用 GitHub 的数字 `id` 来关联账号，不要用 `login` 或 email。用户名可以改，email 可能为空或者未验证。

💡 第 6 步之后，GitHub 的 access_token 和你们自己的登录态就分开了。除非后续还要调 GitHub API，否则不用存这个 token，存了反而多一份泄露风险。

如果想核对你们的实现是否符合上面的流程，把回调处理的代码路径发我就行。
