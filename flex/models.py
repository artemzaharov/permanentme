from django.db import models
from home.models import LeftMenu
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
# Create your models here.
class FlexPage(Page):
    """Flexible page class."""
    
    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
        ],
        null=True,
        blank=True,
        # title_and_text и full_richtext названия для админки не переменные
    )

    
    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"


class FormField(AbstractFormField):
    page = ParentalKey(
        'ServicePage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )
	 
	 
class ServicePage(AbstractEmailForm):
    
    template = "flex/contact.html"
    landing_page_template = "flex/contact_landing.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    button_text = models.CharField(blank=True, max_length=100)
    thank_you_text = models.CharField(blank=True, max_length=200)
    
    left_menu = models.ForeignKey(
        LeftMenu, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    
    content_panels = AbstractEmailForm.content_panels + [
 
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('button_text'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
        SnippetChooserPanel("left_menu"),
    ]
