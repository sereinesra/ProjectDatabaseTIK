from django.shortcuts import render
from fkip.forms import FormDosen, FormTendik, FormMahasiswa
from django.shortcuts import render, redirect
from django.contrib import messages
from fkip.models import Dosen, Tendik, Mahasiswa
# Create your views here.

def hapus_dosen(request, id_dosen):
    dosen = dosen.objects.filter(id=id_dosen)
    dosen.delete()

    messages.success(request, "Data berhasil dihapus")

    return redirect('dosen')

def ubah_dosen(request, id_dosen):
    dosen = dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah-dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }    

    return render(request, template, konteks)

def index(request):
    books = Dosen.objects.all()
    tendiks = Tendik.objects.all()
    students = Mahasiswa.objects.all()
    konteks = {
        'books' : books,
        'tendiks' : tendiks,
        'students' : students,
    }
    return render(request, 'fkip.html')

def tambah_Dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan
            }

            return render (request, 'tambah-dosen.html', konteks)
    else: 
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_Tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }

            return render (request, 'tambah-tendik.html', konteks)
    else: 
        form = FormTendik()

    konteks = {
        'form': form
    }

    return render(request, 'tambah-tendik.html', konteks)

def tambah_Mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }

            return render (request, 'tambah-mahasiswa.html', konteks)
    else: 
        form = FormMahasiswa()

    konteks = {
        'form': form
    }

    return render(request, 'tambah-mahasiswa.html', konteks)
