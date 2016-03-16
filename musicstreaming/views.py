from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'musicstreaming/index.html', {'worked': True})


def dashboard(request):

    return render(request, 'musicstreaming/dashboard.html', {})
