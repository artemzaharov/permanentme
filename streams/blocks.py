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