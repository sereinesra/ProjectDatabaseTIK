from django.contrib import admin
from fkip.models import Dosen, Tendik, Mahasiswa

# Register your models here.
class DosenFKIPAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi', 'Alamat']

class TendikFKIPAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']
    search_fields = ['NIP', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Unit', 'Alamat']

class MahasiswaFKIPAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']
    search_fields = ['NIM', 'Nama', 'TanggalLahir', 'Foto', 'Email', 'Fakultas', 'Prodi']

admin.site.register(Dosen, DosenFKIPAdmin)
admin.site.register(Tendik, TendikFKIPAdmin)
admin.site.register(Mahasiswa, MahasiswaFKIPAdmin)