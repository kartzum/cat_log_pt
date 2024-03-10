from playwright.sync_api import sync_playwright


class ResourceScraper:
    def run(self):
        pass


class PlaywrightResourceScraper(ResourceScraper):
    def run(self):
        with sync_playwright() as p:
            browser = None
            try:
                browser = p.chromium.launch(headless=False)
                self.process(browser)
            finally:
                if browser is not None:
                    browser.close()

    def process(self, browser):
        pass


class ResponseEventHandler:
    def handle(self, response):
        if self.is_applicable_response(response):
            self.process_response(response)

    def is_applicable_response(self, response):
        pass

    def process_response(self, response):
        pass


class NavigationPlaywrightResourceScraper(PlaywrightResourceScraper):
    def __init__(self, response_handler, main_url, page_handler):
        self.response_handler = response_handler
        self.main_url = main_url
        self.page_handler = page_handler

    def process(self, browser):
        page = browser.new_page()
        page.goto(self.main_url)
        page.on("response", lambda response: self.response_handler.handle(response))
        page.wait_for_timeout(10)
        self.page_handler(page)
        page.wait_for_timeout(10000)
