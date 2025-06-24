# Engineering Memory Agent 🧠

An internal DevOps co-pilot that understands logs, alerts, incidents, and code changes using LLMs + embeddings.

## 🔥 Features

- Semantic search across logs, incidents, and deploys
- Natural language querying
- Long-term memory with vector database
- Slack/CLI interface

## 🧱 Tech Stack

- Golang + Fiber
- ChromaDB + Redis + Postgres
- OpenAI / Claude
- Docker + GitHub Actions

## 🧪 Running It

```bash
docker-compose up --build


engineering-memory-agent/
├── cmd/                 # Main entrypoint files
│   └── server/          # Where your main.go lives
├── internal/            # Business logic
│   ├── embeddings/      # Vector-related logic
│   ├── ingest/          # Log ingestion handlers
│   └── api/             # API handlers
├── pkg/                 # Shared code/utils
│   └── logger/          # Logging setup
├── configs/             # Config schemas
├── scripts/             # One-off setup/test scripts
├── data/                # logs.json, alerts.json, etc.
├── docker/              # Dockerfiles per service
├── .env                 # Environment config
├── docker-compose.yml   # Infra setup
├── go.mod / go.sum      # Dependency management
├── README.md            # Project doc
└── api_spec.md          # API endpoints
```
mkdir -p engineering-memory-agent/{cmd/server,internal/{embeddings,ingest,api},pkg/logger,configs,scripts,data,docker}
touch engineering-memory-agent/{.env,README.md,api_spec.md,docker-compose.yml,go.mod}
```