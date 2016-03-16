from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'musicstreaming/index.html', {'worked': True})


def dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        print name
    return render(request, 'musicstreaming/dashboard.html', {})
