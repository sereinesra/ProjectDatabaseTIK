from django.contrib import admin
from fh.models import Dosen, Tendik, Mahasiswa

# Register your models here.

class DosenFHAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']

class TendikFHAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']

class MahasiswaFHAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']
    search_fields = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']

admin.site.register(Dosen, DosenFHAdmin)
admin.site.register(Tendik, TendikFHAdmin)
admin.site.register(Mahasiswa, MahasiswaFHAdmin)