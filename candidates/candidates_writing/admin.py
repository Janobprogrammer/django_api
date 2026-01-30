from django.contrib import admin
from .models import Feedback, Task, Essay


admin.site.register(Task)
admin.site.register(Feedback)
admin.site.register(Essay)
