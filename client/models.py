from django.db import models

from surur.models import Tour


class Client(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT, verbose_name='Заголовок тура', null=True)
    full_name = models.CharField(max_length=100, verbose_name='Имя Фамилия')
    email = models.EmailField(verbose_name='Эмэйл')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон номер')
    payment_id = models.BigIntegerField(null=True)
    payment_status = models.IntegerField(null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'  
