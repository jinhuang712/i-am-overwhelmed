✅ **SQLite.** At ~100 users, a URL shortener does one indexed lookup per redirect, and SQLite handles thousands of those per second on one file with nothing to run or patch. (Typical figure, not benchmarked here.)

Postgres only pays off if you run more than one server or host without a persistent disk:

```
Where does the app run?
├── One server or VM, persistent disk     → SQLite ✅
├── Several app instances                 → Postgres
└── Serverless / ephemeral containers     → Postgres (or hosted SQLite, e.g. Turso)
    (the file gets wiped on redeploy)
```

3 tips if you pick SQLite:

- **WAL mode**: Turn it on so reads keep working while a write is in progress.
- **Backups**: Use Litestream, or a nightly copy made with the SQLite backup command. A plain `cp` of a live database file can give you a corrupted copy.
- **Exit path**: Keep your SQL plain, and moving to Postgres later is about an afternoon of work. 😄

> If "100 users" means 100 accounts but the short links go viral, the read load still stays small. Redirects are cheap.

💬 Will the app run on a single server with a persistent disk?
