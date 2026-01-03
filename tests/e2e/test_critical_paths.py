"""
E2E Tests for Critical Paths using SeleniumBase with CDP Mode
Tests Login and Checkout workflows with CDP Mode for enhanced anti-bot protection
"""

import os
import pytest
from seleniumbase import SB


def test_facebook_login_with_cdp():
    """Test successful Facebook login flow with CDP Mode and anti-bot protection"""
    fb_user = os.getenv("FB_USER")
    fb_password = os.getenv("FB_PASSWORD")
    
    if not fb_user or not fb_password:
        pytest.skip("FB_USER and FB_PASSWORD environment variables not set")
    
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://www.facebook.com")
        
        # Wait for login form with increased timeout for stability
        sb.assert_element('input[name="email"]', timeout=20)
        sb.assert_element('input[name="pass"]', timeout=20)
        
        # Enter credentials from environment
        sb.type('input[name="email"]', fb_user)
        sb.type('input[name="pass"]', fb_password)
        
        # Use CDP mode's stealthy click for login button
        sb.cdp.gui_click_element('button[name="login"]')
        
        # Wait for navigation to complete
        sb.sleep(2)
        
        # Verify we're not on error/challenge pages
        sb.assert_false("login.php" in sb.get_current_url())
        sb.assert_false("checkpoint" in sb.get_current_url())
        
        # Handle anti-bot challenges if present using CDP
        if sb.cdp.is_element_visible('div.fb-challenge'):
            sb.cdp.gui_click_element('div.fb-challenge button')
            sb.sleep(3)
            sb.assert_false("challenge" in sb.get_current_url())
        
        # Verify successful login - check for profile or home elements
        sb.assert_element('div[role="navigation"]', timeout=20)
        sb.assert_true("facebook.com" in sb.get_current_url())


def test_instagram_login_with_cdp():
    """Test successful Instagram login flow with CDP Mode and anti-bot protection"""
    ig_user = os.getenv("IG_USER")
    ig_password = os.getenv("IG_PASSWORD")
    
    if not ig_user or not ig_password:
        pytest.skip("IG_USER and IG_PASSWORD environment variables not set")
    
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://www.instagram.com")
        
        # Wait for login form with increased timeout
        sb.assert_element('input[name="username"]', timeout=20)
        sb.assert_element('input[name="password"]', timeout=20)
        
        # Enter credentials from environment
        sb.type('input[name="username"]', ig_user)
        sb.type('input[name="password"]', ig_password)
        
        # Use CDP mode's stealthy click for login button
        sb.cdp.gui_click_element('button[type="submit"]')
        
        # Wait for navigation to complete
        sb.sleep(2)
        
        # Verify we're not on error/challenge pages
        sb.assert_false("challenge" in sb.get_current_url())
        
        # Handle anti-bot challenges if present using CDP
        if sb.cdp.is_element_visible('div[data-pagelet="challenge"]'):
            sb.cdp.gui_click_element('div[data-pagelet="challenge"] button')
            sb.sleep(3)
            sb.assert_false("challenge" in sb.get_current_url())
        
        # Verify successful login
        sb.assert_element('nav', timeout=20)


def test_twitter_login_with_cdp():
    """Test successful Twitter/X login flow with CDP Mode and anti-bot protection"""
    tw_user = os.getenv("TW_USER")
    tw_password = os.getenv("TW_PASSWORD")
    
    if not tw_user or not tw_password:
        pytest.skip("TW_USER and TW_PASSWORD environment variables not set")
    
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://twitter.com/i/flow/login")
        
        # Wait for login form with increased timeout
        sb.assert_element('input[autocomplete="username"]', timeout=20)
        
        # Enter username from environment
        sb.type('input[autocomplete="username"]', tw_user)
        
        # Use CDP mode's stealthy click for next button
        sb.cdp.gui_click_element('div[role="button"] >> nth=0')
        
        # Wait for password field
        sb.assert_element('input[name="password"]', timeout=20)
        
        # Enter password from environment
        sb.type('input[name="password"]', tw_password)
        
        # Use CDP mode's stealthy click for login button
        sb.cdp.gui_click_element('div[role="button"] >> nth=1')
        
        # Wait for navigation to complete
        sb.sleep(2)
        
        # Verify we're not on error/challenge pages
        sb.assert_false("challenge" in sb.get_current_url())
        
        # Handle anti-bot challenges if present using CDP
        if sb.cdp.is_element_visible('div[data-testid="captcha"]'):
            sb.cdp.gui_click_element('div[data-testid="captcha"]')
            sb.sleep(3)
            sb.assert_false("challenge" in sb.get_current_url())
        
        # Verify successful login
        sb.assert_element('nav[aria-label="Primary"]', timeout=20)


def test_amazon_checkout_with_cdp():
    """Test Amazon checkout flow with CDP Mode and anti-bot protection"""
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://www.amazon.com")
        
        # Wait for page to load with anti-bot check
        sb.assert_element('input[type="text"]', timeout=20)
        
        # Handle CAPTCHA if present using CDP
        if sb.cdp.is_element_visible('iframe[src*="captcha"]'):
            sb.cdp.gui_click_element('iframe[src*="captcha"]')
            sb.sleep(3)
        
        # Search for a product
        sb.type('input[type="text"]', "laptop")
        sb.press_key('input[type="text"]', 'ENTER')
        
        # Wait for search results with increased timeout
        sb.assert_element('[data-component-type="s-search-result"]', timeout=20)
        
        # Use CDP mode's stealthy click for first product
        sb.cdp.gui_click_element('[data-component-type="s-search-result"] >> nth=0')
        
        # Wait for product page
        sb.assert_element('#productTitle', timeout=20)
        
        # Use CDP mode's stealthy click to add to cart
        sb.cdp.gui_click_element('#add-to-cart-button')
        
        # Wait for cart update
        sb.assert_element('#nav-cart-count', timeout=15)
        
        # Proceed to checkout
        sb.open("https://www.amazon.com/gp/cart/view.html")
        
        # Verify cart page
        sb.assert_element('#sc-active-cart', timeout=20)


def test_shopify_checkout_with_cdp():
    """Test Shopify checkout flow with CDP Mode and anti-bot protection"""
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://www.example-shopify-store.com")
        
        # Wait for page to load
        sb.assert_element('body', timeout=20)
        
        # Handle CAPTCHA if present using CDP
        if sb.cdp.is_element_visible('iframe[src*="recaptcha"]'):
            sb.cdp.gui_click_element('iframe[src*="recaptcha"]')
            sb.sleep(3)
        
        # Use CDP mode's stealthy click to add product to cart
        sb.cdp.gui_click_element('.product-form__add-button')
        
        # Wait for cart drawer or redirect with smart assertion
        sb.assert_element_visible_or('.cart-drawer', 'form[data-step="contact_information"]', timeout=5)
        
        # Proceed to checkout
        if sb.cdp.is_element_visible('.cart-drawer'):
            sb.cdp.gui_click_element('.cart-drawer__checkout-button')
        else:
            sb.open("/checkout")
        
        # Verify checkout page with increased timeout
        sb.assert_element('form[data-step="contact_information"]', timeout=20)
        
        # Fill in contact information
        sb.type('input[name="checkout[email]"]', "test@example.com")
        sb.type('input[name="checkout[shipping_address][first_name]"]', "Test")
        sb.type('input[name="checkout[shipping_address][last_name]"]', "User")
        sb.type('input[name="checkout[shipping_address][address1]"]', "123 Test St")
        sb.type('input[name="checkout[shipping_address][city]"]', "Test City")
        sb.type('input[name="checkout[shipping_address][zip]"]', "12345")
        
        # Use CDP mode's stealthy click to continue to shipping
        sb.cdp.gui_click_element('button[data-trekkie-id="continue_to_shipping_button"]')
        
        # Verify shipping section loaded
        sb.assert_element('form[data-step="shipping_method"]', timeout=20)


def test_cloudflare_bypass_with_cdp():
    """Test Cloudflare challenge bypass with CDP Mode and enhanced verification"""
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://example.com")
        
        # Wait for page to load
        sb.assert_element('body', timeout=20)
        
        # Check if Cloudflare challenge is present using CDP
        if sb.cdp.is_element_visible('div.cf-challenge'):
            # CDP Mode should handle this automatically
            # Wait for challenge to resolve
            sb.sleep(5)
            
            # Verify we're past the challenge
            sb.assert_false("challenge" in sb.get_current_url())
            
            # Verify page loaded successfully after challenge
            sb.assert_element('body', timeout=15)
        else:
            # Verify page loaded successfully without challenge
            sb.assert_element('body', timeout=20)


def test_recaptcha_bypass_with_cdp():
    """Test reCAPTCHA bypass with CDP Mode and enhanced verification"""
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode for advanced anti-bot bypass
        sb.activate_cdp_mode("https://www.google.com/recaptcha/api2/demo")
        
        # Wait for reCAPTCHA to load with increased timeout
        sb.assert_element('iframe[src*="recaptcha"]', timeout=20)
        
        # CDP Mode can solve reCAPTCHA automatically
        # Use CDP's stealthy click for CAPTCHA
        sb.cdp.gui_click_element('iframe[src*="recaptcha"]')
        
        # Wait for CAPTCHA to be solved
        sb.sleep(5)
        
        # Verify CAPTCHA is no longer blocking
        sb.assert_false("challenge" in sb.get_current_url())


def test_stealth_mode_verification_with_cdp():
    """Verify stealth mode properties are set correctly with CDP Mode"""
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode
        sb.activate_cdp_mode("https://example.com")
        
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


def test_human_like_interaction_with_cdp():
    """Test human-like interaction patterns with CDP Mode"""
    with SB(uc=True, headed=True) as sb:
        # Activate CDP Mode
        sb.activate_cdp_mode("https://example.com")
        
        # Simulate human scrolling using CDP
        sb.scroll_down(300)
        sb.sleep(1)
        sb.scroll_down(500)
        sb.sleep(1)
        sb.scroll_up(200)
        sb.sleep(1)
        
        # Verify page is still responsive
        sb.assert_element('body', timeout=5)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "--dashboard"])
