from django.shortcuts import redirect, render
from .models import Topic, Message, Comment
from .forms import CommentForm, MessageForm
from django.db.models import Count, Max, OuterRef, Subquery
from django.db.models.functions import Greatest, Coalesce
from django.views.generic.list import ListView

 
class IndexView(ListView):
    template_name = "forum/index.html"
    model = Topic

    def get_queryset(self, **kwargs):
        queryset = (
            Topic.objects.all()
            .annotate(
                letest_message_date=Max("topic_message__created_at"),
                letest_comment_date=Max("topic_message__comment__created_at"),
                latest_date=Greatest("letest_message_date", "letest_comment_date"),
                time=Coalesce(
                    "latest_date", "letest_message_date", "letest_comment_date"
                ),
            )
            .order_by("-time")
        )
        return queryset
 

class ForumView(ListView):
    template_name = "forum/forum.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        topic = Topic.objects.get(name=self.kwargs["topic"])
        context["topic"] = topic

        context["message_form"] = MessageForm()
        context["comment_form"] = CommentForm()

        return context

    def get_queryset(self, **kwargs):
        topic = Topic.objects.get(name=self.kwargs["topic"])
        subquery = Comment.objects.filter(message=OuterRef("id")).order_by(
            "-created_at"
        )
        queryset = (
            Message.objects.filter(topic=topic)
            .annotate(
                reply_num=Count("comment"),
                latest_reply_date=Subquery(subquery.values("created_at")[:1]),
            )
            .prefetch_related("tag", "comment")
            .order_by("created_at")
        )
        return queryset

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            topic = Topic.objects.get(name=self.kwargs["topic"])

            if "message" in request.POST:

                message_form = MessageForm(request.POST, request.FILES)

                if message_form.is_valid():
                    message_form.instance.topic = topic
                    message_form.instance.user = request.user
                    message = message_form.save()
                    for tag in message_form.cleaned_data["tag"]:
                        message.tag.add(tag)

            elif "comment" in request.POST:

                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():

                    message_id = request.POST["comment"]
                    message = Message.objects.get(id=message_id)

                    comment_form.instance.message = message
                    comment_form.instance.user = request.user
                    comment_form.save()

            return redirect("forum:forum", topic=topic.name)

        else:
            return redirect("forum:forum", topic=self.kwargs["topic"])