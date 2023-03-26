# Generated by Django 4.1.7 on 2023-03-11 10:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_book_id_alter_feedback_mid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("dc4fd5de-80a5-4ced-8143-aa64b1617ca0"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="mid",
            field=models.UUIDField(
                default=uuid.UUID("4ab4f385-9137-4749-bad7-711a672b5e8a"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="married",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]