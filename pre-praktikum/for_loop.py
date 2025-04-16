# PENGULANGAN
# for-loop
'''
    for-loop digunakan untuk penngulangan
    yang diketahui jumlah pengulanganya 
    counted-loop

    syntax :
    for kondisi :
        aksi 1 - bagian dari loop
        aksi 2 - bukan baguan dari loop

'''
a = 0 
a += 1
print(a)
a+= 1
print(a)
a += 1 
print(a)
a += 1

# boros line code

# perulangan menggunakan list
angka = [0,1,5,7,10]
for i in angka :
    print(f"i saat ini -> {i}")
print("ini akhir dari loop")

# penggulangan menggunakan range 
angka_range = range(5) # diulang 5 kali

for i in angka_range:
 print(f"i saat ini -> {i}")
print("ini akhir dari 2/n")

angka2_range =(1,10) # diulang 9 kali
print(list,{angka2_range})
for i in angka_range:
 print(f"i saat ini -> {i}")
print("ini akhir dari 3/n")

# pengulangan menggunakan string
string = "mandalika"
print(string)

for i in string :
 print(f"i saat ini ->{i}")
print("ini akhir dari loop 4\n")

