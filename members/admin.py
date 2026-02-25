from django.contrib import admin
from .models import Member, Keluarga, Perpuluhan


#admin.site.register(Perpuluhan)
#admin.site.register(Keluarga)
# Register your models here.

class MemberInline(admin.TabularInline):
    model = Member
    extra = 0

class KeluargaAdmin(admin.ModelAdmin):
    inlines = [MemberInline]



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'jenis_kelamin', 'keluarga', 'sudah_baptis')


@admin.register(Keluarga)
class KeluargaAdmin(admin.ModelAdmin):
    list_display = ('nama_keluarga', 'alamat')


@admin.register(Perpuluhan)
class PerpuluhanAdmin(admin.ModelAdmin):
    list_display = ('member', 'tanggal', 'jumlah', 'metode_pembayaran')
    list_filter = ('tanggal', 'metode_pembayaran')
    search_fields = ('member__nama_lengkap',)