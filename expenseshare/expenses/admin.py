from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Expense  # Import your models

# Register your models here
admin.site.register(User)
admin.site.register(Expense)
