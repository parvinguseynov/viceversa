from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse('This is about page')


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    text_split = user_text.split()
    len_element = len(text_split)
    print(len_element)
    reversed_text = user_text[::-1]

    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'len': len_element})