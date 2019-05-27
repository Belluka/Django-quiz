from django.contrib import admin
from .models import Category, Question, Answers

admin.register(Category, Question, Answers)(admin.ModelAdmin)