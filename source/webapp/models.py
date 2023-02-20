from django.db import models

# Create your models here.


class Payment(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Cумма')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")
