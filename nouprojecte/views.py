from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return HttpResponse("Hola, això és la primera vista de l'enquesta.")
