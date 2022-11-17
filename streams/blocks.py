from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class MenuBlock(blocks.StructBlock):

    title_menu = blocks.CharBlock(required=True, help_text='Add your title')
    title_url = blocks.URLBlock(required=True, help_text='Add additional text')
    
    class Meta:  # noqa
        template = 'streams/menu_block.html'
        icon = "edit"
        label = "Menus"

class TitleAndTextBlock(blocks.StructBlock):
    ''' Simple reuseble title and text block'''
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')
    image = ImageChooserBlock()

    class Meta:  # noqa
        template = 'streams/title_and_text_block.html'
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    """ Reuseble Card with image text and button """

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