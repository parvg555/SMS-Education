# Generated by Django 3.2.2 on 2021-05-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_answer_doubt_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
