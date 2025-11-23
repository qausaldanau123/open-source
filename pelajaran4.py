mahasiswa_list = []

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa {i+1}")
    nama = input("Nama   : ")
    umur = input("Umur   : ")
    alamat = input("Alamat : ")

    data = {
        "Nama": nama,
        "Umur": umur,
        "Alamat": alamat
    }

    mahasiswa_list.append(data)  # <- harus sejajar dengan 'data = {...}'

print("\n=== Data Mahasiswa ===")
for i, mhs in enumerate(mahasiswa_list, start=1):
    print(f"\nMahasiswa {i}")
    print(f"Nama   : {mhs['Nama']}")
    print(f"Umur   : {mhs['Umur']}")
    print(f"Alamat : {mhs['Alamat']}")
