from django.shortcuts import render
from django.http import HttpResponse


def helloPageView(requests) -> HttpResponse:
    return HttpResponse('Hello, World!!')
