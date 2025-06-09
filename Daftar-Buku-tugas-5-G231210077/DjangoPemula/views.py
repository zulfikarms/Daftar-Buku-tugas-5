from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  context = {
    'title':
    'Daftar Buku ',
    'all_buku': [
      [
        "Belajar Pemrograman Python",
        2015
      ], [
        "HTML Untuk Pemula",
        2014
      ], [
        "Membuat Aplikasi Sederhana menggunakan Framework Django",
        2020
      ]
    ]
  }
  return render(request, 'index.html', context)
