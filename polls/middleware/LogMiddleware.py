from polls.models import Log
import json
from django.http import JsonResponse


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin'):
            content_type = request.content_type
            if 'application/json' in content_type:
                try:
                    json_data = request.json()
                except json.JSONDecodeError:
                    json_data = None
            else:
                json_data = None

            log = Log(
                path=request.get_full_path(),
                method=request.method,
                body=request.body,
                query=request.GET.dict(),
                json=json_data
            )
            log.save()

        response = self.get_response(request)
        return response
