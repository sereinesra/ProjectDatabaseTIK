from django.shortcuts import render
from fh.forms import FormDosen, FormTendik, FormMahasiswa
from django.shortcuts import render, redirect
from django.contrib import messages
from fh.models import Dosen, Tendik, Mahasiswa
# Create your views here.
def indexfisip(request):

    books = Dosen.objects.all()
    tendiks = Tendik.objects.all()
    students = Mahasiswa.objects.all()
    konteks = {
        'books' : books,
        'tendiks' : tendiks,
        'students' : students,
    }
    return render(request, 'fisip.html', konteks)
 
def hapus_Dosen(request, id_Dosen):
    dosen = Dosen.objects.filter(id=id_Dosen)
    dosen.delete()

    messages.success(request, "Data berhasil dihapus")

    return redirect('Dosen')

def hapus_Tendik(request, id_Tendik):
    tendik = Tendik.objects.filter(id=id_Tendik)
    tendik.delete()

    messages.success(request, "Data berhasil dihapus")

    return redirect('Tendik')

def hapus_Mahasiswa(request, id_Mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_Mahasiswa)
    mahasiswa.delete()

    messages.success(request, "Data berhasil dihapus")

    return redirect('Mahasiswa')

def ubah_Dosen(request, id_Dosen):
    dosen = Dosen.objects.get(id=id_Dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah_Dosen', id_Dosen=id_Dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }    

    return render(request, template, konteks)

def ubah_Tendik(request, id_Tendik):
    tendik = Tendik.objects.get(id=id_Tendik)
    template = 'ubah-tendik.html'
    if request.POST:
        form = FormTendik(request.POST, instance=tendik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah_tendik', id_Tendik=id_Tendik)
    else:
        form = FormTendik(instance=tendik)
        konteks = {
            'form':form,
            'tendik':tendik,
        }    

    return render(request, template, konteks)

def ubah_Mahasiswa(request, id_Mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_Mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah_mahasiswa', id_Mahasiswa=id_Mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form':form,
            'mahasiswa':mahasiswa,
        }    

    return render(request, template, konteks)

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