# Generated by Django 5.0 on 2024-03-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lsmapp", "0002_remove_review_reviewtitle_review_author_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="Author",
        ),
    ]