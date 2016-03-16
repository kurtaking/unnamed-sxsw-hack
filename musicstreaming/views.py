from django.http import Http404
from django.shortcuts import render
from .models import User, Music, Track, Forkship


# Create your views here.
def index(request):
    return render(request, 'musicstreaming/index.html', {'worked': True})


def dashboard(request):
    if request.method == 'GET':
        path_list = request.path.split('/')
        # user = path_list[2]
        # user_id = User.objects.filter(user_name=user)[0].user_id
        project = path_list[3]
        music_id = Music.objects.filter(music_name=project)[0].music_id
        # fs = Forkship.objects.filter(user=user_id, music=music_id)
        tracks = Track.objects.filter(music_id=music_id)
        track_list = []
        for track in tracks:
            print track.track_id
            track_list.append(track.track_id)
        response = {'tracks': track_list}
        return render(request, 'musicstreaming/project_dashboard.html',
                      response)
        # print request.path.split('/')
    if request.method == 'POST':
        name = request.POST.get('username')
        uid = User.objects.filter(user_name=name)
        music_list = Forkship.objects.filter(user=uid).values()
        resp_list = []
        for music in music_list:
            m = Music.objects.filter(music_id=music['music_id'])
            print m[0].music_name
            resp_list.append(m[0].music_name)
        response = {'music_list': {'name': name, 'list': resp_list}}
        print response
        return render(request, 'musicstreaming/dashboard.html', response)
    raise Http404("Kurt's a fuck up, sorry")
