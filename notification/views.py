import time
from django.shortcuts import render
from django.views import View
from .models import Blog as Posts, Reaction, Notification as Message
from django.http import StreamingHttpResponse, HttpResponse
from django.template.loader import render_to_string
from django.db import transaction
# Create your views here.

import pprint
class Blog(View):

    def get(self, request):
        blog = Posts.objects.all()
        return render(request, "index.html", {"blogs": blog})
    
    def post(self, request):    
        sentiment = Reaction.objects.create(sentiment=request.POST["sentiment"], user=self.request.user)
        blog = Posts.objects.get(id=request.POST["id"])    
        blog.reaction = sentiment
        blog.save()
        if sentiment.sentiment == "like":
            return render(request, "components/like.html")
        else:            
            return render(request, "components/dislike.html")


class Notification(View):
    @staticmethod
    def event_stream(request):
        print(request.user)
        notifications = Message.objects.filter(is_read=False).filter(receiver=request.user)
        if len(notifications) >= 1:
            for notices in notifications:
                html = render_to_string(
                    "components/toast.html", context={"notification": notices})
                yield f"data: {html} \n\n"
                time.sleep(3)
        yield "data: "
            

    def get(self, request):
        response = StreamingHttpResponse(self.event_stream(request))
        response["Content-Type"] = "text/event-stream"
        return response
    
    def post(self, request):
        notification = Message.objects.get(id=request.POST["id"])
        notification.is_read = True
        notification.save()
        return HttpResponse("")
