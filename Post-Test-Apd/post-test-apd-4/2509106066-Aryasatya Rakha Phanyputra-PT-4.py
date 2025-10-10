

USN = "arya"
PW = "066"


while True:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
   
    if username == "" or password == "":
        print("Username dan Password tidak boleh kosong! Harus diisi!")
        continue
   
    if username == USN and password == PW:
        print("Login berhasil!\n")
        break
    elif username == USN and password != PW:
        print("Password salah!")
    elif username != USN and password == PW:
        print("Username salah!")
    else:
        print("Username dan Password salah!")


totalA_plus = totalA_minus = 0
totalB_plus = totalB_minus = 0
totalAB_plus = totalAB_minus = 0
totalO_plus = totalO_minus = 0


while True:
    golongan = input("Masukkan Golongan Darah (A/B/AB/O): ").upper()


    if golongan == "":
        print("Golongan darah tidak boleh kosong!")
        continue


    if golongan == "A":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "":
            print("Rhesus tidak boleh kosong!")
            continue
        elif rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            totalA_plus += kantong * 500
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            totalA_minus += kantong * 500
        else:
            print("Rhesus hanya boleh + atau -!")
            continue


    elif golongan == "B":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "":
            print("Rhesus tidak boleh kosong!")
            continue
        elif rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            totalB_plus += kantong * 500
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            totalB_minus += kantong * 500
        else:
            print("Rhesus hanya boleh + atau -!")
            continue


    elif golongan == "AB":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "":
            print("Rhesus tidak boleh kosong!")
            continue
        elif rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            totalAB_plus += kantong * 500
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            totalAB_minus += kantong * 500
        else:
            print("Rhesus hanya boleh + atau -!")
            continue


    elif golongan == "O":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "":
            print("Rhesus tidak boleh kosong!")
            continue
        elif rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            totalO_plus += kantong * 500
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            totalO_minus += kantong * 500
        else:
            print("Rhesus hanya boleh + atau -!")
            continue


    else:
        print("Golongan darah hanya boleh A, B, AB, atau O!")
        continue


    ulang = input("Apakah Anda ingin input lagi (Y/T)? ").upper()
    while ulang != "Y" and ulang != "T":
        print("Jawaban hanya boleh Y atau T!")
        ulang = input("Apakah Anda ingin input lagi (Y/T)? ").upper()


    if ulang == "T":
        break


print("=== RINGKASAN DONOR DARAH ===")
print("A+ :", totalA_plus, "ml")
print("A- :", totalA_minus, "ml")
print("B+ :", totalB_plus, "ml")
print("B- :", totalB_minus, "ml")
print("AB+:", totalAB_plus, "ml")
print("AB-:", totalAB_minus, "ml")
print("O+ :", totalO_plus, "ml")
print("O- :", totalO_minus, "ml")


print("\nTerima kasih telah berpartisipasi dalam donor darah!")






