# Generated by Django 4.2.4 on 2023-09-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема письма')),
                ('email', models.EmailField(max_length=255, verbose_name='Электронный адрес (email)')),
                ('content', models.TextField(verbose_name='Содержимое письма')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'db_table': 'app_feedback',
                'ordering': ['-time_create'],
            },
        ),
    ]
