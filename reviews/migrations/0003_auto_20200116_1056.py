# Generated by Django 3.0 on 2020-01-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200116_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
