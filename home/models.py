from django.db import models

from wagtail.core.models import Page


from wagtailtrans.models import TranslatablePage
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField

class TransHomePage(TranslatablePage):
    body = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class TransLandingPage(TranslatablePage):

    body = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]