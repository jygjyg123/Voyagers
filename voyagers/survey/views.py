from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Survey, create_surveyAnswer, save_surveyAnswer
import json
from django.http import HttpResponse
from dashboard.forms import UserForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from .forms import surveyForm
import pymongo
from pymongo import MongoClient
from django.contrib.auth import update_session_auth_hash
from dashboard.views import dashboard


myclient = MongoClient(
    "mongodb+srv://Voyagers:Voyagers123@cluster0.45hpd.mongodb.net/<dbname>?retryWrites=true&w=majority")
mydb = myclient["voyagers"]
mycol = mydb["survey_survey"]






@login_required()
def survey(request):
    old_data = mycol.find()
    for i in old_data:
        older_data = i

        pk = request.user.pk
        user = User.objects.get(pk=pk)

        if request.method == 'POST':
            a = (request.POST)
            country = a.get('country')
            city = a.get('city')
            tour = a.get('tour')
            departure = a.get('departure')
            fcd = a.get('futureCompanionDescription')
            gender = a.get('gender')

            survey_data = {"$set": {
                'country': f'{country}',
                'city': f'{city}',
                'tour': f'{tour}',
                'departure': f'{departure}',
                'futureCompanionDescription': f'{fcd}',
                'gender': f'{gender}'
            }}

            if pk in older_data.values():
                mycol.update_one(older_data, survey_data)
           

    return render(request, 'survey.html')

    # ProfileInlineFormset = inlineformset_factory(User, surveyForm, fields=('country',
    #                                                                    'city',
    #                                                                    'tour',
    #                                                                    'departure',))
    # formset = ProfileInlineFormset(instance=user)
    # if request.user.is_authenticated and request.user.id == user.id:
    #     if request.method == "POST":
    #         form = UserForm(request.POST, instance=request.user)
    #         formset = ProfileInlineFormset(
    #             request.POST, request.FILES, instance=user)

    #         if form.is_valid():
    #             custom_form = form.save(commit=False)
    #             formset = ProfileInlineFormset(
    #                 request.POST, request.FILES, instance=custom_form)
    #             if formset.is_valid():
    #                 custom_form.save()
    #                 formset.save()
    #                 return redirect('dashboard')

    #     return render(request, 'survey.html', {
    #         "pk": pk,
    #         "formset": formset,
    #     })
    # else:
    #     raise PermissionDenied
