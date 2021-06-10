from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django import forms


# Umum View
class UmumList(ListView):
    model = Umum
    template_name = 'arsip/umum/umum_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class UmumCreate(CreateView):
    model = Umum
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/umum/umum_form.html'

    success_url = reverse_lazy('umum_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UmumCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class UmumDetail(DetailView):
    model = Umum
    template_name = 'arsip/umum/umum_detail.html'


class UmumUpdate(UpdateView):
    model = Umum
    fields = ['kategori', 'periode', 'keterangan', 'upload']
    template_name = 'arsip/umum/umum_form.html'
    success_url = reverse_lazy('umum_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['periode'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class UmumDelete(DeleteView):
    model = Umum
    success_url = reverse_lazy('umum_list')


def UmumApprove(request, pk):
    umum = Umum.objects.get(pk=pk)
    umum.approval = 1
    umum.save()
    return redirect('umum_list')

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
    fields = ['nomor', 'kategori', 'keterangan', 'tanggal_surat', 'jumlah_tup', 'upload']
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
    fields = ['nomor', 'kategori', 'keterangan', 'tanggal_surat', 'jumlah_tup', 'upload']
    template_name = 'arsip/tup/tup_form.html'
    success_url = reverse_lazy('tup_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tanggal_surat'].widget = forms.DateInput(
            attrs={'type': 'date'})
        return form


class TupDelete(DeleteView):
    model = Tup
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
    fields = ['nama_survei', 'kategori', 'periode',
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
    fields = ['nama_survei', 'kategori', 'periode',
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
    fields = ['nama_survei', 'kategori', 'periode',
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
    fields = ['nama_survei', 'kategori', 'periode',
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
    success_url = reverse_lazy('daftar_sampel_list')


def DaftarSampelApprove(request, pk):
    daftar_sampel = DaftarSampel.objects.get(pk=pk)
    daftar_sampel.approval = 1
    daftar_sampel.save()
    return redirect('daftar_sampel_list')
