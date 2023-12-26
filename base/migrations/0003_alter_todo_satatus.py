# Generated by Django 5.0 on 2023-12-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_todo_satatus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="satatus",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("In Progress", "In Progress"),
                    ("Done", "Done"),
                ],
                max_length=50,
            ),
        ),
    ]
