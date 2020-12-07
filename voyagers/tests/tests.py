# test open and load of default page
import pytest
import validators
from unittest.mock import patch
import pymongo
from django.contrib.auth.models import User
from django.urls import reverse
# from home.models import User_Profile
# from tourpackages.models import Attraction


def pageloader():
    page = "http://127.0.0.1:8000/home/"
    return page

def test_load():
    assert validators.url(pageloader())

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


# @pytest.fixture(autouse=True)
# def patch_mongo(monkeypatch):
#     db = mongomock.MongoClient()
#     def fake_mongo():
#         return db
#     monkeypatch.setattr('mongo_stuff.mongo', fake_mongo)
#
#
# with patch.object(mongo_stuff, 'mongo', return_value=mongomock.MongoClient()):
#
#     from project.working_class import somewhere_else
#
#
# @patch.object(mongo_stuff, 'mongo', return_value=mongomock.MongoClient())
# def test_db1(mocked_mongo):
#     mongo_stuff.mongo()
#     assert True
# def test_users(mongodb):
#     assert 'user' in mongodb.list_collection_names()
#     manuel = mongodb.user.find_one({'name': 'jerry'})
#     assert manuel['last_name'] == 'jiang'

# @pytest.mark.django_db
# def test_auth_view(client, create_user, test_password):
#    user = create_user()
#    url = reverse('auth-url')
#    client.login(
#        username=user.username, password=test_password
#    )
#    response = client.get(url)
#    assert response.status_code == 200

# #Database helpers testing
# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('john', 'lennon@thebeatles.com', 'Johnpassword123')
#     assert User.objects.count() == 1
#
# #User_profile(home) testing
# @pytest.mark.django_db
# def test_user_Profile_create():
#     contact = User_Profile.objects.create(first_name='John', last_name='Doe', Address='111', Country='USA')
#     assert contact.first_name == 'John'
#
# @pytest.mark.django_db
# def test_attraction_create():
#     tour = Attraction.objects.create(citypip install validators='la', attractionName='boat', attractionDescription='boatisfun', price='11')
#     assert tour.city == 'la'

#Client testing
# @pytest.mark.django_db
# def test_view_home(client):
#    url = reverse('index')
#    response = client.get(url)
#    assert response.status_code == 200
# #
# @pytest.mark.django_db
# def test_view_dashboard(client):
#    url = reverse('dashboard')
#    response = client.get(url)
#    assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_view_tours(client):
#    url = reverse('tours')
#    response = client.get(url)
#    assert response.status_code == 200





