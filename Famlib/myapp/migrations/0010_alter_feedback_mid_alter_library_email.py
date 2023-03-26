# Generated by Django 4.1.7 on 2023-03-12 14:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_alter_feedback_mid_alter_library_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="mid",
            field=models.UUIDField(
                default=uuid.UUID("07f3dc00-375e-4b6e-9255-b294d2ac9696"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="library",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
