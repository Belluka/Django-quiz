# Generated by Django 2.2.1 on 2019-05-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kviz', '0002_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='answer_text',
        ),
        migrations.AddField(
            model_name='answers',
            name='answer_text1',
            field=models.CharField(default='vnesi vprasanje', max_length=200),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer_text2',
            field=models.CharField(default='vnesi vprasanje', max_length=200),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer_text3',
            field=models.CharField(default='vnesi vprasanje', max_length=200),
        ),
    ]
