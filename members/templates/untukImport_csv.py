import csv
from datetime import datetime
from members.models import Member

with open('order form-edited.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            tanggal = datetime.strptime(
                row['tanggal_lahir'], "%m/%d/%Y"
            ).date()
        except:
            tanggal = None

        Member.objects.create(
            nama_lengkap=row['nama_lengkap'],
            tanggal_lahir=tanggal,
            nomor_telepon=row['nomor_telepon'],
            sudah_baptis=row['sudah_baptis'].lower() == 'true'
        )

print("Import selesai ✅")
