from django.db import models


class Mentor(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50, )
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, null=True, blank=True)
    phonenumber = models.CharField(verbose_name='Номер телефона наставника', max_length=50)
    telegram_id = models.CharField(verbose_name='Telegram ID', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "ментор"
        verbose_name_plural = "менторы"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
