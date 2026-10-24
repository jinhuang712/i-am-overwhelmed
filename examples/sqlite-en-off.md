**SQLite.**

For about 100 users, a URL shortener is a read-heavy workload with tiny rows. SQLite handles that easily.

- **Simplicity:** There's no server to run, secure, or back up separately. The database is one file.
- **Performance:** Redirect lookups by primary key on a short code take microseconds. With WAL mode on, SQLite handles thousands of reads per second and enough writes for 100 users.
- **Cost:** It needs no extra process or memory, so a small VPS is plenty.

**Setup tips**
- Enable WAL: `PRAGMA journal_mode=WAL;`
- Set `PRAGMA busy_timeout=5000;` and `PRAGMA synchronous=NORMAL;`
- Make the short code the primary key or put a unique index on it.
- Record click counts in a separate table, or batch the updates. That keeps write contention off the redirect path.
- Back it up with `sqlite3 db ".backup file"` or Litestream, and don't copy the live file.

**When to pick Postgres**
- You expect to run multiple app servers writing to the same database.
- You expect heavy concurrent writes, such as high-volume click analytics.
- Your platform has no persistent disk, as with some serverless setups.
- You want Postgres-specific features or a managed database with built-in backups.

If you outgrow SQLite, migrating a table this simple is easy. Start with SQLite.
