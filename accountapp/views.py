from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('input_text')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        # data_list = NewModel.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!'})
        # return render(request, 'accountapp/hello_world.html', context={'text': temp})
        # return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})
        # return HttpResponseRedirect('accountapp:hello_world')
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        # return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})