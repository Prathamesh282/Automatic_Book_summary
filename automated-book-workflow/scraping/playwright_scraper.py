from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Save screenshot in Outputs folder
        page.screenshot(path=f"{output_dir}/scrap_screenshot.png", full_page=True)
        
        # Extract content from screenshot
        content = page.inner_text("#mw-content-text")
        with open(f"{output_dir}/raw_chapter.txt", "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()