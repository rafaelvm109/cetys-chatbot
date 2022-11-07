from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __self__(self):
        return self.category


class PatternResponse(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    pattern = models.TextField(max_length=1000)
    response = models.TextField(max_length=1000)

    def __self__(self):
        return self.tag
