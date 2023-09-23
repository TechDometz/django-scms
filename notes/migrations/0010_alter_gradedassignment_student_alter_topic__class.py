# Generated by Django 4.1 on 2023-09-23 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_classyear_dormitory_examinationlisthandler_and_more'),
        ('notes', '0009_alter_topic_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradedassignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.classroom'),
        ),
    ]