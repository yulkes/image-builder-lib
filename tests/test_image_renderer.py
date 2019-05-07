from pathlib import Path

from PIL import Image, ImageChops, ImageFont
from pytest import fixture

from image_builder_library.render import ImageRenderer
from image_builder_library.template import ImageTemplate, TextElement, TextDirection

SHOULD_SAVE = True

@fixture
def result_directory():
    return Path("comparison_resources")

@fixture
def renderer():
    return ImageRenderer()


def test_image_with_background_color(result_directory):
    template = ImageTemplate(300, 200, None, (255, 0, 0), [])
    result = renderer.render(template)
    _assert_equal_images(result_directory / "red.bmp", result)


def test_image_with_no_background_color(result_directory, renderer):
    template = ImageTemplate(300, 200, None, None, [])
    result = renderer.render(template)
    _assert_equal_images(result_directory / "clear.bmp", result)


def test_image_with_text_element(result_directory, renderer):
    template = ImageTemplate(300, 200, None, None,
                             [TextElement(10, 10, "Hello world", ImageFont.truetype("Arial", size=20), (0, 255, 255), None)])
    result = renderer.render(template)
    _assert_equal_images(result_directory / "simple_text.bmp", result)


def test_image_with_text_element_with_emoji(result_directory, renderer):
    template = ImageTemplate(300, 200, None, None,
                             [TextElement(10, 10, "Hello world ☀️", ImageFont.truetype("Arial", size=20), (0, 255, 255), None)])
    result = renderer.render(template)
    _assert_equal_images(result_directory / "emoji_text.bmp", result)


def test_image_with_text_element_with_hebrew(result_directory, renderer):
    template = ImageTemplate(300, 200, None, None,
                             [TextElement(10, 10, "שלום עולם️", ImageFont.truetype("Arial", size=20), (0, 255, 255), None,
                                          direction=TextDirection.RTL)])
    result = renderer.render(template)
    _assert_equal_images(result_directory / "hebrew_text.bmp", result)

def _assert_equal_images(expected: Path, actual: Image):
    if SHOULD_SAVE:
        actual.save(expected, "bmp")
    if expected.exists():
        expected_image = Image.new("RGB", actual.size)
    else:
        expected_image = Image.open(expected, "r").convert("RGB")
    difference = ImageChops.difference(expected_image, actual)
    if difference.getbbox():
        difference.show()
    assert difference.getbbox() is None
