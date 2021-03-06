# Generated by Django 3.1.2 on 2020-10-15 14:47
import django.db.models.deletion
import wagtail.core.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0052_pagelogentry"),
        ("wagtailimages", "0022_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogListingPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "custom_title",
                    models.CharField(
                        help_text="Overwrites the default title", max_length=100
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogDetailPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "custom_title",
                    models.CharField(
                        help_text="Overwrites the default title",
                        max_length=100,
                        verbose_name="blog title",
                    ),
                ),
                (
                    "description",
                    wagtail.core.fields.RichTextField(verbose_name="blog description"),
                ),
                (
                    "blog_category",
                    models.SmallIntegerField(
                        choices=[
                            (0, "National"),
                            (1, "International"),
                            (2, "Divers"),
                            (3, "Believe it or no"),
                            (4, "Culture"),
                            (4, "Opinion and the other opinion"),
                            (4, "Caricature"),
                            (4, "Videos"),
                        ],
                        verbose_name="blog category",
                    ),
                ),
                (
                    "blog_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="blog image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
