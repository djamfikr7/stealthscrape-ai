# SeleniumBase UC Mode Optimized Dockerfile
# Base image: python:3.10-slim-bullseye for Chrome compatibility and active repositories
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies for Chrome and SeleniumBase UC Mode
RUN apt-get update && \
    apt-get install -y \
    # X11 virtual display (required for UC Mode to bypass bot detection)
    xvfb \
    # Chrome dependencies
    wget \
    gnupg \
    curl \
    libgbm-dev \
    libxshmfence-dev \
    fonts-noto-color-emoji \
    ffmpeg \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    # Additional libraries for Chrome
    libxss1 \
    libappindicator3-1 \
    fonts-liberation \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome Stable
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Verify Chrome installation
RUN google-chrome --version

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Create necessary directories
RUN mkdir -p scraped_data logs

# Set environment variables for SeleniumBase UC Mode
ENV PYTHONUNBUFFERED=1
ENV STEALTHSCRAPE_ENV=production
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV DISPLAY=:99
ENV SELENIUM_HEADLESS=false
ENV UC_MODE=true
ENV CDP_MODE=true

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Start the application with xvfb-run for virtual display support
# xvfb-run provides a virtual X11 display so UC Mode thinks it has a GUI
# This is crucial for bypassing sophisticated bot detection
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
