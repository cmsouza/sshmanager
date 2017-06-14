from django.shortcuts import render


# Create your views here.
def host_list(request):
    return render(request, 'home/home.html', {})
