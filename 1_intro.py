# print('hello world')

# # print utk mencetak sesuatu

# nama = 'dita' #string
# umur = '23' #int tapi kasih '' biar jadi str
# pekerjaan = 'pelajar'

# print('my name is ' + nama)
# print('I am ' + umur + ' years old')
# print(pekerjaan)

# print(type(nama)) # buat tau typenya int/str dll

# # fungsi input
# nama = input('What is your name?: ')
# print('My name is ' + nama) #kalo pake simple + jnlup tambah spasi
# print('My name is', nama, 'umur saya', 23) #pake koma gapake spasi

# print (2+1)
# print (2-1)
# print (3+2)
# print (4/2) #2.0 datatype float
# print (4//2) #2 -> int
# print (5%2) #modulo sisa pembagian
# print (2**3) # pangkat bisa jg pake pow
# print(pow(8,2))

# # mengganti data types
# x = '10'
# print(x) # masih str
# y = int(x) # udh jd int
# print(y)

# a = 35
# a_str = str(a)
# print(a_str)
# print(type(a_str))

# # mau bikin hasil 12.0 dari data berikut
# c = '2' #int
# print(float(c)+10)

# #kuis
# nama = input("Nama anda: ")
# umur = input("Umur: ") # input itu selalu str typenya
# print ("Halo nama saya", nama, "umur saya 5 tahun ke depan adalah", int(umur) + 5)

## recall
# usiaDita = 23
# usiaDita = 23 +5 #usia dita 5 thn ke dpn
# print(usiaDita) # cara pertama

# usiaDita += 5 #cara kedua
# print(usiaDita)

# # import math cara 1
# import math
# print(math.pi)
# print(math.fabs(-4.6))
# print(math.pow(2,5))
# print(math.sqrt(16))
# print(math.ceil(2.4))
# print(math.floor(3.7))
# print(round(4.837489, 3))

# #atau
# from math import pi, fabs, sqrt # per function

# #STRING
x = 'Halo dunia lain'
# print(x)
# print(type(x))
# print(len(x)) # banyak karaktr
# print(x.index('a')) # di index brp startnya dari 0123456
# print(x.split()) # di pisah per kata
# print(x.split('o')) # di split pas ktmu O
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print('halo apakabar'.capitalize())
# print(x.replace('dunia', 'cewe'))

# #kalo ada single quote biar ga dianggep string
# print("halo ini hari jum'at") #doublequote
# print('''ini "jum'at"''') #triple quote

# #Indexing 
# print (x[0]) # index ke 0 yaitu H
# print (x[3])
# print (x[-1])
# print (x[-15])
#  #slicing
# print(x[0:4]) # slicing harus +1 dari index
# print(x[5:]) # sampe habis
# print(x[x.index('d'):])
# print (x[:x.index('l')])
# print(x[:-4])
# # start:stop:step
# print(x[0:15:2])
# print(x[0:15:1])
# print(x[::-1])

# # Boolean
# a = 1
# b = 2
# c = 1
# print(a == c)


print(' ')

# HOMEWORk
# SOLVE1
x = 4
y = 3
z = 2
w= (((x+(y*z))/(x*y))**z)
print(w)

print(' ')

# SOLVE2
angka = input('Silahkan masukkan angka berapapun: ')
print('Kuadra angka',angka,'adalah',int(angka)**2)

print(' ')

#SOLVE3
print('485 hari sama dengan')
tahun = 485//360
bulan = (485%360)//30
minggu = ((485-(tahun*360)-(bulan*30))//7)
hari = (485-(tahun*360)-(bulan*30)-(minggu*7))

print(tahun, ' tahun, ', bulan, ' bulan,', minggu, ' minggu, dan ', hari, ' hari.')

print(' ')

#cara 2
a = input ('jumlah hari: ')
a_int = int(a)
tahun = a_int // 360
bulan = (a_int % 360) // 30
minggu = (a_int % 30) // 7
hari = (a_int % 30) % 7

print(tahun, bulan, minggu, hari)

print(' ')

#SOLVE 4
usia_andi = x
usia_budi = y
x = 49 - y
x = 0.4 * y
y = 49 / 1.4
x = 49 - 35
print('usia andi 2 tahun ke depan adalah ', int(x) + 2)
print('usia Budi 2 tahun ke depan adalah ', int(y) + 2)

print(' ')

#SOLVE 5
print('Nama "Rahmadita Lailqadrisha Sakina" memiliki jumlah karakter "a" sebanyak...')
x = 'Rahmadita Lailqadrisha Sakina'
print (x.count('a'))

# Cara 2
kata = input ('Masukkan kata: ').lower()
find = input (f'Huruf yg mo diitung dari {kata}: ').lower()
katabaru = kata.replace(find, '')
print(f"huruf {find} di kata {kata} ada {len(kata) - len(katabaru)} buah")



print(' ')

# SOLVE 6
import math
waktu_brkt = 9
jarak_ab = 120
a = 60
b = 40
wkt = jarak_ab/(a+b)
jam = math.floor(wkt)
menit = int((wkt*60)%60)

print("Mobil A dan B bertabrakan pada pukul ", waktu_brkt+jam,'.',menit, ' WIB')
