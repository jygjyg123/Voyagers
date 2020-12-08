# test open and load of default page
import pytest
import validators
from unittest.mock import patch
import pymongo
from django.contrib.auth.models import User
from django.urls import reverse
# from home.models import User_Profile
# from tourpackages.models import Attraction



def pageloader1():
    page = "http://127.0.0.1:8000/login/"
    return page

def test_view_login():
    assert validators.url(pageloader1())

def pageloader2():
    page = "http://127.0.0.1:8000/survey/"
    return page

def test_view_survey():
    assert validators.url(pageloader2())

def pageloader3():
    page = "http://127.0.0.1:8000/tourpackages/"
    return page

def test_view_survey():
    assert validators.url(pageloader3())

def pageloader4():
    page = "http://127.0.0.1:8000/signup/"
    return page

def test_view_signup():
    assert validators.url(pageloader4())








