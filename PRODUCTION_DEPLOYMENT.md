# Production Deployment Guide

This guide covers operational concerns and pre-flight checks to ensure StealthScrape AI runs successfully in production environments.

## 📋 Pre-Flight Checklist

Before deploying to production, complete these critical checks:

### 1. ✅ The "Fuel" Check: Residential Proxies

**Why This Matters**: UC Mode makes you look human, but your IP address still behaves like a bot if making thousands of requests from a single server IP. AWS/Azure IPs are flagged immediately by Cloudflare.

**Required Action**: Purchase residential proxies from a reputable provider.

#### Recommended Proxy Providers
- **BrightData** (formerly Luminati) - Industry leader
- **Smartproxy** - Good balance of price/performance
- **IPRoyal** - Budget-friendly residential proxies
- **Oxylabs** - Premium residential proxies

#### Configuration

**Option A: Single Proxy**
```env
# In .env file or GitHub Secrets
PROXY=user:pass@proxy.example.com:8080
```

**Option B: Proxy List for Rotation**
```env
# Multiple proxies for automatic rotation
PROXY_LIST=user:pass@192.168.1.100:8080,user:pass@192.168.1.101:8080,user:pass@192.168.1.102:8080
PROXY_ROTATION_INTERVAL=300  # Rotate every 5 minutes
PROXY_POOL_SIZE=10
```

**Option C: Proxy API (Dynamic)**
```env
PROXY_API_KEY=your_api_key_here
PROXY_API_ENDPOINT=https://api.proxy-provider.com/get-proxy
```

#### Verification

Test your proxy manually before deployment:
```bash
# Test proxy connectivity
curl -x user:pass@proxy.example.com:8080 https://httpbin.org/ip

# Expected output should show proxy IP, not your real IP
```

#### GitHub Secrets Configuration

Add these secrets to your repository:
1. Go to **Repository Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add the following secrets:

```
PROXY=user:pass@proxy.example.com:8080
PROXY_ROTATION_INTERVAL=300
PROXY_POOL_SIZE=10
```

---

### 2. ✅ The "Key" Check: GitHub Secrets Configuration

**Why This Matters**: Your CI/CD pipeline skips E2E tests if credentials are missing. A "Passing" (Green) pipeline might only be passing because it's skipping the hard tests.

**Required Action**: Configure all necessary secrets for E2E testing.

#### Required GitHub Secrets

Add these secrets to your repository settings:

| Secret Name | Description | Required For |
|-------------|-------------|--------------|
| `FB_USER` | Facebook email/username | Facebook E2E tests |
| `FB_PASSWORD` | Facebook password | Facebook E2E tests |
| `IG_USER` | Instagram username | Instagram E2E tests |
| `IG_PASSWORD` | Instagram password | Instagram E2E tests |
| `TW_USER` | Twitter username | Twitter E2E tests |
| `TW_PASSWORD` | Twitter password | Twitter E2E tests |
| `AMAZON_EMAIL` | Amazon email | Amazon E2E tests |
| `AMAZON_PASSWORD` | Amazon password | Amazon E2E tests |
| `SHOPIFY_STORE` | Shopify store URL | Shopify E2E tests |
| `SHOPIFY_EMAIL` | Shopify email | Shopify E2E tests |
| `SHOPIFY_PASSWORD` | Shopify password | Shopify E2E tests |
| `PROXY` | Proxy string (user:pass@host:port) | All E2E tests |
| `DOCKER_USERNAME` | Docker Hub username | Docker deployment |
| `DOCKER_PASSWORD` | Docker Hub password/token | Docker deployment |

#### Step-by-Step Configuration

1. **Navigate to Secrets**:
   ```
   Repository → Settings → Secrets and variables → Actions → New repository secret
   ```

2. **Add Each Secret**:
   - Name: `FB_USER`
   - Value: `your_facebook_email@example.com`
   - Click **Add secret**

3. **Repeat** for all required secrets

4. **Verify Configuration**:
   - Go to **Actions** tab
   - Run the workflow manually to verify secrets are loaded correctly

#### Security Best Practices

- ✅ Use **environment-specific secrets** (separate for dev/staging/prod)
- ✅ Rotate credentials regularly (every 90 days)
- ✅ Use **GitHub Actions secrets** (not repository variables) for sensitive data
- ✅ Enable **branch protection rules** to require approval for secret changes
- ✅ Use **GitHub Environments** for different deployment stages

---

### 3. ✅ The "Black Box" Check: Data Persistence

**Why This Matters**: Docker containers are ephemeral. When the container stops, all scraped data is lost unless properly persisted.

**Required Action**: Choose and implement a data persistence strategy.

#### Option A: Docker Volumes (Recommended for Local/Small-Scale)

**Usage**:
```bash
# Create local data directory
mkdir -p ./scraped_data

# Run container with volume mount
docker run --rm \
  --shm-size=2g \
  -v $(pwd)/scraped_data:/app/scraped_data \
  -e PROXY="user:pass@proxy.example.com:8080" \
  stealth-scraper
```

**Pros**:
- Simple to set up
- Direct access to files
- No additional infrastructure

**Cons**:
- Limited to single machine
- Manual backup required
- Not suitable for distributed deployment

#### Option B: Cloud Storage (Recommended for Production)

**AWS S3**:
```python
# Add to requirements.txt
boto3

# In your scraping script
import boto3
import json

def save_to_s3(data, bucket_name, key):
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(data),
        ContentType='application/json'
    )
```

**Google Cloud Storage**:
```python
# Add to requirements.txt
google-cloud-storage

# In your scraping script
from google.cloud import storage

def save_to_gcs(data, bucket_name, key):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(key)
    blob.upload_from_string(json.dumps(data), content_type='application/json')
```

**Azure Blob Storage**:
```python
# Add to requirements.txt
azure-storage-blob

# In your scraping script
from azure.storage.blob import BlobServiceClient

def save_to_azure(data, connection_string, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(json.dumps(data), overwrite=True)
```

#### Option C: Database (Recommended for Structured Data)

**PostgreSQL**:
```python
# Add to requirements.txt
psycopg2-binary

# In your scraping script
import psycopg2
from psycopg2.extras import Json

def save_to_postgres(data, db_config):
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO scraped_data (platform, url, data, scraped_at) VALUES (%s, %s, %s, NOW())",
        (data['platform'], data['url'], Json(data))
    )
    conn.commit()
    cur.close()
    conn.close()
```

**MongoDB**:
```python
# Add to requirements.txt
pymongo

# In your scraping script
from pymongo import MongoClient

def save_to_mongodb(data, connection_string, database, collection):
    client = MongoClient(connection_string)
    db = client[database]
    coll = db[collection]
    coll.insert_one(data)
    client.close()
```

#### Option D: Webhook/API (Recommended for Real-Time Processing)

**Send to Webhook**:
```python
# In your scraping script
import requests

def send_to_webhook(data, webhook_url):
    response = requests.post(
        webhook_url,
        json=data,
        headers={'Content-Type': 'application/json'}
    )
    response.raise_for_status()
```

**Configuration**:
```env
# In .env file
WEBHOOK_URL=https://your-api.com/webhook/scraped-data
WEBHOOK_AUTH_TOKEN=your_auth_token_here
```

#### Implementation Example

Update your scraping script to include data persistence:

```python
import os
import json
import boto3
from pathlib import Path

class DataPersistence:
    def __init__(self, strategy='local', config=None):
        self.strategy = strategy
        self.config = config or {}
        
    def save(self, data, filename):
        if self.strategy == 'local':
            self._save_local(data, filename)
        elif self.strategy == 's3':
            self._save_s3(data, filename)
        elif self.strategy == 'webhook':
            self._save_webhook(data)
            
    def _save_local(self, data, filename):
        output_dir = Path(self.config.get('output_dir', './scraped_data'))
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = output_dir / filename
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
    def _save_s3(self, data, filename):
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket=self.config['bucket_name'],
            Key=filename,
            Body=json.dumps(data),
            ContentType='application/json'
        )
        
    def _save_webhook(self, data):
        import requests
        response = requests.post(
            self.config['webhook_url'],
            json=data,
            headers={'Authorization': f"Bearer {self.config['webhook_token']}"}
        )
        response.raise_for_status()

# Usage in scraping script
persistence = DataPersistence(
    strategy=os.getenv('DATA_PERSISTENCE_STRATEGY', 'local'),
    config={
        'output_dir': './scraped_data',
        'bucket_name': os.getenv('S3_BUCKET_NAME'),
        'webhook_url': os.getenv('WEBHOOK_URL'),
        'webhook_token': os.getenv('WEBHOOK_AUTH_TOKEN')
    }
)

# Save scraped data
persistence.save(scraped_data, f"scrape_{timestamp}.json")
```

---

### 4. ✅ The "Crash" Check: Memory Allocation

**Why This Matters**: Chrome is a memory hog. UC Mode + CDP Mode + Xvfb (Virtual Display) consumes significant RAM. Insufficient memory causes crashes with misleading error messages.

**Required Action**: Ensure adequate memory allocation.

#### Minimum Memory Requirements

| Component | Memory Usage | Recommended Allocation |
|-----------|---------------|----------------------|
| Chrome (UC Mode) | 500MB - 1GB | 1GB |
| Xvfb (Virtual Display) | 100MB - 200MB | 256MB |
| Python Runtime | 100MB - 200MB | 256MB |
| SeleniumBase | 50MB - 100MB | 128MB |
| Data Processing | Variable | 256MB - 1GB |
| **Total Minimum** | **~1GB** | **2GB** |
| **Recommended** | **~2GB** | **4GB** |

#### Docker Memory Configuration

**Option A: Docker Run Command**
```bash
docker run --rm \
  --memory="4g" \
  --memory-swap="4g" \
  --shm-size=2g \
  stealth-scraper
```

**Option B: Docker Compose**
```yaml
services:
  stealthscrape:
    image: stealth-scraper:latest
    deploy:
      resources:
        limits:
          memory: 4G
        reservations:
          memory: 2G
    shm_size: 2gb
```

**Option C: Kubernetes**
```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: stealthscrape
    image: stealth-scraper:latest
    resources:
      requests:
        memory: "2Gi"
      limits:
        memory: "4Gi"
    volumeMounts:
    - mountPath: /dev/shm
      name: dshm
  volumes:
  - name: dshm
    emptyDir:
      medium: Memory
      sizeLimit: 2Gi
```

#### Shared Memory (`--shm-size`)

**Why It's Critical**: Chrome uses shared memory for IPC (Inter-Process Communication). Insufficient shared memory causes crashes.

**Common Error Messages**:
```
DevToolsActivePort file doesn't exist
Shared memory segments exhausted
Chrome failed to start: exited abnormally
```

**Solution**:
```bash
# Always use --shm-size with Chrome in Docker
docker run --shm-size=2g stealth-scraper
```

**Recommended Values**:
- **Minimum**: 1g (1GB)
- **Recommended**: 2g (2GB)
- **Heavy Workloads**: 4g (4GB)

#### Cloud Provider Recommendations

**AWS**:
- **EC2**: t3.large (2 vCPU, 8GB RAM) minimum
- **ECS**: Configure task memory to 4GB minimum
- **Lambda**: Not recommended (15-minute limit, memory constraints)

**Google Cloud**:
- **Compute Engine**: e2-medium (2 vCPU, 4GB RAM) minimum
- **Cloud Run**: Configure to 4GB memory
- **Kubernetes**: Set memory requests to 2GB, limits to 4GB

**Azure**:
- **Virtual Machines**: Standard D2s v3 (2 vCPU, 8GB RAM) minimum
- **Container Instances**: Configure to 4GB memory
- **Kubernetes**: Set memory requests to 2GB, limits to 4GB

#### Memory Monitoring

**Docker Stats**:
```bash
docker stats stealthscrape
```

**Inside Container**:
```python
import psutil

def check_memory():
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total / (1024**3):.2f} GB")
    print(f"Available: {mem.available / (1024**3):.2f} GB")
    print(f"Used: {mem.percent}%")
    
    # Alert if memory is low
    if mem.available < 500 * 1024 * 1024:  # Less than 500MB
        print("WARNING: Low memory available!")
```

---

### 5. ✅ Final Manual "Smoke Test"

**Why This Matters**: This is the ultimate test to verify the entire end-to-end flow works with real credentials, data persistence, and proper memory allocation.

**Required Action**: Run the following command to verify everything works.

#### Step-by-Step Smoke Test

**1. Create Test Output Directory**:
```bash
mkdir -p ./test_output
```

**2. Run Container with Production Settings**:
```bash
docker run --rm \
  --shm-size=2g \
  -v $(pwd)/test_output:/app/scraped_data \
  -e FB_USER="your_real_email@example.com" \
  -e FB_PASSWORD="your_real_password" \
  -e PROXY="user:pass@proxy.example.com:8080" \
  -e DATA_PERSISTENCE_STRATEGY="local" \
  stealth-scraper pytest tests/e2e/test_critical_paths.py::test_facebook_login_with_cdp -v
```

**3. Verify Output**:
```bash
# Check if test passed
ls -la ./test_output

# Verify data files exist
find ./test_output -name "*.json" -o -name "*.csv"
```

**4. Expected Results**:
- ✅ Test passes without errors
- ✅ Data files appear in `./test_output`
- ✅ No "DevToolsActivePort" errors
- ✅ No "Out of Memory" errors
- ✅ Proxy IP is used (check logs)

#### Alternative Smoke Test (API Mode)

If you want to test the full scraping flow:

```bash
# 1. Start the API server
docker run -d \
  --name stealthscrape-api \
  --shm-size=2g \
  -v $(pwd)/test_output:/app/scraped_data \
  -e FB_USER="your_real_email@example.com" \
  -e FB_PASSWORD="your_real_password" \
  -e PROXY="user:pass@proxy.example.com:8080" \
  -p 8000:8000 \
  stealth-scraper

# 2. Wait for server to start
sleep 10

# 3. Trigger a scrape
curl -X POST http://localhost:8000/api/scrape \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.facebook.com/profile",
    "platform": "facebook",
    "stealth_level": "maximum"
  }'

# 4. Check the output
ls -la ./test_output

# 5. Stop the container
docker stop stealthscrape-api
docker rm stealthscrape-api
```

#### Troubleshooting Common Issues

**Issue: "DevToolsActivePort file doesn't exist"**
```bash
# Solution: Increase shared memory
docker run --shm-size=4g stealth-scraper
```

**Issue: "Out of Memory"**
```bash
# Solution: Increase memory allocation
docker run --memory="4g" --shm-size=2g stealth-scraper
```

**Issue: "Connection Refused" (Proxy)**
```bash
# Solution: Verify proxy is working
curl -x user:pass@proxy.example.com:8080 https://httpbin.org/ip
```

**Issue: "Authentication Failed"**
```bash
# Solution: Verify credentials are correct
# Check GitHub Secrets or .env file
```

**Issue: "No Data Files Created"**
```bash
# Solution: Verify volume mount
docker run --rm -v $(pwd)/test_output:/app/scraped_data stealth-scraper ls -la /app/scraped_data
```

---

## 🚀 Production Deployment Scenarios

### Scenario 1: Local Development

**Setup**:
```bash
# Create environment file
cp .env.example .env

# Edit .env with your credentials
nano .env

# Run with volume mount
docker run --rm \
  --shm-size=2g \
  -v $(pwd)/scraped_data:/app/scraped_data \
  --env-file .env \
  stealth-scraper
```

### Scenario 2: AWS ECS Deployment

**Task Definition**:
```json
{
  "family": "stealthscrape",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "2048",
  "memory": "4096",
  "containerDefinitions": [
    {
      "name": "stealthscrape",
      "image": "stealthscrape:latest",
      "memory": 4096,
      "essential": true,
      "environment": [
        {
          "name": "UC_MODE",
          "value": "true"
        },
        {
          "name": "CDP_MODE",
          "value": "true"
        }
      ],
      "secrets": [
        {
          "name": "FB_USER",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:fb-user"
        },
        {
          "name": "FB_PASSWORD",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:fb-password"
        },
        {
          "name": "PROXY",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:proxy"
        }
      ],
      "mountPoints": [
        {
          "sourceVolume": "scraped-data",
          "containerPath": "/app/scraped_data"
        }
      ]
    }
  ],
  "volumes": [
    {
      "name": "scraped-data",
      "efsVolumeConfiguration": {
        "fileSystemId": "fs-12345678"
      }
    }
  ]
}
```

### Scenario 3: Kubernetes Deployment

**Deployment YAML**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: stealthscrape
spec:
  replicas: 1
  selector:
    matchLabels:
      app: stealthscrape
  template:
    metadata:
      labels:
        app: stealthscrape
    spec:
      containers:
      - name: stealthscrape
        image: stealthscrape:latest
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        env:
        - name: UC_MODE
          value: "true"
        - name: CDP_MODE
          value: "true"
        envFrom:
        - secretRef:
            name: stealthscrape-secrets
        volumeMounts:
        - name: dshm
          mountPath: /dev/shm
        - name: scraped-data
          mountPath: /app/scraped_data
      volumes:
      - name: dshm
        emptyDir:
          medium: Memory
          sizeLimit: 2Gi
      - name: scraped-data
        persistentVolumeClaim:
          claimName: scraped-data-pvc
```

**Secret YAML**:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: stealthscrape-secrets
type: Opaque
stringData:
  FB_USER: "your_email@example.com"
  FB_PASSWORD: "your_password"
  PROXY: "user:pass@proxy.example.com:8080"
```

### Scenario 4: Scheduled Scraping (Cron)

**Kubernetes CronJob**:
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: stealthscrape-cron
spec:
  schedule: "0 3 * * *"  # Run at 3 AM every day
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: stealthscrape
            image: stealthscrape:latest
            command: ["python", "src/main.py"]
            resources:
              requests:
                memory: "2Gi"
              limits:
                memory: "4Gi"
            envFrom:
            - secretRef:
                name: stealthscrape-secrets
          restartPolicy: OnFailure
```

**GitHub Actions Cron**:
```yaml
name: Scheduled Scraping

on:
  schedule:
    - cron: '0 3 * * *'  # Run at 3 AM UTC every day
  workflow_dispatch:  # Allow manual trigger

jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Run scraping
      run: |
        docker run --rm \
          --shm-size=2g \
          -e FB_USER="${{ secrets.FB_USER }}" \
          -e FB_PASSWORD="${{ secrets.FB_PASSWORD }}" \
          -e PROXY="${{ secrets.PROXY }}" \
          stealth-scraper python src/main.py
```

---

## 📊 Monitoring and Observability

### Health Checks

**Docker Health Check**:
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

**Kubernetes Liveness/Readiness Probes**:
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 40
  periodSeconds: 30
  timeoutSeconds: 10
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 20
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3
```

### Logging

**Structured Logging**:
```python
import logging
import json

class StructuredLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)
        
    def log(self, level, message, **kwargs):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': level,
            'message': message,
            **kwargs
        }
        self.logger.info(json.dumps(log_entry))

# Usage
logger = StructuredLogger('stealthscrape')
logger.log('INFO', 'Scraping started', url='https://example.com', platform='facebook')
```

### Metrics

**Prometheus Metrics**:
```python
from prometheus_client import Counter, Histogram, start_http_server

# Define metrics
scrape_counter = Counter('scrapes_total', 'Total scrapes', ['platform', 'status'])
scrape_duration = Histogram('scrape_duration_seconds', 'Scrape duration')

# Use in scraping code
@scrape_duration.time()
def scrape(url, platform):
    try:
        # ... scraping logic ...
        scrape_counter.labels(platform=platform, status='success').inc()
    except Exception as e:
        scrape_counter.labels(platform=platform, status='error').inc()
        raise

# Start metrics server
start_http_server(8001)
```

---

## 🔒 Security Considerations

### Credential Management

**Best Practices**:
- ✅ Use **AWS Secrets Manager** or **Azure Key Vault** for production
- ✅ Rotate credentials every 90 days
- ✅ Use **environment-specific secrets** (dev/staging/prod)
- ✅ Never commit credentials to version control
- ✅ Use **GitHub Environments** for different deployment stages

### Network Security

**Firewall Rules**:
```bash
# Only allow outbound traffic to necessary ports
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT  # HTTPS
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT   # HTTP
iptables -A OUTPUT -p tcp --dport 8080 -j ACCEPT # Proxy
iptables -A OUTPUT -j DROP                        # Block everything else
```

### Rate Limiting

**Implement Rate Limits**:
```python
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)
        
    def allow_request(self, key):
        now = time.time()
        requests = self.requests[key]
        
        # Remove old requests
        requests = [r for r in requests if now - r < self.time_window]
        self.requests[key] = requests
        
        if len(requests) < self.max_requests:
            requests.append(now)
            return True
        return False

# Usage
limiter = RateLimiter(max_requests=10, time_window=60)  # 10 requests per minute

if not limiter.allow_request('facebook'):
    print("Rate limit exceeded, waiting...")
    time.sleep(60)
```

---

## 🎯 Success Criteria

Your StealthScrape AI deployment is production-ready when:

- ✅ **Residential Proxies**: Configured and verified working
- ✅ **GitHub Secrets**: All required secrets configured
- ✅ **Data Persistence**: Working and tested (files appear in output directory)
- ✅ **Memory Allocation**: At least 2GB RAM with 2GB shared memory
- ✅ **Smoke Test**: End-to-end test passes with real credentials
- ✅ **Health Checks**: Container health endpoint responding
- ✅ **Monitoring**: Logging and metrics configured
- ✅ **Security**: Credentials managed securely
- ✅ **Rate Limiting**: Implemented to prevent blocking
- ✅ **Error Handling**: Graceful degradation on failures

---

## 📞 Support and Troubleshooting

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|--------|----------|
| DevToolsActivePort error | Insufficient shared memory | Increase `--shm-size` to 2g or 4g |
| Out of Memory error | Insufficient RAM | Increase `--memory` to 4g or 8g |
| Connection Refused | Proxy not working | Verify proxy with `curl -x proxy:port https://httpbin.org/ip` |
| Authentication Failed | Wrong credentials | Verify GitHub Secrets or .env file |
| No data files | Volume mount issue | Verify volume mount path with `docker inspect` |
| Chrome crashes | Memory leak | Restart container periodically, increase memory |

### Getting Help

- **Documentation**: Check [`README.md`](README.md:1) for basic usage
- **Proxy Guide**: See [`PROXY_INTEGRATION.md`](PROXY_INTEGRATION.md:1) for proxy configuration
- **Docker Guide**: See [`DOCKER_DEPLOYMENT.md`](DOCKER_DEPLOYMENT.md:1) for Docker deployment
- **GitHub Issues**: Report bugs at https://github.com/djamfikr7/stealthscrape-ai/issues

---

**You are now ready to deploy StealthScrape AI to production!** 🚀
