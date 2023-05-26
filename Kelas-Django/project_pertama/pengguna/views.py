from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#tanpa template html
# def pengguna(request):
#     return HttpResponse("haloo semua")

# menjalankan view dengan template html
# def pengguna(request):
#     template = loader.get_template('pengguna.html')
#     return HttpResponse(template.render())

#DATA DI DATABASE SUDAH ADA
from pengguna.models import Pengguna

def pengguna(request):
    data_pengguna = Pengguna.objects.all().values()[2] #contoh yg diambil adalah data ke 2
    template = loader.get_template('pengguna.html')
    return HttpResponse(template.render(data_pengguna, request))