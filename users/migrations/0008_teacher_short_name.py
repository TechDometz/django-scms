# Generated by Django 3.1.2 on 2021-05-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210426_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='short_name',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True),
        ),
    ]