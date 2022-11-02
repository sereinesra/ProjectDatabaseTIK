from django.contrib import admin
from django.urls import path
from fkip.views import index
from faperta.views import *
from feb.views import indexfeb
from fh.views import indexfh
from fisip.views import indexfisip
from pascasarjana.views import indexpascasarjana
from ft.views import indexft
from fk.views import indexfk
from profil.views import indexprofil
from about.views import indexabout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', index),
    path('faperta/', indexfaperta),
    path('tambah-dosen/', tambah_Dosen, name='tambah_Dosen'),
    path('feb/', indexfeb),
    path('fh/', indexfh),
    path('fisip/', indexfisip),
    path('pascasarjana/', indexpascasarjana),
    path('ft/', indexft),
    path('fk/', indexfk),
    path('profil/', indexprofil),
    path('about/', indexabout),
    path('tambah-tendik/', tambah_Tendik,name='tambah_Tendik'),
    path('tambah-mahasiswa/', tambah_Mahasiswa, name='tambah_Mahasiswa'),
    path('Dosen/ubah/<int:id_Dosen>', ubah_Dosen, name='ubah_Dosen'),
    path('Dosen/hapus/<int:id_Dosen>', hapus_Dosen, name='hapus_Dosen'),
    path('Tendik/ubah/<int:id_Tendik>', ubah_Tendik, name='ubah_Tendik'),
    path('Tendik/hapus/<int:id_Tendik>', hapus_Tendik, name='hapus_Tendik'),
    path('Mahasiswa/ubah/<int:id_Mahasiswa>', ubah_Mahasiswa, name='ubah_Mahasiswa'),
    path('Mahasiswa/hapus/<int:id_Mahasiswa>', hapus_Mahasiswa, name='hapus_Mahasiswa'),
]
