# StealthScrape AI

Advanced web scraping platform powered by **SeleniumBase UC Mode** and **Chrome DevTools Protocol (CDP)** for undetectable automation.

## 🚀 Overview

StealthScrape AI is a production-ready web scraping engine that bypasses sophisticated bot detection systems using:
- **UC Mode (Undetected Chrome)**: Mimics real browser behavior to avoid detection
- **CDP Mode (Chrome DevTools Protocol)**: Advanced stealth interactions for anti-bot protection
- **Smart Waits**: Eliminates flaky tests with automatic element waiting
- **Proxy Rotation**: IP rotation to prevent blocking and enable large-scale operations
- **Docker Support**: Containerized deployment with virtual display (Xvfb) for headless environments

## ✨ Features

### Core Capabilities
- 🤖 **Multi-Platform Support**: Facebook, Instagram, Twitter/X, TikTok, Generic scraping
- 🛡 **Anti-Bot Protection**: Bypasses Cloudflare, CAPTCHA, and detection systems
- 🔄 **Proxy Rotation**: Automatic IP rotation with residential proxy support
- 📊 **Dashboard Analytics**: Real-time monitoring and performance metrics
- 🧪 **Session Management**: Persistent sessions with automatic cleanup
- 🎯 **Smart Targeting**: Platform-specific scraping strategies

### Technical Features
- ✅ **No Raw Selenium**: 100% SeleniumBase patterns (SB context manager or BaseCase)
- ✅ **No time.sleep()**: Smart waits with `sb.sleep()` for human-like delays
- ✅ **UC Mode Enabled**: Undetected Chrome for maximum stealth
- ✅ **CDP Mode**: Advanced Chrome DevTools Protocol integration
- ✅ **Virtual Display**: Xvfb support for headless CI/CD environments
- ✅ **Proxy Support**: Format `user:pass@ip:port` with CDP mode compatibility
- ✅ **Health Checks**: Container health monitoring and automatic recovery

## 📋 Requirements

### System Requirements
- **Python**: 3.10 or higher
- **Chrome**: Google Chrome Stable (automatically installed)
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Disk**: 10GB free space

### Python Dependencies
All dependencies are managed via [`requirements.txt`](requirements.txt):
- `seleniumbase==4.45.8` - Core automation framework
- `fastapi==0.104.1` - REST API server
- `uvicorn[standard]==0.24.0` - ASGI server
- `pytest==8.4.2` - Test runner with SeleniumBase plugin
- `psutil==5.9.6` - System monitoring
- `pandas==2.1.3` - Data processing
- `aiohttp==3.9.1` - Async HTTP client

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd selinium

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install ChromeDriver (required for UC Mode)
seleniumbase install chromedriver
```

### 2. Configuration

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# Application Settings
STEALTHSCRAPE_ENV=development
PORT=8000
HOST=0.0.0.0

# Stealth Configuration
STEALTH_LEVEL=maximum
USE_RESIDENTIAL_PROXIES=true
CDP_MODE=true
UC_MODE=true

# Test Credentials (Optional - for E2E tests)
FB_USER=your_facebook_email@example.com
FB_PASSWORD=your_facebook_password
IG_USER=your_instagram_username
IG_PASSWORD=your_instagram_password
TW_USER=your_twitter_username
TW_PASSWORD=your_twitter_password
AMAZON_EMAIL=your_amazon_email@example.com
AMAZON_PASSWORD=your_amazon_password
SHOPIFY_STORE=your-store.myshopify.com
SHOPIFY_EMAIL=your_shopify_email@example.com
SHOPIFY_PASSWORD=your_shopify_password

# Proxy Configuration (Optional)
PROXY=user:pass@proxy.example.com:8080
PROXY_ROTATION_INTERVAL=300
PROXY_POOL_SIZE=10
```

### 3. Run Tests

```bash
# Run unit tests
pytest tests/unit/ -v

# Run integration tests
pytest tests/integration/ -v

# Run E2E tests (requires credentials)
pytest tests/e2e/ -v

# Run with dashboard (generates HTML report)
pytest tests/ --dashboard --html=reports/report.html
```

### 4. Run Application

```bash
# Start the API server
uvicorn src.backend.api:app --host 0.0.0.0 --port 8000

# Or use the stealth scrape engine directly
python -c "from src.backend.stealth_scrape_engine import StealthScrapeEngine; engine = StealthScrapeEngine(); print('Engine initialized')"
```

## 🐳 Docker Deployment

### Build Docker Image

```bash
# Build the image
docker build -t stealthscrape:latest .
```

### Run Container

```bash
# Run standalone container
docker run -d -p 8000:8000 \
  -e STEALTHSCRAPE_ENV=production \
  -e UC_MODE=true \
  -e CDP_MODE=true \
  stealthscrape:latest

# Run with docker-compose
docker-compose up -d

# Check container health
curl http://localhost:8000/health
```

### Docker Features

- **Base Image**: `python:3.10-slim-bullseye` for Chrome compatibility
- **Virtual Display**: Xvfb provides 1920x1080x24 display for UC Mode
- **Chrome Stable**: Latest Google Chrome with all dependencies
- **Health Checks**: Automatic monitoring with 30s interval
- **Entry Point**: Custom script for proper xvfb-run integration
- **Volume Mounts**: Persistent data and log storage

### Docker Compose Services

The [`docker-compose.yml`](docker-compose.yml) includes:
- **stealthscrape-app**: Main application with UC Mode
- **redis**: Session management and caching
- **postgres**: Data persistence
- **prometheus**: Metrics collection
- **grafana**: Visualization dashboard

## 🔄 CI/CD Pipeline

### GitHub Actions

The [`github/workflows/selenium_test.yml`](github/workflows/selenium_test.yml) pipeline provides:

1. **Automated Testing**
   - Runs on every push and pull request
   - Installs system dependencies (xvfb, Chrome)
   - Runs unit, integration, and E2E tests
   - Uses `xvfb-run` for UC Mode support in CI

2. **Test Execution**
   ```yaml
   # Unit tests with xvfb-run
   xvfb-run -a --server-args="-screen 0 1920x1080x24" pytest tests/unit/ -v
   
   # Integration tests with xvfb-run
   xvfb-run -a --server-args="-screen 0 1920x1080x24" pytest tests/integration/ -v
   
   # E2E tests (conditional on credentials)
   xvfb-run -a --server-args="-screen 0 1920x1080x24" pytest tests/e2e/ -v
   ```

3. **Dashboard Reports**
   - Generates HTML reports with `--dashboard --html=reports/report.html`
   - Uploads test artifacts
   - Comments PRs with test results

4. **Docker Build & Test**
   - Builds Docker image
   - Runs tests inside container
   - Verifies health endpoint
   - Pushes to Docker Hub on main branch

5. **Security Scanning**
   - Runs Bandit security analysis
   - Uploads security reports as artifacts

### Required GitHub Secrets

Configure these in your repository settings:

```yaml
# Test Credentials
FB_USER, FB_PASSWORD
IG_USER, IG_PASSWORD
TW_USER, TW_PASSWORD
AMAZON_EMAIL, AMAZON_PASSWORD
SHOPIFY_STORE, SHOPIFY_EMAIL, SHOPIFY_PASSWORD

# Docker Hub
DOCKER_USERNAME, DOCKER_PASSWORD

# GitHub Token (for PR commenting)
GITHUB_TOKEN
```

## 🌐 API Usage

### Start Scraping Session

```python
import requests

# Start Facebook scraping
response = requests.post('http://localhost:8000/api/scrape', json={
    'url': 'https://www.facebook.com/profile',
    'platform': 'facebook',
    'stealth_level': 'maximum',
    'proxy': 'user:pass@proxy.example.com:8080'
})

session_id = response.json()['session_id']
print(f"Session started: {session_id}")
```

### Check Session Status

```python
response = requests.get(f'http://localhost:8000/api/session/{session_id}')
status = response.json()
print(f"Status: {status['status']}, Progress: {status['progress']}%")
```

### Get Session Results

```python
response = requests.get(f'http://localhost:8000/api/results/{session_id}')
results = response.json()
print(f"Scraped data: {results}")
```

### Stop Session

```python
requests.post(f'http://localhost:8000/api/session/{session_id}/stop')
```

### Platform-Specific Endpoints

```python
# Instagram scraping
requests.post('http://localhost:8000/api/scrape/instagram', json={
    'url': 'https://www.instagram.com/profile',
    'include_stories': True,
    'max_posts': 12
})

# Twitter scraping
requests.post('http://localhost:8000/api/scrape/twitter', json={
    'url': 'https://twitter.com/profile',
    'include_tweets': True,
    'max_tweets': 10
})
```

## 🔄 Proxy Integration

### Proxy Format

StealthScrape supports standard proxy format: `user:pass@ip:port`

```bash
# HTTP Proxy
HTTP_PROXY=http://username:password@proxy.example.com:8080

# HTTPS Proxy
HTTPS_PROXY=https://username:password@proxy.example.com:8443

# SOCKS5 Proxy
SOCKS5_PROXY=socks5://username:password@proxy.example.com:1080

# Multiple Proxies (for rotation)
PROXY_LIST=user:pass@192.168.1.100:8080,user:pass@192.168.1.101:8080
```

### Configuration

```env
# Single Proxy
PROXY=user:pass@proxy.example.com:8080

# Proxy Rotation
PROXY_ROTATION_INTERVAL=300  # Rotate every 5 minutes
PROXY_POOL_SIZE=10             # Number of proxies in pool
```

### Engine Configuration

```python
config = {
    'use_residential_proxies': True,
    'proxy_rotation_interval': 300,
    'proxy_pool_size': 10
}

engine = StealthScrapeEngine(config)
```

### CDP Mode Proxy Handling

When using CDP mode, proxy is automatically applied:

```python
# CDP mode handles proxy automatically
session_id = engine.create_session(
    "https://example.com/profile",
    options={
        'proxy': 'user:pass@proxy.example.com:8080',
        'cdp_mode': True
    }
)
```

**Important**: Proxy must be set before `activate_cdp_mode()` is called.

### Proxy Rotation Strategies

See [`PROXY_INTEGRATION.md`](PROXY_INTEGRATION.md) for comprehensive proxy management:
- Time-based rotation
- Request-based rotation
- Error-based rotation
- Health monitoring
- Best practices for social media platforms

## 📊 Dashboard & Monitoring

### Dashboard Endpoint

```bash
curl http://localhost:8000/api/dashboard
```

Returns:
```json
{
  "active_sessions": 3,
  "total_sessions": 150,
  "success_rate": 98.5,
  "total_items_scraped": 1250,
  "system_status": {
    "cpu_usage": 45.2,
    "memory_usage": 62.8,
    "network_bandwidth": 125.5,
    "disk_usage": 55.3,
    "active_connections": 8,
    "total_memory": "16.0 GB",
    "available_memory": "6.2 GB",
    "cpu_cores": 8,
    "hostname": "scrape-server-01",
    "platform": "Linux-5.15.0-107-generic",
    "python_version": "3.10.12"
  }
}
```

### Health Check

```bash
curl http://localhost:8000/health
```

Returns:
```json
{
  "status": "healthy",
  "active_sessions": 3
}
```

## 🧪 Testing

### Test Structure

```
tests/
├── unit/                    # Unit tests for engine components
│   └── test_stealth_scrape_engine.py
├── integration/             # Integration tests for platforms
│   └── test_facebook_scraper.py
└── e2e/                     # End-to-end critical path tests
    ├── test_critical_paths.py      # Login, Checkout flows
    └── test_critical_paths_cdp.py # CDP Mode tests
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/unit/test_stealth_scrape_engine.py -v

# Run with dashboard
pytest tests/ --dashboard --html=reports/report.html

# Run with coverage
pytest tests/ --cov=src/backend --cov-report=html

# Run specific markers
pytest tests/ -m "not requires_auth"  # Skip tests requiring credentials
pytest tests/ -m "requires_auth"  # Only run tests with credentials
```

### Test Markers

- `unit`: Unit tests
- `integration`: Integration tests
- `e2e`: End-to-end tests
- `requires_auth`: Tests requiring credentials
- `requires_proxy`: Tests requiring proxy configuration
- `slow`: Slow-running tests

## 🛡 Security & Anti-Bot

### Stealth Levels

1. **Basic**: Standard SeleniumBase smart waits
2. **Advanced**: Adds user agent rotation and proxy support
3. **Maximum**: Full UC Mode with CDP and anti-bot bypass

### Anti-Bot Features

- **WebDriver Property Removal**: Hides automation indicators
- **Hardware Concurrency Mocking**: Simulates real browser
- **Device Memory Simulation**: Mimics actual hardware
- **Chrome DevTools Variables**: Removes automation detection
- **CAPTCHA Bypass**: UC Mode automatic CAPTCHA solving
- **Cloudflare Bypass**: CDP mode for advanced challenges
- **Rate Limiting**: Smart delays and rotation

### Best Practices

1. **Use Residential Proxies**: For social media platforms
2. **Rotate User Agents**: Mimic different browsers
3. **Human-Like Delays**: Random timing between actions
4. **Mouse Movement**: Natural cursor behavior
5. **Scroll Patterns**: Realistic scrolling
6. **Session Persistence**: Reuse sessions when possible

## 🐛 Troubleshooting

### Common Issues

#### Issue: Chrome Not Found

**Symptoms**: `chrome not found` error

**Solutions**:
```bash
# Install ChromeDriver
seleniumbase install chromedriver

# Or install Google Chrome manually
sudo apt-get install google-chrome-stable
```

#### Issue: Headless Chrome Errors

**Symptoms**: `DevToolsActivePort file doesn't exist` or `HeadlessChrome` error

**Solutions**:
```bash
# Use xvfb-run for virtual display
xvfb-run -a --server-args="-screen 0 1920x1080x24" pytest tests/

# Or set headed mode
export SELENIUM_HEADLESS=false
```

#### Issue: Proxy Not Working

**Symptoms**: Requests still use original IP

**Solutions**:
1. Verify proxy format: `user:pass@ip:port`
2. Test proxy manually:
   ```bash
   curl -x user:pass@proxy.com:8080 https://httpbin.org/ip
   ```
3. Check proxy credentials
4. Try different proxy type (HTTP vs SOCKS5)

#### Issue: 403 Forbidden / CAPTCHA

**Symptoms**: Access denied or CAPTCHA challenges

**Solutions**:
1. Enable UC Mode: `UC_MODE=true`
2. Enable CDP Mode: `CDP_MODE=true`
3. Use residential proxies
4. Increase stealth level: `STEALTH_LEVEL=maximum`
5. Rotate proxies more frequently
6. Add delays between requests

#### Issue: Tests Failing in CI

**Symptoms**: Tests pass locally but fail in GitHub Actions

**Solutions**:
1. Ensure xvfb-run is used in CI
2. Check ChromeDriver installation
3. Verify environment variables
4. Check test timeouts
5. Review CI logs for specific errors

## 📚 Documentation

- [`spec.md`](spec.md) - Project specification and requirements
- [`PROXY_INTEGRATION.md`](PROXY_INTEGRATION.md) - Comprehensive proxy integration guide
- [`DOCKER_DEPLOYMENT.md`](DOCKER_DEPLOYMENT.md) - Docker deployment guide
- [`.env.example`](.env.example) - Environment variable template

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `pytest tests/ -v`
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Create a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- **SeleniumBase**: For the excellent automation framework
- **Undetected Chrome**: For UC Mode implementation
- **Chrome DevTools Protocol**: For advanced browser control
- **pytest**: For the powerful testing framework

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Built with ❤️ using SeleniumBase UC Mode & CDP Mode**
