from django.shortcuts import render, redirect
from survey.models import Survey



# Create your views here.
def surveyhome(request):
    results=Survey.objects.all()
    context = {}
    return render(request, 'surveyhome.html', {"Survey":results})

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')

            survey.save()

def results(request):
    context = {}
    return render(request, 'results.html', context)

def vote(request):
    context = {}
    return render(request, 'vote.html', context)
