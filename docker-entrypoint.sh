#!/bin/bash
set -e

echo "Starting StealthScrape API with Xvfb..."
echo "DISPLAY: $DISPLAY"
echo "UC_MODE: $UC_MODE"
echo "CDP_MODE: $CDP_MODE"

# Start the application with xvfb-run
exec xvfb-run -a --server-args="-screen 0 1920x1080x24" \
    uvicorn src.backend.api:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 1
