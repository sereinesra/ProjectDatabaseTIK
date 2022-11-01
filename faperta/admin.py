from django.contrib import admin
from faperta.models import Dosen, Tendik, Mahasiswa

# Register your models here.

class DosenFapertaAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']

class TendikFapertaAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']

class MahasiswaFapertaAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']
    search_fields = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']

admin.site.register(Dosen, DosenFapertaAdmin)
admin.site.register(Tendik, TendikFapertaAdmin)
admin.site.register(Mahasiswa, MahasiswaFapertaAdmin)