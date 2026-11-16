# P0 Disaster Recovery & Multi-Cloud Failover Runbook

## Service: Team Obsidian Knowledge Gateway
- **Target RTO**: < 15 minutes
- **Target RPO**: < 1 hour

### 1. Alerting Triggers
- Sentry alert: `RedisConnectionPoolTimeout` > 10 events / min
- API Healthcheck `GET /health` latency > 2000ms

### 2. Immediate Mitigation Actions
1. Restart worker pool: `systemctl restart obsidian-worker`
2. Clear dead Redis connection handles: `redis-cli client kill type normal`
3. Verify database replication health: `SELECT * FROM pg_stat_replication;`
