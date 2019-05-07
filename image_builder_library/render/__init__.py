from PIL import Image
from PIL.ImageDraw import ImageDraw

from image_builder_library.template import ImageTemplate, TextElement


class ImageRenderer(object):

    def render(self, template: ImageTemplate) -> Image.Image:
        result = self._render_base(template)
        drawer = ImageDraw(result)
        for element in template.elements:
            self._render_image_element(drawer, element)
        return result

    def _render_base(self, template: ImageTemplate):
        result = Image.new("RGB", (template.width, template.height), template.background_color)
        if template.background_image:
            pass
        return result

    def _render_image_element(self, drawer: ImageDraw, element: Image):
        if isinstance(element, TextElement):
            self._render_text(drawer, element)

    def _render_text(self, drawer: ImageDraw, text_element: TextElement):
        drawer.text(xy=text_element.location, text=text_element.text, fill=text_element.text_color,
                    font=text_element.font, direction=text_element.direction.value, align=text_element.align.value)
