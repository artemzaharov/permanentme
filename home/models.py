from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks



class HomePage(Page):
    """ Home page model."""

    template = "home/home_page.html"
    max_count = 1
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = models.CharField(max_length=150, blank=False, null=True)
    banner_text = models.TextField(max_length=1000, blank=False, null=True)
    banner_button = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bunner_button_text = models.CharField(max_length=100, blank=False, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    services = models.CharField(max_length=100, blank=False, null=True)
    content = StreamField(
        [
            ("cards", blocks.CardBlock())
        ],
        null=True,
        blank=True,
        # title_and_text и full_richtext названия для админки не переменные
    )

    content_panels = Page.content_panels +[
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            FieldPanel("banner_text"),
            PageChooserPanel("banner_button"),
            FieldPanel("bunner_button_text"),
            ImageChooserPanel("banner_image"),
        ], heading="Information"),
        MultiFieldPanel([
            FieldPanel("services"),
            StreamFieldPanel("content"),
        ], heading="Services")
    ]