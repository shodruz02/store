from django.db import models

# Create your models here.

class Providers(models.Model):
    name = models.CharField("Название", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    Phone_number = models.IntegerField()
    Email = models.CharField("Email", max_length=50)


    class Meta:
        verbose_name = "Провайдер"
        verbose_name_plural = "Провайдеры"

    def __str__(self) -> str:
        return self.name