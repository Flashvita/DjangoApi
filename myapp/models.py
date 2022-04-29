from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Категория')
    slug = models.SlugField()

    def __str__(self):
        return self.title
