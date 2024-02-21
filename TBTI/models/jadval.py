from django.db import models

# Create your models here.

class TBTI(models.Model):
    name = models.CharField("ФИО", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    Phone_number = models.IntegerField()
    Email = models.CharField("Email", max_length=50)
    day_of_barth= models.DateField("Год раждение")


    class Meta:
        verbose_name = "Гурӯҳ"
        verbose_name_plural = "Гурӯҳҳо"

    def __str__(self) -> str:
        return self.name