# Project Rescue Specification: SeleniumBase Migration & Stabilization

## 1. Project Context
The current Selenium project is unstable ("struggling at the end").
**Goal**: Refactor the existing codebase to use **SeleniumBase** patterns, specifically leveraging **UC Mode** and **CDP Mode** to bypass detection and eliminate flakiness.

## 2. Technical Stack & Standards
- **Framework**: SeleniumBase (Must replace raw Selenium WebDriver).
- **Runner**: Pytest.
- **Syntax Pattern**: Use the `SB` Context Manager (`with SB(uc=True) as sb:`) OR `BaseCase` class inheritance.
- **Strict Prohibition**: 
  - NO `time.sleep()` (Use `sb.sleep()` or smart waits).
  - NO raw `driver.find_element(...)` (Use `sb.click()`, `sb.type()`, `sb.assert_element()`).

## 3. Stabilization Strategies (Derived from Knowledge Base)
### A. Anti-Bot / Stealth (Priority High)
If a test fails due to 403 Forbidden, CAPTCHA, or "Element Not Found" on login:
1.  **Enable UC Mode**: Initialize driver with `uc=True`.
2.  **Enable CDP Mode**: For complex scraping, use `sb.activate_cdp_mode(url)`.
3.  **Smart Clicks**: Use `sb.cdp.gui_click_element(selector)` for stealthy interactions.

### B. Flakiness Fixes
1.  **Automatic Waiting**: SeleniumBase methods automatically wait for element readiness. Do not add explicit `WebDriverWait`.
2.  **Selector Strategy**: Prefer CSS Selectors. If using XPath, ensure it is robust relative to text (e.g., `//button[contains(text(), 'Login')]`).

## 4. Execution Plan (BMAD Agile Workflow)

### Step 1: Architect Analysis
- Scan existing raw Selenium files.
- Map raw WebDriver calls to SeleniumBase equivalents (e.g., `send_keys` -> `type`).
- Identify areas requiring UC Mode (Login screens, Cloudflare pages).

### Step 2: Developer Refactor
- Convert one test file at a time.
- **Pattern**:
  ```python
  from seleniumbase import BaseCase
  class MyTest(BaseCase):
      def test_example(self):
          self.open("url")
          self.type("selector", "text")
          self.click("selector")
# or if stealth is needed
from seleniumbase import SB
with SB(uc=True) as sb:
    sb.open("url")
    sb.type("selector", "text")           