# Generated by Django 4.1.7 on 2023-03-13 09:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_users_userlevel_alter_feedback_mid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="mid",
            field=models.UUIDField(
                default=uuid.UUID("608509d4-8d0e-42a2-a006-9bf9c7d520c6"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
