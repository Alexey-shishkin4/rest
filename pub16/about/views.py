from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect


def about(request):
    template = 'about.html'
    context = {}
    return render(request, template, context)