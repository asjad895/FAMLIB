from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import*

# Register your models here.
admin.site.register(Message)
admin.site.register(Content)
# admin.site.register(UserLevel)
admin.site.register(Users)
admin.site.register(Library)
# admin.site.register(BLevel)
admin.site.register(profile)
