
nama = "Andi"
nilai = 85

# Membuat dan mengisi file
with open("laporan.txt", "w") as file:
    file.write("LAPORAN NILAI\n")
    file.write("------------------\n")
    file.write(f"Nama  : {nama}\n")
    file.write(f"Nilai : {nilai}\n")

# Menampilkan pesan
print("Laporan berhasil dibuat!")
