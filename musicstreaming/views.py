from django.http import Http404
from django.shortcuts import render
from .models import User, Music, Forkship


# Create your views here.
def index(request):
    return render(request, 'musicstreaming/index.html', {'worked': True})


def dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        uid = User.objects.filter(user_name=name)
        music_list = Forkship.objects.filter(user=uid).values()
        response = {'music_list': music_list}
        print response
        return render(request, 'musicstreaming/dashboard.html', response)
    raise Http404("Kurt's a fuck up, sorry")
