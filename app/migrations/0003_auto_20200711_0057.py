# Generated by Django 2.2.3 on 2020-07-10 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='views',
            new_name='viewsofquestion',
        ),
    ]
