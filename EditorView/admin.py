from django.contrib import admin

# Register your models here.
from .models import Category, PatternResponse

admin.site.register(Category)
admin.site.register(PatternResponse)