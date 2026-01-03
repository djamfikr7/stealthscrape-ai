# Proxy Integration Guide for StealthScrape

## Overview

This guide explains how to configure and use proxies with StealthScrape to prevent IP burnout and enable large-scale scraping operations.

## Proxy Format

StealthScrape supports the standard proxy format: `user:pass@ip:port`

### Examples

```bash
# HTTP Proxy
HTTP_PROXY=http://username:password@proxy.example.com:8080

# HTTPS Proxy
HTTPS_PROXY=https://username:password@proxy.example.com:8443

# SOCKS5 Proxy
SOCKS5_PROXY=socks5://username:password@proxy.example.com:1080

# Multiple Proxies (for rotation)
PROXY_LIST=user:pass@192.168.1.100:8080,user:pass@192.168.1.101:8080,user:pass@192.168.1.102:8080
```

## Configuration Options

### 1. Environment Variables

Set proxy configuration in your `.env` file:

```env
# Single Proxy
PROXY=user:pass@proxy.example.com:8080

# Or use HTTP/HTTPS specific
HTTP_PROXY=http://user:pass@proxy.example.com:8080
HTTPS_PROXY=https://user:pass@proxy.example.com:8443

# Proxy Rotation Configuration
PROXY_ROTATION_INTERVAL=300  # Rotate every 5 minutes
PROXY_POOL_SIZE=10             # Number of proxies in pool
```

### 2. API Configuration

Pass proxy when creating a scraping session:

```python
from stealth_scrape_engine import StealthScrapeEngine

engine = StealthScrapeEngine()

# Create session with proxy
session_id = engine.create_session(
    "https://example.com/profile",
    options={
        'proxy': 'user:pass@proxy.example.com:8080'
    }
)
```

### 3. Engine Configuration

Configure proxy rotation in engine initialization:

```python
config = {
    'use_residential_proxies': True,
    'proxy_rotation_interval': 300,
    'proxy_pool_size': 10
}

engine = StealthScrapeEngine(config)
```

## Proxy Types

### Residential Proxies

**Best for:** Social media platforms (Facebook, Instagram, Twitter)

- **Pros:** Legitimate IP ranges, harder to block
- **Cons:** More expensive, slower speeds
- **Recommended Providers:**
  - Bright Data
  - Smartproxy
  - Oxylabs

### Datacenter Proxies

**Best for:** General web scraping, e-commerce sites

- **Pros:** Fast, inexpensive, high bandwidth
- **Cons:** Easily detected and blocked
- **Recommended Providers:**
  - Luminati
  - Storm Proxies
  - Blazing SEO

### Mobile Proxies

**Best for:** Mobile-first platforms (TikTok, Instagram)

- **Pros:** Appear as mobile device, high trust
- **Cons:** Very expensive, limited availability
- **Recommended Providers:**
  - ProxyEmpire
  - IPRoyal
  - Smartproxy

## CDP Mode Proxy Handling

When using CDP (Chrome DevTools Protocol) mode, proxy configuration is handled differently:

### Standard Mode
```python
with SB(proxy="user:pass@proxy.com:8080") as sb:
    sb.open("https://example.com")
```

### CDP Mode
```python
with SB(proxy="user:pass@proxy.com:8080") as sb:
    sb.activate_cdp_mode("https://example.com")
    # Proxy is automatically applied to CDP session
```

**Important Notes:**
1. Proxy must be set **before** `activate_cdp_mode()` is called
2. CDP mode uses the same proxy format as standard mode
3. Proxy authentication is handled by SeleniumBase internally

## Proxy Rotation Strategies

### 1. Time-Based Rotation

Rotate proxies at fixed intervals:

```python
config = {
    'proxy_rotation_interval': 300,  # Every 5 minutes
    'use_residential_proxies': True
}
```

### 2. Request-Based Rotation

Rotate after a certain number of requests:

```python
def scrape_with_rotation(engine, url, max_requests_per_proxy=50):
    session_id = engine.create_session(url)
    
    for i in range(max_requests_per_proxy):
        result = engine.scrape_facebook(session_id, url)
        
        # Rotate proxy after N requests
        if i > 0 and i % max_requests_per_proxy == 0:
            engine.close_session(session_id)
            session_id = engine.create_session(url)
    
    return result
```

### 3. Error-Based Rotation

Rotate on detection/blocking:

```python
def scrape_with_fallback(engine, url):
    session_id = engine.create_session(url)
    
    try:
        result = engine.scrape_facebook(session_id, url)
        return result
    except Exception as e:
        if "blocked" in str(e).lower() or "403" in str(e):
            # Close session and create new one with different proxy
            engine.close_session(session_id)
            session_id = engine.create_session(url)
            return engine.scrape_facebook(session_id, url)
```

## Best Practices

### 1. Use Residential Proxies for Social Media

```python
config = {
    'use_residential_proxies': True,
    'stealth_level': 'maximum'
}
```

### 2. Implement Exponential Backoff

```python
import time

def scrape_with_retry(engine, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            session_id = engine.create_session(url)
            result = engine.scrape_facebook(session_id, url)
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 2, 4, 8 seconds
                time.sleep(wait_time)
            else:
                raise
```

### 3. Monitor Proxy Health

```python
def check_proxy_health(proxy):
    try:
        session = requests.Session()
        session.proxies = {
            'http': proxy,
            'https': proxy
        }
        response = session.get('https://httpbin.org/ip', timeout=10)
        return response.status_code == 200
    except:
        return False
```

### 4. Limit Concurrent Connections

```python
config = {
    'max_threads': 5,  # Limit concurrent sessions
    'proxy_pool_size': 10  # More proxies than threads
}
```

## Troubleshooting

### Issue: Proxy Not Working

**Symptoms:** Requests still use original IP

**Solutions:**
1. Verify proxy format: `user:pass@ip:port`
2. Check proxy credentials
3. Test proxy manually:
   ```bash
   curl -x user:pass@proxy.com:8080 https://httpbin.org/ip
   ```

### Issue: Proxy Blocked

**Symptoms:** 403 Forbidden or CAPTCHA

**Solutions:**
1. Switch to residential proxies
2. Increase rotation interval
3. Use mobile proxies for mobile platforms
4. Add user agent rotation

### Issue: Slow Performance

**Symptoms:** Requests taking too long

**Solutions:**
1. Test proxy speed:
   ```bash
   curl -o /dev/null -s -w '%{time_total}\n' -x user:pass@proxy.com:8080 https://example.com
   ```
2. Switch to datacenter proxies for speed
3. Use geographically closer proxies

### Issue: CDP Mode Not Using Proxy

**Symptoms:** CDP mode bypasses proxy settings

**Solutions:**
1. Ensure proxy is set before `activate_cdp_mode()`
2. Check proxy format is correct
3. Verify proxy authentication works

## Security Considerations

### 1. Never Commit Credentials

```bash
# Add to .gitignore
.env
proxies.txt
```

### 2. Use Environment Variables

```python
import os

proxy = os.getenv('PROXY')
if not proxy:
    raise ValueError("PROXY environment variable not set")
```

### 3. Rotate Credentials

Change proxy credentials regularly to prevent account association:

```python
def rotate_proxy_credentials():
    # Implement logic to cycle through different credentials
    pass
```

## Monitoring and Analytics

### Track Proxy Performance

```python
class ProxyMonitor:
    def __init__(self):
        self.proxy_stats = {}
    
    def record_request(self, proxy, success, response_time):
        if proxy not in self.proxy_stats:
            self.proxy_stats[proxy] = {
                'success_count': 0,
                'failure_count': 0,
                'total_time': 0
            }
        
        if success:
            self.proxy_stats[proxy]['success_count'] += 1
            self.proxy_stats[proxy]['total_time'] += response_time
        else:
            self.proxy_stats[proxy]['failure_count'] += 1
    
    def get_best_proxy(self):
        best_proxy = None
        best_avg_time = float('inf')
        
        for proxy, stats in self.proxy_stats.items():
            if stats['success_count'] > 0:
                avg_time = stats['total_time'] / stats['success_count']
                if avg_time < best_avg_time:
                    best_avg_time = avg_time
                    best_proxy = proxy
        
        return best_proxy
```

## Example Usage

### Complete Example with Proxy

```python
from stealth_scrape_engine import StealthScrapeEngine
import os

# Initialize engine with proxy support
config = {
    'use_residential_proxies': True,
    'proxy_rotation_interval': 300,
    'stealth_level': 'maximum',
    'uc_mode': True,
    'cdp_mode': True
}

engine = StealthScrapeEngine(config)

# Create session with proxy
proxy = os.getenv('PROXY', 'user:pass@proxy.example.com:8080')
session_id = engine.create_session(
    "https://www.facebook.com/profile",
    options={
        'proxy': proxy,
        'cdp_mode': True
    }
)

# Scrape with proxy
result = engine.scrape_facebook(session_id, "https://www.facebook.com/profile")

# Clean up
engine.close_session(session_id)
```

## Docker Deployment with Proxies

### Environment Variables in Docker

```yaml
# docker-compose.yml
services:
  stealthscrape-app:
    environment:
      - PROXY=user:pass@proxy.example.com:8080
      - PROXY_ROTATION_INTERVAL=300
      - USE_RESIDENTIAL_PROXIES=true
```

### Docker Build Arguments

```dockerfile
# Dockerfile
ARG PROXY
ENV PROXY=${PROXY}
```

## Conclusion

Proper proxy integration is critical for:
1. **Preventing IP Burnout**: Rotate IPs to avoid blocking
2. **Scaling Operations**: Run multiple concurrent sessions
3. **Bypassing Geo-restrictions**: Access region-specific content
4. **Maintaining Stealth**: Appear as legitimate traffic

Always test proxy configurations in a controlled environment before deploying to production.
