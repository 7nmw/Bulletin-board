from django.contrib import admin
from .models import Author, Category, Notice, Responses, SubscribersCategory


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Notice)
admin.site.register(Responses)
admin.site.register(SubscribersCategory)