"""
Integration tests for Facebook scraping functionality using SeleniumBase
"""

import pytest
import random
import string
from unittest.mock import MagicMock, patch

try:
    from seleniumbase import SB
    from seleniumbase import BaseCase
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False


class TestFacebookScraperWithSB(BaseCase):
    """Integration tests for Facebook scraping using SeleniumBase BaseCase"""
    
    def test_facebook_session_creation_with_sb(self):
        """Test creating a Facebook scraping session using SB context manager"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to Facebook
            sb.open("https://www.facebook.com")
            
            # Verify page loaded
            sb.assert_element('input[name="email"]', timeout=10)
            sb.assert_element('input[name="pass"]', timeout=10)
            
            # Check URL
            assert "facebook.com" in sb.get_current_url()
    
    def test_facebook_login_with_uc_mode(self):
        """Test Facebook login with UC Mode for anti-bot protection"""
        with self.uc_mode():
            # Navigate to Facebook
            self.open("https://www.facebook.com")
            
            # Wait for login form
            self.assert_element('input[name="email"]', timeout=10)
            self.assert_element('input[name="pass"]', timeout=10)
            
            # Enter test credentials
            self.type('input[name="email"]', "test@example.com")
            self.type('input[name="pass"]', "testpassword123")
            
            # Click login button
            self.click('button[name="login"]')
            
            # Verify login attempt
            self.sleep(2)
    
    def test_facebook_profile_scraping(self):
        """Test scraping Facebook profile data"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to a public profile
            sb.open("https://www.facebook.com/facebookapp")
            
            # Wait for profile to load
            sb.assert_element('h1', timeout=15)
            
            # Extract profile name
            profile_name = sb.get_text('h1')
            assert profile_name is not None
            assert len(profile_name) > 0
            
            # Check for bio section
            if sb.is_element_visible('div[data-pagelet="ProfileTimeline"]'):
                bio_text = sb.get_text('div[data-pagelet="ProfileTimeline"]')
                assert bio_text is not None


class TestTikTokScraperWithSB(BaseCase):
    """Integration tests for TikTok scraping using SeleniumBase"""
    
    def test_tiktok_session_creation_with_sb(self):
        """Test creating a TikTok scraping session using SB context manager"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to TikTok
            sb.open("https://www.tiktok.com")
            
            # Verify page loaded
            sb.assert_element('body', timeout=15)
            
            # Check URL
            assert "tiktok.com" in sb.get_current_url()
    
    def test_tiktok_profile_scraping(self):
        """Test scraping TikTok profile data"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to a public profile
            sb.open("https://www.tiktok.com/@tiktok")
            
            # Wait for profile to load
            sb.assert_element('h1', timeout=15)
            
            # Extract username
            username = sb.get_text('h1')
            assert username is not None
            assert len(username) > 0
            
            # Simulate human scrolling
            sb.scroll_down(500)
            sb.sleep(1)
            sb.scroll_down(500)
            sb.sleep(1)


class TestInstagramScraperWithSB(BaseCase):
    """Integration tests for Instagram scraping using SeleniumBase"""
    
    def test_instagram_session_creation_with_sb(self):
        """Test creating an Instagram scraping session using SB context manager"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to Instagram
            sb.open("https://www.instagram.com")
            
            # Verify page loaded
            sb.assert_element('input[name="username"]', timeout=10)
            
            # Check URL
            assert "instagram.com" in sb.get_current_url()
    
    def test_instagram_profile_scraping(self):
        """Test scraping Instagram profile data"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to a public profile
            sb.open("https://www.instagram.com/instagram/")
            
            # Wait for profile to load
            sb.assert_element('h2', timeout=15)
            
            # Extract username
            username = sb.get_text('h2')
            assert username is not None
            assert len(username) > 0
            
            # Check for post grid
            if sb.is_element_visible('article'):
                posts = sb.find_elements('article a')
                assert len(posts) > 0


class TestTwitterScraperWithSB(BaseCase):
    """Integration tests for Twitter/X scraping using SeleniumBase"""
    
    def test_twitter_session_creation_with_sb(self):
        """Test creating a Twitter scraping session using SB context manager"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to Twitter
            sb.open("https://twitter.com")
            
            # Verify page loaded
            sb.assert_element('body', timeout=15)
            
            # Check URL
            assert "twitter.com" in sb.get_current_url() or "x.com" in sb.get_current_url()
    
    def test_twitter_profile_scraping(self):
        """Test scraping Twitter profile data"""
        with SB(uc=True, headless=True) as sb:
            # Navigate to a public profile
            sb.open("https://twitter.com/elonmusk")
            
            # Wait for profile to load
            sb.assert_element('div[data-testid="UserName"]', timeout=15)
            
            # Extract username
            username = sb.get_text('div[data-testid="UserName"]')
            assert username is not None
            assert len(username) > 0
            
            # Check for tweets
            if sb.is_element_visible('div[data-testid="tweet"]'):
                tweets = sb.find_elements('div[data-testid="tweet"]')
                assert len(tweets) > 0


class TestAntiBotDetection(BaseCase):
    """Test anti-bot detection bypass capabilities"""
    
    def test_stealth_mode_properties(self):
        """Verify stealth mode properties are set correctly"""
        with SB(uc=True, headless=True) as sb:
            # Execute JavaScript to check WebDriver property
            webdriver_property = sb.execute_script(
                "return navigator.webdriver"
            )
            
            # Should be undefined or false in stealth mode
            assert webdriver_property is None or webdriver_property is False
            
            # Check for Chrome object
            chrome_object = sb.execute_script(
                "return typeof window.chrome"
            )
            
            # Should be 'object' in stealth mode
            assert chrome_object == 'object'
    
    def test_human_like_interaction(self):
        """Test human-like interaction patterns"""
        with SB(uc=True, headless=True) as sb:
            sb.open("https://example.com")
            
            # Simulate human scrolling
            sb.scroll_down(300)
            sb.sleep(1)
            sb.scroll_down(500)
            sb.sleep(1)
            sb.scroll_up(200)
            sb.sleep(1)
            
            # Verify page is still responsive
            sb.assert_element('body', timeout=5)


class TestStealthEngineIntegration:
    """Integration tests for StealthScrapeEngine with SeleniumBase"""
    
    @pytest.fixture
    def stealth_engine(self):
        """Fixture to create a stealth engine instance"""
        try:
            import sys
            sys.path.insert(0, '/media/fi/NewVolume1/project01/selinium')
            from src.backend.stealth_scrape_engine import StealthScrapeEngine
            engine = StealthScrapeEngine({
                'stealth_level': 'maximum',
                'use_residential_proxies': False,
                'cdp_mode': True,
                'uc_mode': True,
                'headless': True
            })
            yield engine
            # Cleanup
            for session_id in list(engine.sessions.keys()):
                engine.close_session(session_id)
        except ImportError:
            pytest.skip("StealthScrapeEngine not available")
    
    def test_facebook_session_creation(self, stealth_engine):
        """Test creating a Facebook scraping session"""
        session_id = stealth_engine.create_session(
            "https://facebook.com/testuser",
            {
                'platform': 'facebook',
                'stealth_level': 'maximum'
            }
        )
        
        assert session_id is not None
        assert len(session_id) == 12  # Session ID format
        
        session = stealth_engine.get_session_status(session_id)
        assert session['status'] in ['initializing', 'initialized', 'ready']
        assert session['target_url'] == "https://facebook.com/testuser"
    
    def test_session_cleanup(self, stealth_engine):
        """Test proper session cleanup"""
        session_id = stealth_engine.create_session(
            "https://facebook.com/testuser",
            {'platform': 'facebook'}
        )
        
        # Verify session exists
        assert session_id in stealth_engine.sessions
        assert stealth_engine.active_sessions == 1
        
        # Close session
        stealth_engine.close_session(session_id)
        
        # Verify session was removed
        assert session_id not in stealth_engine.sessions
        assert stealth_engine.active_sessions == 0
    
    def test_dashboard_stats(self, stealth_engine):
        """Test dashboard statistics generation"""
        stats = stealth_engine.get_dashboard_stats()
        
        assert 'active_sessions' in stats
        assert 'total_sessions' in stats
        assert 'success_rate' in stats
        assert 'system_status' in stats
        assert 'recent_logs' in stats
        
        # Verify types
        assert isinstance(stats['active_sessions'], int)
        assert isinstance(stats['success_rate'], float)
        assert isinstance(stats['system_status'], dict)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--dashboard"])
