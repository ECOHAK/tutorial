from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from firstapp.models import Curriculum


def index1(request):
    return HttpResponse('<h1>Hello</h1>')

def index2(request):
    return HttpResponse('<hi>Hi</h1>')

def main(request):
    return HttpResponse('<h1>Main</h1>')

def show(request):
    curriculum = Curriculum.objects.all()
    html = ''
    for c in curriculum:
        html += c.name + '<br>'

    #Ctrl + / : 주석
    #return HttpResponse(html)
    return render(
        request,
        'firstapp/show.html',
        {
            'data': html,
            'curriculum':curriculum
        }
    )


