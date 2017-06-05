from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def config_file(request):
	return JsonResponse({'foo': 'bar'})
