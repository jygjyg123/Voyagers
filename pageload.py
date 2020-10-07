# test open and load of default page
import pytest
import validators

def pageloader():
    page = "https://github.com/jygjyg123/Voyagers"
    return page

def test_load():
    assert validators.url(pageloader())
