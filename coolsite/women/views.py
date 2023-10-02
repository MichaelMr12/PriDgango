from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    print(request.GET)

    return HttpResponse('страница приложения women/')



def about(request):
    return redirect('spisok_pri', '12')
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_id(request, number_student):
    if int(number_student) > 30:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> ПРИ 201 </h1> <p>Студент под номером {number_student} </p>')


def categories(request, cat):
    return HttpResponse(f'<h1> Ссылка {cat} </h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена проверьте адрес!! </h1>')


def page500(exception):
    return HttpResponseNotFound(f'<h1> Ошибка!! {exception} </h1>')


def page403(request, exception):
    return HttpResponseNotFound(f'<h1> Не пущу!! {exception} </h1>')
