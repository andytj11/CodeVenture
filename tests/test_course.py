# test_course.py

import pytest
from course import TranslationInterface, CourseInterface

# Sample translations for testing
sample_translations = {
    "1": {
        "title": {
            "en": "Variables Type",
            "bm": "Jenis Pemboleh Ubah",
            "zh": "变量类型"
        },
        "content": {
            "en": ["Variables Type:", "Examples:", "x = 5"],
            "bm": ["Jenis Pemboleh Ubah:", "Contoh:", "x = 5"],
            "zh": ["变量类型:", "例子:", "x = 5"]
        }
    }
}

# Sample course content for testing
sample_course_content = {
    "1": {
        "title": {
            "en": "Variables Type"
        },
        "content": {
            "en": ["Variables Type:", "Examples:", "x = 5"]
        }
    },
    "2": {
        "title": {
            "en": "Loops"
        },
        "content": {
            "en": ["Loops:", "Examples:", "for x in range(5):"]
        }
    }
}



def test_translation_interface_positive_en():
    """Positive Test: Check translation for English content."""
    translator = TranslationInterface()
    title, content = translator.get_translation("1", "1")
    assert title == "Variables Type"
    assert "Variables Type:" in content

    title, content = translator.get_translation("2", "1")
    assert title == "Loops"
    assert "Loops:" in content


def test_translation_interface_positive_bm():
    """Positive Test: Check translation for Malay content."""
    translator = TranslationInterface()
    title, content = translator.get_translation("2", "2")
    assert title == "Gelung"
    assert "Gelung:" in content

    title, content = translator.get_translation("1", "2")
    assert title == "Jenis Pemboleh Ubah"
    assert "Jenis Pemboleh Ubah:" in content


def test_translation_interface_positive_zh():
    """Positive Test: Check translation for Chinese content."""
    translator = TranslationInterface()
    title, content = translator.get_translation("1", "3")
    assert title == "变量类型"
    assert "变量类型:" in content

    title, content = translator.get_translation("2", "3")
    assert title == "循环"
    assert "循环:" in content

# Negative Tests

def test_translation_interface_invalid_topic():
    """Negative Test: Check behavior for an invalid topic ID."""
    translator = TranslationInterface()
    with pytest.raises(KeyError):
        translator.get_translation("100", "1")

    with pytest.raises(KeyError):
        translator.get_translation("100", "2")

    with pytest.raises(KeyError):
        translator.get_translation("100", "3")

    with pytest.raises(KeyError):
        translator.get_translation("100", "4")


def test_translation_interface_invalid_language():
    """Negative Test: Check behavior for an invalid language ID, should default to English."""
    translator = TranslationInterface()
    title, content = translator.get_translation("1", "100")
    assert title == "Variables Type"
    assert "Variables Type:" in content

    title, content = translator.get_translation("2", "100")
    assert title == "Loops"
    assert "Loops:" in content





