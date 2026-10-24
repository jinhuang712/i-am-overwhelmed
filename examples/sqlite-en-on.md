## Recommendation: SQLite ✅

For ~100 users, SQLite is the better fit.

**Why**
- A URL shortener is read-heavy (redirects), and SQLite handles that very well.
- There's no separate server to run, secure, or back up. The database is one file.
- 100 users won't come close to its write limits. Turn on WAL mode and it handles thousands of writes per second.
- Deploying is simpler and costs less.

**Setup tips**
- Enable `PRAGMA journal_mode=WAL;`
- Set `PRAGMA busy_timeout=5000;`
- Put a unique index on the short code.
- Back up with Litestream or a nightly `.backup`.

**When I'd pick Postgres instead**
- You need multiple app servers writing to the same database.
- You expect to grow far beyond this, or want managed hosting with built-in failover.
- Your host has no persistent disk (some serverless platforms), so a file database won't survive.

**Caveat:** I'm assuming a single server. If you plan to run on serverless or several instances, tell me and I'd change this.

**Question:** Where will you deploy it?
- A. One VPS or container with a persistent disk (SQLite fits, **recommended**)
- B. Serverless or multiple instances (Postgres fits)
- C. Not sure yet (start with SQLite, since moving to Postgres later is easy with a standard ORM)
