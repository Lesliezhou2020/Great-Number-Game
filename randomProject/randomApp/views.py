from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['guess'] = None

    return render(request, "index.html")


def guess(request):
    request.session['guess'] = int(request.POST['guess'])
    print(request.session['guess'])
    print(request.session['number'])
    return redirect('/')


def reset(request):
    request.session['number'] = random.randint(1, 100)
    request.session['guess'] = None
    return redirect('/')