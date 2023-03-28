from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import Message,Book,Users,Library,profile

# Register your models here.
admin.site.register(Message)
admin.site.register(Book)
# admin.site.register(UserLevel)
admin.site.register(Users)
admin.site.register(Library)
# admin.site.register(BLevel)
admin.site.register(profile)
