# Generated by Django 4.0 on 2023-10-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_alter_parent_address_alter_parent_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]