# Generated by Django 2.2.5 on 2019-09-19 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=200, verbose_name='Url')),
                ('url_code', models.CharField(max_length=8, verbose_name='Short url')),
            ],
        ),
    ]