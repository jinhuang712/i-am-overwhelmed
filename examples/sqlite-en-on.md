# ✅ SQLite

At ~100 users, a URL shortener is a read-heavy workload with tiny rows. SQLite handles that easily.

## Why SQLite
- **Zero ops:** no server, no credentials, no connection pool. Backup is copying one file (or Litestream).
- **Fast reads:** redirects are simple key lookups, in-process with no network hop.
- **Enough write capacity:** with `PRAGMA journal_mode=WAL`, it handles thousands of writes per second. Click counters at 100 users won't come close.

## When I'd pick Postgres instead
- ⚠️ You need **multiple app servers** writing to the same DB.
- ⚠️ Your host has an **ephemeral disk** (some PaaS, serverless), so a local file won't survive.
- You expect to grow **100x** soon, or want managed backups and replicas.

## 💡 Tip
Keep your queries standard and use an ORM or query builder. Moving to Postgres later is then a config change plus a data copy, not a rewrite.

🤔 Postgres for 100 users is over-engineering, unless you already run it and it costs you nothing extra.

Where will this be deployed (single VPS, container with a volume, or serverless)? That's the one thing that could change my answer.
- A. Single VPS or container with a persistent volume → SQLite (recommended)
- B. Serverless or ephemeral disk → Postgres
