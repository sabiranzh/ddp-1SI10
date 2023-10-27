Kendaraan = ["Mobil", "Sedan", "Toyota", 1500]
print(Kendaraan)

Kendaraan.insert(2, "Putih")
Kendaraan.insert(3, 4)
Kendaraan.insert(4,"130Juta")
print(Kendaraan)

Kendaraan.remove("Sedan")
print(Kendaraan)

pilihan = input("Pilih Opsi:")
match pilihan:
    case"1":
        s = int(input("masukan sisi:"))
        persegi = s*s
        print("luas persegi", persegi)
    case"2":
        phi=3.14
        r=int(input("masukan jari jari:"))
        lingkaran=phi*r*r
        print("luas lingkaran",lingkaran)
    case"3":
        l=1/2
        a=int(input("masukan alas:"))
        t=int(input("masukan tinggi:"))
        segitiga=l*a*t
        print("luas segitiga",segitiga)
    case _:
        print("Pilihan tidak tersedia")