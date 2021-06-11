from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django import forms


class BackupAplikasiList(ListView):
    model = BackupAplikasi
    template_name = 'arsip/backup_aplikasi/backup_aplikasi_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class BackupAplikasiCreate(CreateView):
    model = BackupAplikasi
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/backup_aplikasi/backup_aplikasi_form.html'

    success_url = reverse_lazy('backup_aplikasi_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BackupAplikasiCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class BackupAplikasiDetail(DetailView):
    model = BackupAplikasi
    template_name = 'arsip/backup_aplikasi/backup_aplikasi_detail.html'


class BackupAplikasiUpdate(UpdateView):
    model = BackupAplikasi
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/backup_aplikasi/backup_aplikasi_form.html'
    success_url = reverse_lazy('backup_aplikasi_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class BackupAplikasiDelete(DeleteView):
    model = BackupAplikasi
    template_name = 'arsip/backup_aplikasi/backup_aplikasi_confirm_delete.html'
    success_url = reverse_lazy('backup_aplikasi_list')


def BackupAplikasiApprove(request, pk):
    laporan_bmn = LaporanBmn.objects.get(pk=pk)
    laporan_bmn.approval = 1
    laporan_bmn.save()
    return redirect('laporan_bmn_list')

#
class LaporanBmnList(ListView):
    model = LaporanBmn
    template_name = 'arsip/laporan_bmn/laporan_bmn_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class LaporanBmnCreate(CreateView):
    model = LaporanBmn
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/laporan_bmn/laporan_bmn_form.html'

    success_url = reverse_lazy('laporan_bmn_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(LaporanBmnCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class LaporanBmnDetail(DetailView):
    model = LaporanBmn
    template_name = 'arsip/laporan_bmn/laporan_bmn_detail.html'


class LaporanBmnUpdate(UpdateView):
    model = LaporanBmn
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/laporan_bmn/laporan_bmn_form.html'
    success_url = reverse_lazy('laporan_bmn_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class LaporanBmnDelete(DeleteView):
    model = LaporanBmn
    template_name = 'arsip/laporan_bmn/laporan_bmn_confirm_delete.html'
    success_url = reverse_lazy('laporan_bmn_list')


def LaporanBmnApprove(request, pk):
    laporan_bmn = LaporanBmn.objects.get(pk=pk)
    laporan_bmn.approval = 1
    laporan_bmn.save()
    return redirect('laporan_bmn_list')


#
class LaporanKinerjaList(ListView):
    model = LaporanKinerja
    template_name = 'arsip/laporan_kinerja/laporan_kinerja_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class LaporanKinerjaCreate(CreateView):
    model = LaporanKinerja
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/laporan_kinerja/laporan_kinerja_form.html'

    success_url = reverse_lazy('laporan_kinerja_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(LaporanKinerjaCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class LaporanKinerjaDetail(DetailView):
    model = LaporanKinerja
    template_name = 'arsip/laporan_kinerja/laporan_kinerja_detail.html'


class LaporanKinerjaUpdate(UpdateView):
    model = LaporanKinerja
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/laporan_kinerja/laporan_kinerja_form.html'
    success_url = reverse_lazy('laporan_kinerja_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class LaporanKinerjaDelete(DeleteView):
    model = LaporanKinerja
    template_name = 'arsip/laporan_kinerja/laporan_kinerja_confirm_delete.html'
    success_url = reverse_lazy('laporan_kinerja_list')


def LaporanKinerjaApprove(request, pk):
    laporan_kinerja = LaporanKinerja.objects.get(pk=pk)
    laporan_kinerja.approval = 1
    laporan_kinerja.save()
    return redirect('laporan_kinerja_list')

# SKPA View


class SkpaList(ListView):
    model = Surat
    template_name = 'arsip/skpa/skpa_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class SkpaCreate(CreateView):
    model = Surat
    fields = ['nomor', 'perihal', 'tanggal_surat', 'upload']
    template_name = 'arsip/skpa/skpa_form.html'

    success_url = reverse_lazy('skpa_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(SkpaCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal_surat'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class SkpaDetail(DetailView):
    model = Surat
    template_name = 'arsip/skpa/skpa_detail.html'


class SkpaUpdate(UpdateView):
    model = Surat
    fields = ['nomor', 'perihal', 'tanggal_surat', 'upload']
    template_name = 'arsip/skpa/skpa_form.html'
    success_url = reverse_lazy('skpa_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal_surat'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class SkpaDelete(DeleteView):
    model = Surat
    template_name = 'arsip/skpa/skpa_confirm_delete.html'
    success_url = reverse_lazy('skpa_list')


def SkpaApprove(request, pk):
    skpa = Surat.objects.get(pk=pk)
    skpa.approval = 1
    skpa.save()
    return redirect('skpa_list')

# DIPA View


class DipaList(ListView):
    model = Dipa
    template_name = 'arsip/dipa/dipa_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class DipaCreate(CreateView):
    model = Dipa
    fields = ['uraian_dipa', 'tanggal', 'file_pok', 'file_adk', 'file_dipa']
    template_name = 'arsip/dipa/dipa_form.html'

    success_url = reverse_lazy('dipa_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(DipaCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class DipaDetail(DetailView):
    model = Dipa
    template_name = 'arsip/dipa/dipa_detail.html'


class DipaUpdate(UpdateView):
    model = Dipa
    fields = ['uraian_dipa', 'tanggal', 'file_pok', 'file_adk', 'file_dipa']
    template_name = 'arsip/dipa/dipa_form.html'
    success_url = reverse_lazy('dipa_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class DipaDelete(DeleteView):
    model = Dipa
    template_name = 'arsip/dipa/dipa_confirm_delete.html'
    success_url = reverse_lazy('dipa_list')


def DipaApprove(request, pk):
    dipa = Dipa.objects.get(pk=pk)
    dipa.approval = 1
    dipa.save()
    return redirect('dipa_list')

# SPM View


class SpmList(ListView):
    model = Spm
    template_name = 'arsip/spm/spm_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class SpmCreate(CreateView):
    model = Spm
    fields = ['nomor_spm', 'jenis_spm', 'tanggal_spm', 'nomor_sp2d',
              'tanggal_sp2d', 'jumlah_potongan', 'jumlah_bersih', 'file_spm', 'file_sp2d']
    template_name = 'arsip/spm/spm_form.html'

    success_url = reverse_lazy('spm_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(SpmCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal_spm'].widget = forms.DateInput(
            attrs={'type': 'date'})
        form.fields['tanggal_sp2d'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class SpmDetail(DetailView):
    model = Spm
    template_name = 'arsip/spm/spm_detail.html'


class SpmUpdate(UpdateView):
    model = Spm
    fields = ['nomor_spm', 'jenis_spm', 'tanggal_spm', 'nomor_sp2d',
              'tanggal_sp2d', 'jumlah_potongan', 'jumlah_bersih', 'file_spm', 'file_sp2d']
    template_name = 'arsip/spm/spm_form.html'
    success_url = reverse_lazy('spm_list')


class SpmDelete(DeleteView):
    model = Spm
    template_name = 'arsip/spm/spm_confirm_delete.html'
    success_url = reverse_lazy('spm_list')


def SpmApprove(request, pk):
    spm = Spm.objects.get(pk=pk)
    spm.approval = 1
    spm.save()
    return redirect('spm_list')

# TUP View


class TupList(ListView):
    model = Tup
    template_name = 'arsip/tup/tup_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class TupCreate(CreateView):
    model = Tup
    fields = ['kategori', 'nomor', 'keterangan',
              'tanggal_surat', 'jumlah_tup', 'upload']
    template_name = 'arsip/tup/tup_form.html'

    success_url = reverse_lazy('tup_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TupCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal_surat'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class TupDetail(DetailView):
    model = Tup
    template_name = 'arsip/tup/tup_detail.html'


class TupUpdate(UpdateView):
    model = Tup
    fields = ['kategori', 'nomor', 'keterangan',
              'tanggal_surat', 'jumlah_tup', 'upload']
    template_name = 'arsip/tup/tup_form.html'
    success_url = reverse_lazy('tup_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal_surat'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class TupDelete(DeleteView):
    model = Tup
    template_name = 'arsip/tup/tup_confirm_delete.html'
    success_url = reverse_lazy('tup_list')


def TupApprove(request, pk):
    tup = Tup.objects.get(pk=pk)
    tup.approval = 1
    tup.save()
    return redirect('tup_list')

# Survei View


class SurveiList(ListView):
    model = Survei
    template_name = 'arsip/survei/survei_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class SurveiCreate(CreateView):
    model = Survei
    fields = ['kategori', 'nama_survei', 'periode',
              'penanggung_jawab', 'keterangan', 'upload']
    template_name = 'arsip/survei/survei_form.html'

    success_url = reverse_lazy('survei_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(SurveiCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class SurveiDetail(DetailView):
    model = Survei
    template_name = 'arsip/survei/survei_detail.html'


class SurveiUpdate(UpdateView):
    model = Survei
    fields = ['kategori', 'nama_survei', 'periode',
              'penanggung_jawab', 'keterangan', 'upload']
    template_name = 'arsip/survei/survei_form.html'
    success_url = reverse_lazy('survei_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class SurveiDelete(DeleteView):
    model = Survei
    template_name = 'arsip/daftar-sampel/daftarsampel_confirm_delete.html'
    success_url = reverse_lazy('survei_list')


def SurveiApprove(request, pk):
    survei = Survei.objects.get(pk=pk)
    survei.approval = 1
    survei.save()
    return redirect('survei_list')

# Daftar Sampel View


class DaftarSampelList(ListView):
    model = DaftarSampel
    template_name = 'arsip/daftar-sampel/daftarsampel_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class DaftarSampelCreate(CreateView):
    model = DaftarSampel
    fields = ['kategori', 'nama_survei', 'periode',
              'wilayah', 'penanggung_jawab', 'keterangan', 'upload']
    template_name = 'arsip/daftar-sampel/daftarsampel_form.html'

    success_url = reverse_lazy('daftar_sampel_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(DaftarSampelCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class DaftarSampelDetail(DetailView):
    model = DaftarSampel
    template_name = 'arsip/daftar-sampel/daftarsampel_detail.html'


class DaftarSampelUpdate(UpdateView):
    model = DaftarSampel
    fields = ['kategori', 'nama_survei', 'periode',
              'wilayah', 'penanggung_jawab', 'keterangan', 'upload']
    template_name = 'arsip/daftar-sampel/daftarsampel_form.html'
    success_url = reverse_lazy('daftar_sampel_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class DaftarSampelDelete(DeleteView):
    model = DaftarSampel
    template_name = 'arsip/survei/survei_confirm_delete.html'
    success_url = reverse_lazy('daftar_sampel_list')


def DaftarSampelApprove(request, pk):
    daftar_sampel = DaftarSampel.objects.get(pk=pk)
    daftar_sampel.approval = 1
    daftar_sampel.save()
    return redirect('daftar_sampel_list')
