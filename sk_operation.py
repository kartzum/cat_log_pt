import uuid

from model import CatalogSchemeOperationInstance, AppData, app_data, CatalogOperationInstanceResult

from load_operation import LoadOperation

from scraper import ResponseEventHandler, NavigationPlaywrightResourceScraper


class ShowcasesResponseEventHandler(ResponseEventHandler):

    def __init__(self, process_response_handler):
        self.process_response_handler = process_response_handler

    def is_applicable_response(self, response):
        return "/v2/showcases" in response.url and "list" not in response.url

    def process_response(self, response):
        self.process_response_handler(response)


class SkLoadNewOperation(LoadOperation):
    def __init__(self, instance: CatalogSchemeOperationInstance, application_data: AppData):
        self.instance = instance
        self.application_data = application_data

    def run(self):
        def response_handler(response):
            self.instance.is_complete = True
            result = response.json()
            instance_result = CatalogOperationInstanceResult(
                str(uuid.uuid1()),
                self.instance.identifier,
                self.instance.catalog_id,
                result
            )
            self.application_data.catalog_results[instance_result.identifier] = instance_result

        def page_handler(page):
            page.locator('.CategoryLink_root__SrUi8').and_(page.get_by_role("link")).filter(
                has_text="Что нового").click()

        self.instance.is_running = True

        response_handler = ShowcasesResponseEventHandler(response_handler)
        scraper = NavigationPlaywrightResourceScraper(response_handler, "https://samokat.ru", page_handler)

        scraper.run()
