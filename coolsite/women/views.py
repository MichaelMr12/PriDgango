from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
    print(request.GET)
    return HttpResponse('страница приложения women/')


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_id(request, number_student):
    return HttpResponse(f'<h1> ПРИ 201 </h1> <p>Студент под номером {number_student} </p>')


def categories(request, cat):
    return HttpResponse(f'<h1> Ссылка {cat} </h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена проверьте адрес!! </h1>')