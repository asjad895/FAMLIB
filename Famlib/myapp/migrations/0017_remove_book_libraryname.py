# Generated by Django 4.1.7 on 2023-03-28 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_message_delete_feedback"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="libraryname",
        ),
    ]
