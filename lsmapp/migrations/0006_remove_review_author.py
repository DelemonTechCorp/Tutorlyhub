# Generated by Django 5.0 on 2024-03-15 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lsmapp", "0005_alter_review_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="Author",
        ),
    ]
