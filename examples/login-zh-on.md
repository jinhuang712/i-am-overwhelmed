这是标准的 OAuth 2.0 授权码流程（Authorization Code flow）。我假设你们用的是它，而不是 device flow 或纯前端 PKCE，这是我的推测，没看你们的代码。

```
Browser            Backend              GitHub
   |                  |                    |
1  |-- GET /auth/github -->|                |
2  |<-- 302 + state ------|                 |
3  |-- GET /login/oauth/authorize?client_id&state -->|
4  |<-------- login + consent page ------------------|
5  |<-------- 302 redirect_uri?code&state ------------|
6  |-- GET /callback?code&state -->|          |
7  |                  |-- POST access_token (code + secret) -->|
8  |                  |<-- access_token ------|
9  |                  |-- GET api.github.com/user -->|
10 |                  |<-- profile -----------|
11 |<-- Set-Cookie session + 302 home --|      |
```

- **state**：第 2 步生成并存进 session，第 6 步必须比对，防 CSRF。
- **code**：一次性、很短命，经过浏览器，所以本身不值钱。
- **client_secret**：只在第 7 步由后端发出，浏览器永远看不到。
- **access_token**：留在后端，浏览器只拿到你们自己的 session cookie。

💡 最常见的坑是漏掉 state 校验，或把 access_token 返回给前端。

想深入哪一块？
- A. ✅ state 与 CSRF 防护怎么做
- B. 第 11 步之后用户与 session 的关联
- C. 排查回调失败（redirect_uri 不匹配等）
