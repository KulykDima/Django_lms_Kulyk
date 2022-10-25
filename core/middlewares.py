import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()
        duration = end - start
        print(f'Request for url "{request.path}" was processed: {round(duration, 2)} s')
        return response
