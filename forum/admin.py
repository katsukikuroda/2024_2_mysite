from django.contrib import admin
from .models import Topic, Message, Comment, Tag
 


admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Tag)
