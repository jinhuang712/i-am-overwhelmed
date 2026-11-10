✅ **SQLite.** At ~100 users a URL shortener is a tiny, read-heavy workload (lookup a slug, redirect), and SQLite handles thousands of reads per second on one box.

```
SQLite                    Postgres
├── no server to run      ├── separate service to run
├── one file to back up   ├── users, backups, upgrades
└── fast local reads      └── pays off at multi-server scale
```

- **Turn on WAL mode** (write-ahead logging, which lets reads continue during writes): `PRAGMA journal_mode=WAL;`
- **Migration is cheap**: a `links(slug, url, created_at)` table moves to Postgres in an afternoon if you outgrow it.

⚠️ **Premise I'm assuming**: one app server with a local disk. SQLite struggles if you run several servers or a platform with ephemeral disks (like many serverless hosts).

Q1. Where will this run? (Quick: e.g. "one VPS", "Vercel", "Fly with 2 machines")
