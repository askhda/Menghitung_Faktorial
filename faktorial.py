print ('Program untuk menghitung nilai faktorial dari suatu bilangan')

first =  1
hasil = 1

nilai_dihitung = input("Masukkan angka yang ingin dihitung ")

#Menghitung tanpa menggunakan fungsi
angka = int(nilai_dihitung)
while(angka >= first):
    hasil=hasil*angka
    angka=angka-1

#Menghitung menggunakan fungsi dengan perulangan while    
def  while_faktorial(nilai):
    angka = int(nilai)
    hasil = 1
    
    while(angka>= first):
        hasil = hasil*angka
        angka = angka-1
    return hasil

#Menghitung menggunakan fungsi dengan perulangan for
def for_faktorial(nilai):
    angka = int(nilai)
    hasil = 1
    for angka in range (angka, 0, -1):
        hasil = hasil*angka
    return hasil
    
print ("Faktorial dari " + str(nilai_dihitung) + " adalah " + str(hasil))
print ("Faktorial dari " + str(nilai_dihitung) + " adalah " + str(while_faktorial(nilai_dihitung)))
print ("Faktorial dari " + str(nilai_dihitung) + " adalah " + str(for_faktorial(nilai_dihitung)))
