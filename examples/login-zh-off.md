这是标准的 OAuth 2.0 授权码流程（Authorization Code Flow）。

## 时序

```
浏览器                    我们的后端                    GitHub
  |  1. 点「用 GitHub 登录」  |                            |
  |------------------------->|                            |
  |                          | 生成 state（可选 PKCE）存 session
  |  2. 302 到 GitHub 授权页  |                            |
  |<-------------------------|                            |
  |  3. GET /login/oauth/authorize?client_id&redirect_uri&scope&state
  |------------------------------------------------------>|
  |  4. 用户登录 GitHub（如未登录）并点「Authorize」          |
  |<----------------------------------------------------->|
  |  5. 302 到 redirect_uri?code=xxx&state=yyy             |
  |<------------------------------------------------------|
  |  6. GET /auth/github/callback?code&state              |
  |------------------------->|                            |
  |                          | 7. 校验 state 与 session 中一致
  |                          | 8. POST /login/oauth/access_token
  |                          |    (client_id, client_secret, code, redirect_uri)
  |                          |--------------------------->|
  |                          |    access_token            |
  |                          |<---------------------------|
  |                          | 9. GET api.github.com/user
  |                          |    Authorization: Bearer <token>
  |                          |--------------------------->|
  |                          |    id, login, avatar...    |
  |                          |<---------------------------|
  |                          | 10. 查找/创建本地用户，建立会话
  | 11. Set-Cookie: session + 302 到首页                    |
  |<-------------------------|                            |
```

## 各步骤要点

1. **发起**：后端生成随机 `state`（防 CSRF），存进 session 或签名 cookie。如果用 PKCE，同时生成 `code_verifier` 并把 `code_challenge` 带上。
2. **跳转授权页**：参数有 `client_id`、`redirect_uri`、`scope`（只要登录用 `read:user`，要邮箱再加 `user:email`）和 `state`。
3. **用户授权**：这一步完全发生在浏览器和 GitHub 之间，我们的后端看不到。
4. **回调**：GitHub 把用户重定向回我们预先注册的 `redirect_uri`，带上一次性的 `code`（短时效，约 10 分钟）和原样返回的 `state`。
5. **校验 state**：不一致就直接拒绝，这是防登录 CSRF 的关键。
6. **换 token**：后端用 `code` + `client_secret` 向 GitHub 请求 `access_token`。这一步是服务器对服务器，`client_secret` 不会暴露给浏览器。请求时加 `Accept: application/json`，否则 GitHub 默认返回 form 编码格式。
7. **取用户信息**：用 token 调 `GET /user`。如果需要邮箱，再调 `GET /user/emails`，因为用户可能把邮箱设为私密，`/user` 里的 `email` 可能为空。
8. **建立本地会话**：用 GitHub 的**数字 `id`** 作为唯一标识去匹配或创建本地用户，不要用 `login`（可改名）或 email。然后下发自己的会话 cookie（`HttpOnly; Secure; SameSite=Lax`）。

## 容易踩的点

- `access_token` 只留在后端。如果只用来登录，用完就可以丢掉，不必存。
- `redirect_uri` 必须和 GitHub OAuth App 中注册的一致，否则授权会失败。
- `code` 只能用一次。
- 登录之后浏览器和 GitHub 就没关系了，后续请求只带我们自己的 session cookie。

如果你想对照项目里的实际实现来检查（比如 state 校验、用什么字段做用户唯一标识），告诉我代码在哪，我可以帮你看。
