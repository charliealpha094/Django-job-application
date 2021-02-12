# Generated by Django 3.1.6 on 2021-02-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20210210_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('employed', 'Employed'), ('archived', 'Archived')], default='active', max_length=20),
        ),
    ]
