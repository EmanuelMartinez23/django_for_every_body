from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        validators= [ MinLengthValidator(2, "Title must be greater than 2 characters")],
        verbose_name="title"
    )
    # price = models.DecimalField(max_digits= 7, decimal_places = 2, null = True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, verbose_name="precio")
    text = models.TextField(verbose_name="text")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =  models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add  =True)
    updated_at =  models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title