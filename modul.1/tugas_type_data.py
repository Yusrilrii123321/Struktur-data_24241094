# Meminta pengguna memasukkan jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Dictionary untuk menyimpan data
data_mahasiswa = {}

# Perulangan untuk input data setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")
    nim = input("Masukkan NIM: ")         # str
    nama = input("Masukkan Nama: ")       # str
    jurusan = input("masukkan jurusan: ")    # str


    # Simpan dalam dictionary
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan,
    
    }

# Menampilkan hasil
print("\n=== Daftar Data Mahasiswa dan Nilai Rata-Rata ===")
for nim, info in data_mahasiswa.items():
    nama = info["nama"]
    jurusan = info["jurusan"]
 

    print(f"\nNIM       : {nim}")
    print(f"Nama      : {nama}")
    print(f"jurusan   : {jurusan}")
 
