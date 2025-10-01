USN = "arya"
PW = "066"

print("=== LOGIN ACCOUNT ===")
user = input("Masukkan Username : ")
pwd = input("Masukkan Password : ")

if user != USN and pwd == PW:
    print("Username salah!")
    exit()
elif user == USN and pwd != PW:
    print("Password salah!")
    exit()
elif user != USN and pwd != PW:
    print("Username dan password salah!")
    exit()

else:    
    print("Login berhasil! selamat datang", USN)
    
    # === MENU KALKULATOR ===
    print("=== KALKULATOR  ===")
    print("1. Konversi Panjang")
    print("2. Konversi Massa")
    print("3. Konversi Suhu")
    print("4. Konversi Waktu")
    print("5. Konversi Mata Uang")

    pil = input("Pilih kalkulator: ")

    # Konversi Panjang
    if pil == "1":
        print("Konversi panjang ke meter")
        print("1. Kaki(feet) -> meter")
        print("2. Kilometer -> meter")
        print("3. Centimeter -> meter")
        con = input("Pilih jenis konversi: ")
        nilai = float(input("Masukkan nilai: "))

        if con == "1":
            hasil = nilai * 0.3048
            print("Hasil meternya adalah:", hasil)
        elif con == "2":
            hasil = nilai * 1000
            print("Hasil meternya adalah:", hasil)           
        elif con == "3":
            hasil = nilai / 100
            print("Hasil meternya adalah:", hasil)
        else:
            print("Pilihan konversi meter tidak ada!")
      
    # Konversi Massa
    elif pil == "2":
        print(" Konversi Massa ke Kilogram ")
        print("1. Pon (pound) -> Kilogram")
        print("2. Ton -> Kilogram")
        print("3. Gram -> Kilogram")
        print("4. Ons -> Kilogram")
        print("5. Dekagram -> Kilogram")
        con = input("Pilih jenis konversi: ")
        nilai = float(input("Masukkan nilai: "))

        if con == "1":
            hasil = nilai * 0.45
            print("Kilogram:", hasil)
        elif con == "2":
            hasil = nilai * 1000
            print("Kilogram:", hasil)        
        elif con == "3":
            hasil = nilai / 1000
            print("Kilogram:", hasil)
        elif con == "4":
            hasil = nilai * 0.1
            print("Kilogram:", hasil)
        elif con == "5":
            hasil = nilai / 100
            print("Kilogram:", hasil)
        else:
            print("Pilihan konversi massa tidak ada!")

    # Konversi Suhu
    elif pil == "3":
        print(" Konversi Suhu ke Kelvin ")
        print("1. Celsius -> Kelvin")
        print("2. Fahrenheit -> Kelvin")
        print("3. Reamur -> Kelvin")
        con = input("Pilih jenis konversi: ")
        nilai = float(input("Masukkan nilai: "))
        if con == "1":
            hasil = nilai + 273.15
            print("hasil konversi ke kelvin:", hasil)           
        elif con == "2":
            hasil = (nilai - 32) * 5/9 + 273.15
            print("hasil konversi ke kelvin:", hasil)
        elif con == "3":
            hasil = (nilai * 5/4) + 273.15
            print("hasil konversi ke kelvin:", hasil)            
        else:
            print("Pilihan konversi suhu tidak ada!")

    # Konversi Waktu
    elif pil == "4":
        print(" Konversi Waktu ke Detik ")
        print("1. Menit -> Detik")
        print("2. Jam -> Detik")
        con = input("Pilih jenis konversi: ")
        nilai = float(input("Masukkan nilai: "))

        if con == "1":
            hasil = nilai * 60
            print("hasil detiknya:", hasil)          
        elif con == "2":
            hasil = nilai * 3600
            print("hasil detiknya:", hasil)           
        else:
            print("Pilihan konversi waktu tidak ada!")

    # Konversi Mata Uang
    elif pil == "5":
        print("Konversi Mata Uang")
        print("1. Rupiah -> Dollar")
        print("2. Dollar -> Rupiah")
        print("3. Rupiah -> Yen")
        print("4. Yen -> Rupiah")
        print("5. Rupiah -> Won")
        print("6. Won -> Rupiah")
        con = input("Pilih jenis konversi: ")
        nilai = float(input("Masukkan jumlah uang: "))

        # Kurs uang 
        kursusd = 16750.0    
        kursyen = 112.26    
        kurswon = 11.88 

        if con == "1":
            hasil = nilai / kursusd
            print("Hasil mata uangnya $:", hasil)
        elif con == "2":
            hasil = nilai * kursusd
            print("Hasil mata uangnya Rp:", hasil)                      
        elif con == "3":
            hasil = nilai / kursyen
            print("Hasil mata uangnya ¥:", hasil)            
        elif con == "4":
            hasil = nilai * kursyen
            print("Hasil mata uangnya Rp:", hasil)            
        elif con == "5":
            hasil = nilai / kurswon
            print("Hasil mata uangnya ₩:", hasil)           
        elif con == "6":
            hasil = nilai * kurswon 
            print("Hasil mata uangnya Rp:", hasil)           
        else:
            print("Pilihan konversi mata uang tidak ada!")

    else:
        print("Pilihan kalkulator tidak ada!")
