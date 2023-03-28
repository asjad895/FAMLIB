# Generated by Django 4.1.7 on 2023-03-28 12:02

import django.core.validators
from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_alter_message_mid_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="file",
            field=models.FileField(
                upload_to="library_content/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=[
                            "pdf",
                            "doc",
                            "docs",
                            "txt",
                            "zip",
                            ".py",
                            "jpg",
                            "jpeg",
                            "png",
                            "docx",
                            "xls",
                            "xlsx",
                            "ppt",
                            "pptx",
                        ]
                    ),
                    myapp.models.validate_file_size,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics/"),
        ),
    ]