from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse

import scrapytest.middlewares.downloader as downloader


class CustomMiddleware(object):
    def process_request(self, request, spider):
        url = str(request.url)
        dl = downloader.CustomDownloader()
        content = dl.VisitPersonPage(url)
        return HtmlResponse(url, status=200, body=content)

    def process_response(self, request, response, spider):
        if len(response.body) == 100:
            return IgnoreRequest("body length == 100")
        else:
            return response