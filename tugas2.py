
#(1)
#perbedaan list, tuple, set & dictionary
#List adalah tipe data kolektif yang bersifat mutable dan ordered, alias bisa diedit-edit dan bisa diakses via indeks.
#Tuple adalah tipe data kolektif yang bersifat immutable dan ordered. Dalam artian ia sama dengan list, hanya saja tuple tidak bisa diedit-edit.
#Sedangkan Set adalah tipe data kolektif yang bersifat unique, unordered, dan unchangeable di mana semua nilainya harus unik, dan ia tidak bisa diakses via indeks (karena tidak berurut), dan dia tidak bisa diedit-edit (akan tetapi bisa ditambah dan dihapus).
#Karena data dalam dictionary tidak berurutan maka kita tidak dapat mengakses data dengan urutan index.

    #kesimpulan
        #Jika anda ingin struktur data yang anda gunakan tidak dapat diubah-ubah, maka gunakanlah tuple.
        #Jika anda ingin data yang disimpan tidak ada yang sama, maka gunakanlah set.
        #Jika data ingin disimpan secara berurutan maka gunakanlah list.
        #Jika anda ingin mengakses data menggunakan key maka gunakanlah dictionary. Dictionary sering digunakan pada JSON.

#(2)

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print(a [1 : 5])

#(3)

b = [
    [5, 9, 8],
    [0, 0, 6]
    ]
print(b[1][1:3])

#4
c = [
    [5, 9, 8],
    [0, 0, 6],
    [5, 9, 10],
    [11, 0, 6]
    ]

print(c[2: ][0:])

#5
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

areas.pop(8)
areas.pop(8)

print(areas)

#6
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = S [0::2]

print(T)

#8
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe ["itali"] = "roma"
print(europe)

#9

print (10>5 and 2>3)

print(20<10 or 50>9)

print(not 10>20)

#10

A = int(input())
if A > 100000 :
    print("High")
elif A > 50000 :
    print("Medium")
elif A <= 50000 :
    print("low")

