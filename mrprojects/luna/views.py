from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt

#from luna.models import Models...

context = {}

def reset_context():
	global context
	context = {
		'page_title': '',
		#'django_version' : django.get_version()
	}

def index(request):
	reset_context()
	context['page_title'] = 'Modo Ouvir'
	return render(request, 'index.html', context)