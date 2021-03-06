# Generated by Django 3.0 on 2020-01-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=400)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(blank=True, null=True)),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
