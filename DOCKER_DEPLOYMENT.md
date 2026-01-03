# Docker Deployment Guide for SeleniumBase UC Mode

## Overview

This Docker configuration is optimized for SeleniumBase UC Mode (Undetected Chrome) with virtual display support using Xvfb. The virtual display is crucial for bypassing sophisticated bot detection systems.

## Key Features

- **Base Image**: `python:3.10-slim-buster` for optimal Chrome compatibility
- **Virtual Display**: Xvfb provides a virtual X11 display so UC Mode thinks it has a GUI
- **UC Mode Enabled**: Undetected Chrome mode for bypassing bot detection
- **CDP Mode**: Chrome DevTools Protocol for advanced stealth interactions
- **Chrome Stable**: Latest Google Chrome with all dependencies

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Docker Container                          │
│                                                              │
│  ┌──────────────┐    ┌──────────────────────────────────┐  │
│  │   Xvfb       │    │   Application (FastAPI/Uvicorn)   │  │
│  │  (Virtual    │───▶│   - SeleniumBase UC Mode          │  │
│  │   Display)   │    │   - StealthScrape Engine          │  │
│  │  :99         │    │   - API Endpoints                 │  │
│  └──────────────┘    └──────────────────────────────────┘  │
│         │                        │                          │
│         └────────────────────────┘                          │
│                        │                                     │
│         ┌──────────────┴──────────────┐                     │
│         │                             │                     │
│  ┌──────▼──────┐              ┌──────▼──────┐              │
│  │   Chrome    │              │  Selenium   │              │
│  │   Stable    │              │   Base      │              │
│  └─────────────┘              └─────────────┘              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Build the Docker Image

```bash
docker build -t stealthscrape:latest .
```

### 2. Run with Docker Compose (Recommended)

```bash
docker-compose up -d
```

This will start:
- StealthScrape application with UC Mode
- Redis for session management
- PostgreSQL for data persistence
- Prometheus for metrics
- Grafana for monitoring

### 3. Run Standalone Container

```bash
docker run -d \
  --name stealthscrape \
  -p 8000:8000 \
  -e STEALTHSCRAPE_ENV=production \
  -e UC_MODE=true \
  -e CDP_MODE=true \
  -e DISPLAY=:99 \
  -v $(pwd)/scraped_data:/app/scraped_data \
  -v $(pwd)/logs:/app/logs \
  stealthscrape:latest
```

## Environment Variables

### Required for UC Mode

| Variable | Default | Description |
|----------|---------|-------------|
| `DISPLAY` | `:99` | Virtual display for Xvfb (required for UC Mode) |
| `UC_MODE` | `true` | Enable Undetected Chrome mode |
| `CDP_MODE` | `true` | Enable Chrome DevTools Protocol mode |
| `SELENIUM_HEADLESS` | `false` | Disable headless mode (UC Mode needs display) |

### Application Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `STEALTHSCRAPE_ENV` | `production` | Environment (development/production) |
| `PORT` | `8000` | Application port |
| `HOST` | `0.0.0.0` | Application host |
| `STEALTH_LEVEL` | `maximum` | Stealth level (low/medium/maximum) |

### Test Credentials (Optional)

| Variable | Description |
|----------|-------------|
| `FB_USER` / `FB_PASSWORD` | Facebook test credentials |
| `IG_USER` / `IG_PASSWORD` | Instagram test credentials |
| `TW_USER` / `TW_PASSWORD` | Twitter test credentials |
| `AMAZON_EMAIL` / `AMAZON_PASSWORD` | Amazon test credentials |
| `SHOPIFY_STORE` / `SHOPIFY_EMAIL` / `SHOPIFY_PASSWORD` | Shopify test credentials |

## How Xvfb Enables UC Mode

### Why Virtual Display is Critical

UC Mode (Undetected Chrome) needs to appear as a legitimate browser to bypass bot detection. This includes:

1. **Browser Fingerprinting**: UC Mode checks for display properties
2. **WebGL Rendering**: Some sites check GPU capabilities
3. **Canvas Fingerprinting**: Needs proper display context
4. **Timing Analysis**: Real browser behavior patterns

### Xvfb Configuration

The Dockerfile uses:
```bash
xvfb-run -a --server-args="-screen 0 1920x1080x24"
```

- `-a`: Auto-select display number (defaults to :99)
- `--server-args="-screen 0 1920x1080x24"`: Creates a 1920x1080 display with 24-bit color depth

This provides:
- Full HD resolution (1920x1080)
- 24-bit color depth (16.7 million colors)
- Virtual display that Chrome can render to

## Dockerfile Breakdown

### Base Image Selection
```dockerfile
FROM python:3.10-slim-buster
```
- `python:3.10`: Stable Python 3.10 release
- `slim`: Minimal image size
- `buster`: Debian 10 (better Chrome compatibility than bullseye/bookworm)

### System Dependencies
```dockerfile
RUN apt-get install -y \
    xvfb \                    # Virtual display
    google-chrome-stable \    # Chrome browser
    libgbm-dev \              # GPU buffer management
    libnss3 \                 # Network Security Services
    libasound2 \              # Audio support
    # ... other dependencies
```

### Chrome Installation
```dockerfile
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get install -y google-chrome-stable
```

### Environment Variables
```dockerfile
ENV DISPLAY=:99
ENV SELENIUM_HEADLESS=false
ENV UC_MODE=true
ENV CDP_MODE=true
```

### Startup Command
```dockerfile
CMD ["xvfb-run", "-a", "--server-args=-screen 0 1920x1080x24", \
     "uvicorn", "src.backend.api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
```

## Troubleshooting

### Issue: Chrome fails to start

**Symptoms**: `chrome not reachable` or `session not created` errors

**Solutions**:
1. Check Chrome version: `docker exec stealthscrape google-chrome --version`
2. Verify Xvfb is running: `docker exec stealthscrape ps aux | grep xvfb`
3. Check logs: `docker logs stealthscrape`

### Issue: Bot detection still triggers

**Symptoms**: 403 Forbidden, CAPTCHA, or access denied

**Solutions**:
1. Ensure `UC_MODE=true` is set
2. Verify `SELENIUM_HEADLESS=false` (UC Mode needs display)
3. Check `DISPLAY=:99` is set correctly
4. Try increasing `STEALTH_LEVEL` to `maximum`
5. Consider using residential proxies

### Issue: Container exits immediately

**Symptoms**: Container starts and stops immediately

**Solutions**:
1. Check application logs: `docker logs stealthscrape`
2. Verify all environment variables are set
3. Ensure port 8000 is not already in use
4. Check health endpoint: `curl http://localhost:8000/health`

### Issue: High memory usage

**Symptoms**: Container using excessive memory

**Solutions**:
1. Reduce worker count in docker-compose.yml
2. Limit Chrome instances in application config
3. Use `--memory` flag: `docker run --memory="2g" ...`
4. Enable headless mode for non-critical operations

## Performance Optimization

### Resource Limits

Add to docker-compose.yml:
```yaml
services:
  stealthscrape-app:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

### Worker Configuration

For production, adjust workers based on CPU cores:
```yaml
# 4 CPU cores: 2 workers
# 8 CPU cores: 4 workers
CMD ["xvfb-run", "-a", "--server-args=-screen 0 1920x1080x24", \
     "uvicorn", "src.backend.api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
```

### Volume Optimization

Use tmpfs for temporary files:
```yaml
volumes:
  - /tmp:/tmp
```

## Security Considerations

### 1. Environment Variables

Never commit `.env` file with real credentials. Use:
```bash
docker run -e FB_USER=user@example.com -e FB_PASSWORD=secret ...
```

Or use Docker secrets:
```yaml
secrets:
  fb_password:
    file: ./secrets/fb_password.txt
```

### 2. Network Isolation

Use dedicated network:
```yaml
networks:
  stealthscrape-network:
    driver: bridge
    internal: false  # Set to true to block external access
```

### 3. User Permissions

Run as non-root user (add to Dockerfile):
```dockerfile
RUN useradd -m -u 1000 appuser
USER appuser
```

## Monitoring

### Health Checks

The container includes a health check:
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl -f http://localhost:8000/health || exit 1
```

Check health status:
```bash
docker inspect --format='{{.State.Health.Status}}' stealthscrape
```

### Logs

View application logs:
```bash
docker logs -f stealthscrape
```

View logs from docker-compose:
```bash
docker-compose logs -f stealthscrape-app
```

### Metrics

Access Prometheus metrics:
```bash
curl http://localhost:9090/metrics
```

Access Grafana dashboard:
```
http://localhost:3000
Username: admin
Password: admin
```

## Testing

### Run Tests in Container

```bash
# Build image
docker build -t stealthscrape:test .

# Run tests
docker run --rm \
  -e FB_USER=test@example.com \
  -e FB_PASSWORD=testpass \
  -v $(pwd)/reports:/app/reports \
  stealthscrape:test \
  pytest tests/ --dashboard --html=reports/report.html
```

### Run E2E Tests with Credentials

```bash
docker run --rm \
  -e FB_USER=real@example.com \
  -e FB_PASSWORD=realpass \
  -e IG_USER=realuser \
  -e IG_PASSWORD=realpass \
  -v $(pwd)/reports:/app/reports \
  stealthscrape:test \
  pytest tests/e2e/ --dashboard --html=reports/e2e_report.html
```

## Production Deployment

### 1. Build Production Image

```bash
docker build -t stealthscrape:prod .
```

### 2. Tag for Registry

```bash
docker tag stealthscrape:prod registry.example.com/stealthscrape:latest
```

### 3. Push to Registry

```bash
docker push registry.example.com/stealthscrape:latest
```

### 4. Deploy with Docker Compose

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### 5. Scale for Load

```bash
docker-compose up -d --scale stealthscrape-app=3
```

## Maintenance

### Update Chrome

```bash
docker exec stealthscrape apt-get update
docker exec stealthscrape apt-get install --only-upgrade google-chrome-stable
```

### Update Python Dependencies

```bash
docker exec stealthscrape pip install --upgrade -r requirements.txt
```

### Clean Up

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune
```

## Support

For issues related to:
- **Docker**: Check Docker logs and container status
- **UC Mode**: Verify environment variables and Xvfb status
- **SeleniumBase**: Review SeleniumBase documentation
- **Chrome**: Check Chrome version and compatibility

## References

- [SeleniumBase Documentation](https://seleniumbase.io/)
- [UC Mode Guide](https://seleniumbase.io/help_docs/uc_mode/)
- [Docker Documentation](https://docs.docker.com/)
- [Xvfb Manual](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml)
