# Generated by Django 3.1.2 on 2021-05-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0007_auto_20210503_0654'),
        ('administration', '0007_classjournal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classjournal',
            name='absent_students',
            field=models.ManyToManyField(blank=True, to='sis.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='classjournal',
            unique_together={('date',)},
        ),
    ]