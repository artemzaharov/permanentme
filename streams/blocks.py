from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')
    image = ImageChooserBlock()

    class Meta:  # noqa
        template = 'streams/title_and_text_block.html'
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    """ Cards with image text and button """

    

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=400)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                # here we will use some logic in the templates for choose link
                ("button_url", blocks.URLBlock(required=False,
                                               help_text='If the button page above is selected, that will be used first.'))

            ]
        )
    )
    class Meta:  # noqa
        template = 'streams/card_block.html'
        icon = "placeholder"
        label = "Service Cards"