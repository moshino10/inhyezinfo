# Generated by Django 3.1.3 on 2020-11-03 04:24
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_auto_20201017_0119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetailpage",
            name="blog_category",
            field=models.SmallIntegerField(
                choices=[
                    (0, "National"),
                    (1, "International"),
                    (2, "Sport"),
                    (3, "Divers"),
                    (4, "Believe it or no"),
                    (5, "Culture"),
                    (6, "Opinion and the other opinion"),
                    (7, "Caricature"),
                    (8, "Articles"),
                    (9, "Videos"),
                ],
                verbose_name="blog category",
            ),
        ),
    ]