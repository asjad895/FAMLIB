# Generated by Django 4.1.7 on 2023-03-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0019_rename_username_message_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]