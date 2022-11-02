from django.shortcuts import render
from fisip.forms import FormDosen, FormTendik, FormMahasiswa
from django.shortcuts import render, redirect
from django.contrib import messages
from fisip.models import Dosen, Tendik, Mahasiswa
# Create your views here.
def indexfh(request):
    judul = "Sejarah"
    tentang = "Fakultas Hukum Universitas Sultan Ageng Tirtayasa berdiri tahun 1981, tepatnya pada tanggal 1 Oktober 1981 dengan status sebagai STIH Serang yang bertempat di Kresidenan Banten, Jl. K.H. Sam’un dan merupakan embrio lahirnya Universitas Sultan Ageng Tirtayasa Banten. Mulai tahun 1984, STIH Serang di integrasi sesuai dengan SK Mendikbud No. 0596/0/1984, menjadi Fakultas Hukum Universitas Sultan Ageng Tirtayasa yang bertempat di Jl. Raya Jakarta KM. 4 Pakupatan – Serang. Fakultas Hukum pada tahun 1994 memperoleh status terdaftar berdasarkan SK Mendikbud No. 0597/0/1984. Pada tahun 1994 Fakultas Hukum kembali memperoleh status penetapan terdaftar kembali berdasarkan SK Ditjen Pendidikan Tinggi No. 059/Dikti/Kep./1994. Pada tahun 2000 Fakultas Hukum memperoleh status terakreditasi dengan peringkat B, berdasarkan SK BAN-PT No. 19/BAN-PT/AK-IV/VIII/2000, dengan adanya SK Akreditasi tersebut maka Fakultas Hukum dapat menyelenggarakan proses pembelajaran secara mandiri. Pada tahun 2001 status Fakultas Hukum menjadi Fakultas Hukum dari Universitas Sultan Ageng Tirtayasa Banten dengan Status Negeri, berdasarkan Kepres No. 32/2001, hingga saat ini dan beralamat di Jl. Raya Jakarta KM. 4 Pakupatan–Serang. Saat ini  fakultas Hukum terakreditasi peringkat B berdasarkan SK. No. 186/SK/BAN-PT/Ak-SURV/S/VI/2014 tertanggal 28 Juni 2014."
    
    books = Dosen.objects.all()
    tendiks = Tendik.objects.all()
    students = Mahasiswa.objects.all()
    konteks = {
        'title' : judul,
        'penjelasan' : tentang,
        'books' : books,
        'tendiks' : tendiks,
        'students' : students,
    }
    return render(request, 'fh.html', konteks)
 
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