import time
from django.shortcuts import render
from django.views import View
from .models import Blog as Posts, Reaction
from django.http import StreamingHttpResponse, HttpResponse
from django.template.loader import render_to_string
# Create your views here.

import pprint
class Blog(View):

    def get(self, request):
        blog = Posts.objects.all()
        return render(request, "index.html", {"blogs": blog})
    
    def post(self, request):
        pprint.pprint(request.body)
        pprint.pprint(request.POST)
        return HttpResponse("Hello")


class Notification(View):
    @staticmethod
    def event_stream():
        for i in range(1, 4):
            html = render_to_string(
                "components/toast.html", context={"i": f"Liked you photo {i}"})
            yield f"data: {html} \n\n"
            time.sleep(3)

    def get(self, request):
        response = StreamingHttpResponse(self.event_stream())
        response["Content-Type"] = "text/event-stream"
        return response
