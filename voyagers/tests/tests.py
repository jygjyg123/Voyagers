# test open and load of default page
import pytest
import validators
import uuid
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import User_Profile
from tourpackages.models import Attraction


def pageloader():
    page = "http://127.0.0.1:8000/home/"
    return page


def test_load():
    assert validators.url(pageloader())

#Database helpers testing
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1

#User_profile(home) testing
@pytest.mark.django_db
def test_user_Profile_create():
    contact = User_Profile.objects.create(first_name='John', last_name='Doe', Address='111', Country='USA')
    assert contact.first_name == 'John'

@pytest.mark.django_db
def test_attraction_create():
    tour = Attraction.objects.create(city='la', attractionName='boat', attractionDescription='boatisfun', price='11')
    assert tour.city == 'la'

#Client testing
@pytest.mark.django_db
def test_view_home(client):
   url = reverse('index')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_view_dashboard(client):
   url = reverse('dashboard')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_view_tours(client):
   url = reverse('tours')
   response = client.get(url)
   assert response.status_code == 200


# @pytest.mark.django_db
# def test_with_authenticated_client(client, django_user_model):
#     username = "user1"
#     password = "bar"
#     user = django_user_model.objects.create_user(username=username, password=password)
#     # Use this:
#     # Or this:
#     client.login(username=username, password=password)
#     response = client.get('login')
#     assert response.content == 'Protected Area'

# @pytest.fixture
# def test_password():
#     return 'strong-test-pass'
#
#
# @pytest.fixture
# def create_user(db, django_user_model, test_password):
#     def make_user(**kwargs):
#         kwargs['password'] = test_password
#         if 'username' not in kwargs:
#             kwargs['username'] = str(uuid.uuid4())
#         return django_user_model.objects.create_user(**kwargs)
#
#     return make_user
#
# @pytest.mark.django_db
# def test_user_detail(client, create_user):
#    user = create_user(username='someone')
#    url = reverse('index', kwargs={'pk': user.pk})
#    response = client.get(url)
#    assert response.status_code == 200
#    assert 'someone' in response.content


