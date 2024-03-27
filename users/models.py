from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, default='', verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватарка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey('lms.Course', on_delete=models.CASCADE, verbose_name='Курс', related_name='payments',
                               **NULLABLE)
    lesson = models.ForeignKey('lms.Lesson', on_delete=models.CASCADE, verbose_name='Урок', related_name='payments',
                               **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа')
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('transfer', 'Transfer')],
                                      verbose_name='Способ оплаты')
    payment_url = models.CharField(max_length=500, default='', verbose_name='Ссылка на оплату')
    status = models.CharField(max_length=1, default='P', choices=[("P", "Process"), ("S", "Success"),
                                                                  ("C", "Canceled")], verbose_name='Статус платежа')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'Пользователь {self.user} оплатил курс {self.course} на сумму {self.amount}'
