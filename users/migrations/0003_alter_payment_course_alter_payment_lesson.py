# Generated by Django 5.0.2 on 2024-03-06 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='lms.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='lms.lesson', verbose_name='Урок'),
        ),
    ]
