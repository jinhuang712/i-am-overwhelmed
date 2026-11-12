这是标准的 **OAuth 2.0 授权码流程（Authorization Code Flow）**。整个过程分为以下几步：

## 时序概览

```
浏览器                 你的后端                     GitHub
  |  1. 点击登录          |                            |
  |--------------------->|                            |
  |  2. 302 重定向到 GitHub (带 client_id, state...)    |
  |<---------------------|                            |
  |  3. 访问 github.com/login/oauth/authorize          |
  |-------------------------------------------------->|
  |  4. 用户登录 GitHub 并点击“授权”                     |
  |  5. 302 重定向回 callback?code=xxx&state=yyy       |
  |<--------------------------------------------------|
  |  6. 访问你的 callback  |                            |
  |--------------------->|  7. 用 code 换 access_token |
  |                      |--------------------------->|
  |                      |<---------------------------|
  |                      |  8. 用 token 拉取用户信息    |
  |                      |--------------------------->|
  |                      |<---------------------------|
  |  9. 建立会话(Set-Cookie)，跳转到站内页面            |
  |<---------------------|                            |
```

## 各步骤详解

**1–2. 发起授权（浏览器 → 后端）**
后端生成一个随机 `state`，存入 session 或 cookie，然后返回 302 重定向到：
```
https://github.com/login/oauth/authorize
  ?client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yoursite.com/auth/github/callback
  &scope=read:user user:email
  &state=随机字符串
```
- `state` 用于防御 CSRF。
- 如有需要，还可以加上 PKCE 参数（`code_challenge` / `code_challenge_method=S256`），GitHub 已支持。

**3–4. 用户在 GitHub 上授权**
如果用户还没登录 GitHub，会先完成登录。随后 GitHub 展示授权页面，列出你的应用和申请的权限范围。用户此前授权过的话，这一步会自动跳过。

**5–6. 回调（GitHub → 浏览器 → 后端）**
GitHub 把浏览器重定向到你的 `redirect_uri`，并带上 `?code=一次性授权码&state=原样返回`。
后端收到后必须先校验 `state` 与第 1 步保存的一致，不一致就拒绝请求。

**7. 用 code 换 token（后端 ↔ GitHub，服务器之间直连）**
```
POST https://github.com/login/oauth/access_token
Accept: application/json

client_id=...&client_secret=...&code=...&redirect_uri=...
```
返回 `access_token`。`client_secret` 只出现在这一步的服务器之间请求里，**绝不能暴露给浏览器**。`code` 只能使用一次，有效期很短（约 10 分钟）。

**8. 获取用户身份**
```
GET https://api.github.com/user
Authorization: Bearer <access_token>
```
从返回结果中拿到 `id`、`login`、`avatar_url` 等信息。如果需要邮箱，再调用 `GET /user/emails`，取其中 `primary` 且 `verified` 的那一个。

**9. 建立你自己的登录态**
- 用 GitHub 的 **`id`**（数字，永久不变）关联或创建本地用户。不要用 `login` 用户名，因为用户可以改名。
- 签发你自己的 session cookie 或 JWT，然后重定向到首页或用户登录前所在的页面。
- 如果之后不需要代表用户调用 GitHub API，可以直接丢弃 access_token；如果需要，就加密保存。

## 关键安全要点
| 要点 | 原因 |
|---|---|
| 校验 `state` | 防止 CSRF 登录攻击 |
| `client_secret` 只放后端 | 防止应用被冒用 |
| `redirect_uri` 与 GitHub App 配置严格一致 | 防止 code 被重定向到攻击者的地址 |
| 用 GitHub 用户 `id` 关联账号 | 用户名可以修改 |
| 按邮箱合并已有账号前，先确认邮箱已 verified | 防止账号接管 |
| scope 只申请需要的最小权限 | 降低 token 泄露后的影响 |

如果你需要，我可以看一下你们项目里实际的回调实现代码，帮忙检查有没有遗漏的地方。
