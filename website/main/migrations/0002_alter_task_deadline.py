# Generated by Django 4.0.6 on 2022-08-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.TextField(max_length=20, verbose_name='Дэдлайн'),
        ),
    ]