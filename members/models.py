from django.db import models



# Create your models here.
class Keluarga(models.Model):
    nama_keluarga = models.CharField(max_length=200)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_keluarga

class Member(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=10)
    tanggal_lahir = models.DateField()
    #alamat = models.CharField(max_length=225)
    nomor_telepon = models.CharField(max_length=15)
    #nama_keluarga = models.CharField(max_length=100)
    sudah_baptis = models.BooleanField()
    sudah_sidi = models.BooleanField()
    pelayanan_diikuti = models.CharField(max_length=100, blank=True)
    ibadah_sering_diikuti = models.CharField(max_length=100, blank=True)
    keluarga = models.ForeignKey(Keluarga, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nama_lengkap

class Perpuluhan(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name = 'perpuluhan')
    tanggal = models.DateField()
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.nama_lengkap} - {self.jumlah}"

