✅ **SQLite.** At ~100 users, a shortener is read-heavy and tiny, so SQLite handles it with zero ops.

```
Request ──► App ──► SQLite file
                    (one file, backup = copy)
```

- **Why**: no separate server to run, patch, or pay for
- **Speed**: redirects are simple key lookups, so microseconds
- **Setup**: turn on WAL mode (write-ahead log, lets reads and writes overlap) with `PRAGMA journal_mode=WAL;`
- **Backups**: use Litestream or a nightly copy

⚠️ **Premise to check**: SQLite assumes one app server with a local disk. If you deploy on serverless or run several instances, Postgres fits better.

🤔 **Switch to Postgres if**:
- You need multiple app servers
- Click analytics produce heavy concurrent writes
- You plan to grow well beyond 100 users

Q1. Will this run on a single server with a persistent disk? (yes/no)
