**SQLite.** At ~100 users, it's not close.

**Why SQLite fits:**
- A URL shortener is mostly reads (redirects), with occasional writes when someone creates a link. SQLite handles that easily, even with thousands of redirects per second.
- There's no server to run, secure, or back up separately. It's one file, and you can back it up with `sqlite3 db .backup` or Litestream.
- Lookups by slug are a single indexed primary-key read, which takes microseconds.

**Settings worth turning on:**
```sql
PRAGMA journal_mode = WAL;     -- concurrent reads during writes
PRAGMA busy_timeout = 5000;    -- avoid "database is locked" errors
PRAGMA synchronous = NORMAL;   -- safe with WAL, faster
```

**When to pick Postgres instead:**
- You'll run multiple app servers or containers that all need to write to the same DB. SQLite wants a single host.
- Your platform has ephemeral disks, like Heroku or some serverless setups, and no persistent volume.
- You expect heavy write-side analytics, such as logging every click with rich metadata at high volume. Even then, batching the inserts usually keeps SQLite fine.
- Your team already runs Postgres and a managed instance costs you nothing extra to operate.

If you keep your SQL fairly standard, or use an ORM, switching to Postgres later is a small migration.
