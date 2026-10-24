## Recommendation: SQLite ✅

For about 100 users, SQLite is the better fit.

**Why**
- **Simple:** it's one file, with no server to run, secure, or back up separately.
- **Fast enough:** a URL shortener mostly reads (redirects). SQLite handles thousands of reads per second.
- **Cheap:** there's nothing extra to host.

**Setup tips**
- Turn on WAL mode: `PRAGMA journal_mode=WAL;`
- Set `PRAGMA busy_timeout=5000;`
- Back up with Litestream or a scheduled `.backup`.

**When to pick Postgres instead**
- You need multiple app servers writing to the same database.
- You expect heavy write volume or rapid growth.
- Your host has no persistent disk, as with some serverless or container setups.

Moving from SQLite to Postgres later is easy at this size. Keep your SQL fairly standard, or use an ORM, and you won't be locked in.

**Question:** Where will you host it?

A. A single VPS or server with a persistent disk. SQLite fits here, so I recommend this.
B. Serverless or ephemeral containers. Postgres is safer here because the disk may not persist.
C. Not sure yet.
