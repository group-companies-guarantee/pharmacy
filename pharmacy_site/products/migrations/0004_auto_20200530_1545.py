# Generated by Django 3.0 on 2020-05-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200516_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.CharField(default=1111, help_text='password', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='token',
            field=models.CharField(default=1111, help_text='token', max_length=100),
            preserve_default=False,
        ),
    ]