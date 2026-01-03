"""
StealthScrape API Server
FastAPI-based REST API for the web scraping platform
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
import uvicorn
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from stealth_scrape_engine import StealthScrapeEngine

app = FastAPI(
    title="StealthScrape API",
    description="Advanced web scraping API with undetectable automation capabilities",
    version="1.0.0"
)

# Mount static files directory
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../frontend")), name="static")

# Initialize the scraping engine
engine = StealthScrapeEngine()


class ScrapeRequest(BaseModel):
    url: str
    platform: str  # 'facebook', 'tiktok', 'instagram', 'twitter', 'generic'
    options: Optional[Dict[str, Any]] = None
    proxy: Optional[str] = None
    stealth_level: str = "maximum"

class ScrapeInstagramRequest(BaseModel):
    url: str
    options: Optional[Dict[str, Any]] = None
    proxy: Optional[str] = None
    stealth_level: str = "maximum"
    include_stories: bool = False
    max_posts: int = 12

class ScrapeTwitterRequest(BaseModel):
    url: str
    options: Optional[Dict[str, Any]] = None
    proxy: Optional[str] = None
    stealth_level: str = "maximum"
    include_tweets: bool = True
    max_tweets: int = 10


class SessionStatus(BaseModel):
    session_id: str
    status: str
    progress: int
    items_scraped: int
    errors: List[str]


@app.get("/")
async def root():
    """Serve the frontend application"""
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    return FileResponse(frontend_path)

@app.get("/api")
async def api_info():
    """API information endpoint"""
    return {
        "name": "StealthScrape API",
        "version": "1.0.0",
        "description": "Advanced web scraping API with undetectable automation capabilities",
        "endpoints": {
            "scrape": "/api/scrape",
            "session_status": "/api/session/{session_id}",
            "dashboard": "/api/dashboard",
            "results": "/api/results/{session_id}",
            "stop_session": "/api/session/{session_id}/stop"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "active_sessions": engine.active_sessions
    }


@app.post("/api/scrape", response_model=Dict[str, Any])
async def start_scraping(request: ScrapeRequest, background_tasks: BackgroundTasks):
    """Start a new scraping session"""
    try:
        # Create session with platform-specific options
        options = request.options or {}
        options.update({
            'platform': request.platform,
            'stealth_level': request.stealth_level,
            'proxy': request.proxy
        })
        
        session_id = engine.create_session(request.url, options)
        
        # Return immediate response with session ID
        return {
            "session_id": session_id,
            "status": "starting",
            "message": "Scraping session started successfully",
            "estimated_time": "30-120 seconds"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start scraping session: {str(e)}")

@app.post("/api/scrape/instagram", response_model=Dict[str, Any])
async def scrape_instagram(request: ScrapeInstagramRequest, background_tasks: BackgroundTasks):
    """Scrape Instagram profile with advanced options"""
    try:
        options = request.options or {}
        options.update({
            'platform': 'instagram',
            'stealth_level': request.stealth_level,
            'proxy': request.proxy,
            'include_stories': request.include_stories,
            'max_posts': request.max_posts
        })
        
        session_id = engine.create_session(request.url, options)
        
        return {
            "session_id": session_id,
            "status": "starting",
            "message": "Instagram scraping session started successfully",
            "platform": "instagram",
            "estimated_time": "45-180 seconds"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start Instagram scraping: {str(e)}")

@app.post("/api/scrape/twitter", response_model=Dict[str, Any])
async def scrape_twitter(request: ScrapeTwitterRequest, background_tasks: BackgroundTasks):
    """Scrape Twitter/X profile with advanced options"""
    try:
        options = request.options or {}
        options.update({
            'platform': 'twitter',
            'stealth_level': request.stealth_level,
            'proxy': request.proxy,
            'include_tweets': request.include_tweets,
            'max_tweets': request.max_tweets
        })
        
        session_id = engine.create_session(request.url, options)
        
        return {
            "session_id": session_id,
            "status": "starting",
            "message": "Twitter scraping session started successfully",
            "platform": "twitter",
            "estimated_time": "30-120 seconds"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start Twitter scraping: {str(e)}")


@app.get("/api/session/{session_id}", response_model=SessionStatus)
async def get_session_status(session_id: str):
    """Get the status of a scraping session"""
    status = engine.get_session_status(session_id)
    
    if "error" in status:
        raise HTTPException(status_code=404, detail=status["error"])
    
    return SessionStatus(
        session_id=session_id,
        status=status["status"],
        progress=status["progress"],
        items_scraped=status["items_scraped"],
        errors=status["errors"]
    )


@app.get("/api/dashboard")
async def get_dashboard():
    """Get dashboard statistics"""
    return engine.get_dashboard_stats()


@app.get("/api/results/{session_id}")
async def get_session_results(session_id: str):
    """Get the results of a completed scraping session"""
    # In a real implementation, this would retrieve stored results
    # For now, we'll simulate a response
    session = engine.get_session_status(session_id)
    
    if "error" in session:
        raise HTTPException(status_code=404, detail=session["error"])
    
    if session["status"] not in ["completed", "ready"]:
        raise HTTPException(status_code=400, detail="Session not completed yet")
    
    # Simulate returning scraped data
    return {
        "session_id": session_id,
        "data": {
            "profiles": [
                {
                    "name": "Sample User",
                    "followers": 15420,
                    "engagement_rate": 3.2,
                    "post_count": 87,
                    "content_types": ["image", "video", "text"]
                }
            ],
            "metadata": {
                "scraped_at": session["created_at"],
                "platform": session["options"].get("platform", "unknown"),
                "items_count": session["items_scraped"]
            }
        }
    }


@app.post("/api/session/{session_id}/stop")
async def stop_session(session_id: str):
    """Stop an active scraping session"""
    try:
        engine.close_session(session_id)
        return {"message": "Session stopped successfully", "session_id": session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to stop session: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
