from users.models import RequestLog


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.__contains__("/admin/"):
            return self.get_response(request)
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        RequestLog.create_log(
            username=username,
            method=request.method
        )

        return self.get_response(request)