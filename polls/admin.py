# 必须先在admin中进行注册，告诉admin站点，请将polls的模型加入站点内，接受站点的管理。
from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Article

admin.site.register(Question)
admin.site.register(Article)