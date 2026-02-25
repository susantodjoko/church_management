#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime
from django.db.models import Sum
from .models import Member, Keluarga, Perpuluhan

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "mymember": mymember,
        "riwayat": mymember.perpuluhan.all(),
    }
    return HttpResponse(template.render(context, request))

def detail_keluarga(request, id):
    keluarga = Keluarga.objects.get(id=id)
    members = keluarga.member_set.all()

    context = {
        "keluarga": keluarga,
        "members": members,
    }
    return render(request, 'detail_keluarga.html', context)

def dasboard(request):
    now = datetime.now()

    total_members = Member.objects.count()
    total_keluarga = Keluarga.objects.count()
    total_baptis = Member.objects.filter(sudah_baptis=True).count()

    total_perpuluhan_bulan = Perpuluhan.objects.filter(tanggal__month=now.month, tanggal__year=now.year).aggregate(total=Sum('jumlah'))['total'] or 0
    total_perpuluhan_all = Perpuluhan.objects.aggregate(total=Sum('jumlah'))['total'] or 0

    context = {
        'total_members': total_members,
        'total_keluarga': total_keluarga,
        'total_perpuluhan_bulan': total_perpuluhan_bulan,
        'total_perpuluhan_all': total_perpuluhan_all,
    }
    return render(request, 'dashboard.html', context)

def detail_member(request, id):
    mymember = Member.objects.get(id=id)
    riwayat = mymember.perpuluhan.all()
    total_perpuluhan = riwayat.aggregate(total=Sum('jumlah'))['total'] or 0

    context = {
        'mymember': mymember,
        'riwayat': riwayat,
        'total_perpuluhan': total_perpuluhan,
    }
    return render(request, 'detail.html', context)