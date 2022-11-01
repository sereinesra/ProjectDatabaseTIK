from django.contrib import admin
from ft.models import Dosen, Tendik, Mahasiswa

# Register your models here.

class DosenFTAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']

class TendikFTAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']

class MahasiswaFTAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']
    search_fields = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']

admin.site.register(Dosen, DosenFTAdmin)
admin.site.register(Tendik, TendikFTAdmin)
admin.site.register(Mahasiswa, MahasiswaFTAdmin)