# Generated by Django 4.2.3 on 2023-11-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel_with_database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
