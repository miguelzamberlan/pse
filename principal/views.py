from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def principal(request):

    return render(request, 'principal.html')