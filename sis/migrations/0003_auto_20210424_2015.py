# Generated by Django 3.1.2 on 2021-04-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0002_auto_20210424_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradescalerule',
            name='letter_grade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='gradescalerule',
            name='numeric_scale',
            field=models.DecimalField(blank=True, decimal_places=2, default=507, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='post_code',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]