# Generated by Django 4.2.2 on 2023-06-24 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0004_alter_article_author_alter_comment_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
