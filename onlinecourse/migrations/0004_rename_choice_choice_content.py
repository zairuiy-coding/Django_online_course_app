# Generated by Django 4.2.3 on 2024-05-26 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("onlinecourse", "0003_rename_question_question_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice", old_name="choice", new_name="content",
        ),
    ]
