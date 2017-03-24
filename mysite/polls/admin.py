from django.contrib import admin

# Register your models here.

from polls.models import question,choice

admin.site.register(question.Question)
admin.site.register(choice.Choice)
