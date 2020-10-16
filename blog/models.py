from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogDetailPage(Page):
    """Blog detail page."""

    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("blog image"),
    )
    description = RichTextField(
        blank=False,
        verbose_name=_("blog description"),
        features=["h2", "h3", "h4", "h5", "bold", "italic", "ol", "ul", "link"],
    )
    content = RichTextField(
        blank=False,
        verbose_name=_("blog content"),
    )
    blog_category = models.SmallIntegerField(
        choices=settings.CATEGORY_CHOICES,
        blank=False,
        null=False,
        verbose_name=_("blog category"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("blog_image"),
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("blog_category"),
    ]
