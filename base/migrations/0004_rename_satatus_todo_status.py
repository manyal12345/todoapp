# Generated by Django 5.0 on 2023-12-29 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_todo_satatus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="satatus",
            new_name="status",
        ),
    ]
