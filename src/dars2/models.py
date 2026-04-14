from django.db import models

# Create your models here.


class TodoList(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = "yangi", "Yangi"
        IN_PROGRESS = "jarayonda", "Jarayonda"
        COMPLATED = "bajarilgan", "Bajarilgan"

    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.NEW)

    def __str__(self):
        return self.title
    
# 5 minut
# pip install django django-rest-framework 


# seralizer, views, urls, test qilib 3 ta malumot qoshasizlar.

class ExampleModel(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    price = models.IntegerField(default=12)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz
