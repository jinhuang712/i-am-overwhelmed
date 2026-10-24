**SQLite.**

For about 100 users, a URL shortener is a read-heavy workload: lots of redirects and few writes. SQLite handles that easily.

- **Performance:** In WAL mode, SQLite serves thousands of reads per second and hundreds of writes per second. That is far more than 100 users will generate.
- **Operations:** It's a single file, so there's no server to run, patch or secure. Backups are a file copy, or you can use Litestream for continuous replication.
- **Cost and complexity:** You don't need a separate database host, connection pooling or network credentials.

Settings to use:
```sql
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA busy_timeout = 5000;
PRAGMA foreign_keys = ON;
```
Put a unique index on the short code.

Choose Postgres instead if:
- You need to run multiple app servers that share one database. SQLite wants a single host with local disk.
- You expect heavy concurrent writes, such as high-volume click-tracking inserts.
- Your platform has no persistent disk, as with many serverless or ephemeral-container setups.
- You already run Postgres and want to reuse it.

If you write the data layer with a thin abstraction or a portable query builder (or ORM), moving to Postgres later is a modest migration. Starting with SQLite doesn't lock you in.

If you log every click, write those inserts through a single queue or batch them. That keeps write contention low.
