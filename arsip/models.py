from django.db import models
from django.conf import settings

# Create your models here.
class Umum(models.Model):
    KATEGORI = (
        ('Backup Aplikasi SAS', 'Backup Aplikasi SAS'),
        ('Backup Aplikasi Persediaan', 'Backup Aplikasi Persediaan'),
        ('Backup Aplikasi SIMAK BMN', 'Backup Aplikasi SIMAK BMN'),
        ('Backup Aplikasi GPP', 'Backup Aplikasi GPP'),
        ('Backup Aplikasi SAIBA', 'Backup Aplikasi SAIBA'),
        ('Laporan Kondisi Barang', 'Laporan Kondisi Barang'),
        ('Laporan Pengadaan Barang dan Jasa', 'Laporan Pengadaan Barang dan Jasa'),
        ('LPJ Perbendaharaan Pengeluaran', 'LPJ Perbendaharaan Pengeluaran'),
        ('Buku Kas Umum', 'Buku Kas Umum'),
        ('Buku Pembantu Pajak', 'Buku Pembantu Pajak'),
        ('Buku Besar Kas', 'Buku Besar Kas'),
        ('Berita Acara Rekonsiliasi e-Rekon', 'Berita Acara Rekonsiliasi e-Rekon'),
        ('Form Rencana Aksi', 'Form Rencana Aksi'),
    )
    nama = models.CharField(max_length=200, null=True)
    keterangan = models.CharField(max_length=200, null=True, blank=True)
    kategori = models.CharField(max_length=200, null=True, choices=KATEGORI)
    periode = models.DateField(null=True)
    upload = models.FileField(upload_to='file_upload/Umum/', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.upload.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nama

class Surat(models.Model):
    nomor = models.CharField(max_length=200,null=True)
    perihal = models.CharField(max_length=200,null=True)
    tanggal_surat = models.DateField(null=True)
    keterangan = models.TextField(null=True)
    upload = models.FileField(upload_to='file_upload/Surat/', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.upload.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.perihal

class Dipa(models.Model):
    uraian_dipa = models.CharField(max_length=200,null=True)
    periode = models.DateField(null=True)
    file_pok = models.FileField(upload_to='file_upload/Dipa/POK', null=True)
    file_adk = models.FileField(upload_to='file_upload/Dipa/ADK', null=True)
    file_dipa = models.FileField(upload_to='file_upload/Dipa/DIPA', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.file_pok.delete()
        self.file_adk.delete()
        self.file_dipa.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.uraian_dipa

class Spm(models.Model):
    nomor_spm = models.CharField(max_length=200,null=True)
    jenis_spm = models.CharField(max_length=200,null=True)
    tanggal_spm = models.DateField(null=True)
    nomor_sp2d = models.CharField(max_length=200,null=True)
    tanggal_sp2d = models.DateField(null=True)
    jumlah_potongan = models.IntegerField(null=True)
    jumlah_bersih = models.IntegerField(null=True)
    file_spm = models.FileField(upload_to='file_upload/SPM/SPM/', null=True)
    file_sp2d = models.FileField(upload_to='file_upload/SPM/SP2D/', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.file_spm.delete()
        self.file_sp2d.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nomor_spm

class Tup(models.Model):
    nomor = models.CharField(max_length=200,null=True)
    tanggal_surat = models.DateField(null=True)
    jumlah_tup = models.IntegerField(null=True)
    keterangan = models.TextField(null=True)
    upload = models.FileField(upload_to='file_upload/Surat/', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.upload.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nama

class Survei(models.Model):
    KATEGORI = (
        ('Kuesioner', 'Kuesioner'),
        ('Berita Acara Respon Rate', 'Berita Acara Respon Rate'),
        ('Laporan Kegiatan', 'Laporan Kegiatan'),
    )
    nama_survei = models.CharField(max_length=200, null=True)
    periode = models.DateField(null=True)
    penanggung_jawab = models.CharField(max_length=200, null=True)
    keterangan = models.CharField(max_length=200, null=True, blank=True)
    kategori = models.CharField(max_length=200, null=True, choices=KATEGORI)
    upload = models.FileField(upload_to='file_upload/Survei/', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.upload.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nama_survei

class DaftarSampel(models.Model):
    KATEGORI = (
        ('Daftar Sampel Blok Sensus', 'Daftar Sampel Blok Sensus'),
        ('Daftar Sampel Rumah Tangga/Non, Usaha/Non', 'Daftar Sampel Rumah Tangga/Non, Usaha/Non'),
        ('Laporan Kegiatan', 'Laporan Kegiatan'),
    )
    nama_survei = models.CharField(max_length=200, null=True)
    periode = models.DateField(null=True)
    wilayah = models.CharField(max_length=200, null=True)
    penanggung_jawab = models.CharField(max_length=200, null=True)
    keterangan = models.CharField(max_length=200, null=True, blank=True)
    kategori = models.CharField(max_length=200, null=True, choices=KATEGORI)
    upload = models.FileField(upload_to='file_upload/Daftar_Sampel/', null=True)
    date_created = models.DateField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        self.upload.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nama_survei
