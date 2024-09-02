from django.contrib import admin

from .models import Choice, Question, Example

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Example)