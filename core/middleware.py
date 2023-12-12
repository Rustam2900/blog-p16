import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CountRequestsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request, *args, **kwargs):
        self.count += 1
        logger.info(f" Request count: {self.count}")
        return self.get_response(request, *args, **kwargs)
