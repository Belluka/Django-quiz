from django.db import models

class Category(models.Model):
	category_text = models.CharField(max_length=200)

class Question(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)

class Answers(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=200, default="vnesi vprasanje")
	solution = models.BooleanField(default=False)