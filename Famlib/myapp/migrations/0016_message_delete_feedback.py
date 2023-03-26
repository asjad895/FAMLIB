# Generated by Django 4.1.7 on 2023-03-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_remove_book_libraryid_book_libraryname_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "mid",
                    models.AutoField(
                        default=1, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("type", models.CharField(max_length=20)),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("heading", models.CharField(max_length=100)),
                ("message", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name="Feedback",
        ),
    ]