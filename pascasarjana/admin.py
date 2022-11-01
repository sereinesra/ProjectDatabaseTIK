from django.contrib import admin
from pascasarjana.models import Dosen, Tendik, Mahasiswa

# Register your models here.

class DosenPSAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']

class TendikPSAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']

class MahasiswaPSAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']
    search_fields = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']

admin.site.register(Dosen, DosenPSAdmin)
admin.site.register(Tendik, TendikPSAdmin)
admin.site.register(Mahasiswa, MahasiswaPSAdmin)