import os
os.system('cls || clear')

users = {'admin': {'password': 'dungeon master', 'role': 'admin'}}
party = {}
line1 = '=' * 50
party_id = 1

print(line1)
print("SELAMAT DATANG DI DUNGEON AND DRAGONS!".center(50))
print(line1)
input("\nSilahkan tekan Enter untuk LOGIN!!!")

while True:
    os.system('cls || clear')
    print(line1)
    print("=== MENU LOGIN ===".center(50))
    print(line1)
    print("1. Login".center(50))
    print("2. Register".center(50))
    print("3. Keluar".center(50))
    print(line1)
    pilih = input("\nMasukkan pilihan akun : ")
    os.system('cls || clear')

    # LOGIN
    if pilih == '1':
        print(line1)
        print("=== LOGIN ===".center(50))
        print(line1)
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")

        role_user = None
        if username in users and users[username]['password'] == password:
            role_user = users[username]['role']

        # MENU ADMIN
        if role_user == 'admin':
            print(f"\nLogin berhasil! Selamat datang, {username} (Admin)")
            input("\nTekan Enter untuk masuk ke menu utama...")

            while True:
                os.system('cls || clear')
                print(line1)
                print("=== MENU ADMIN D&D ===".center(50))
                print(line1)
                print("1. Tambah anggota".center(50))
                print("2. Lihat semua anggota".center(50))
                print("3. Update anggota".center(50))
                print("4. Hapus anggota".center(50))
                print("5. Logout".center(50))
                print(line1)
                pilih_admin = input("Pilih menu : ")
                os.system('cls || clear')

                # CREATE
                if pilih_admin == '1':
                    os.system('cls || clear')
                    print(line1)
                    print("=== Tambah Anggota Party ===".center(50))
                    print(line1)
                    jumlah = int(input("Berapa anggota yang ingin ditambahkan? "))

                    for i in range(jumlah):
                        print(f"\nAnggota ke-{i+1}")
                        kelas = input("Class : ")
                        nama = input("Nama : ")
                        lv = input("Lv : ")
                        skill = input("Skill utama : ")
                        ras = input(" Ras : ")
                        party[party_id] = {
                            'kelas': kelas,
                            'nama': nama,
                            'lv': lv,
                            'skill': skill,
                            'ras': ras
                        }
                        print(f"{nama} berhasil ditambahkan ke party!")
                        party_id += 1

                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')

                # READ
                elif pilih_admin == '2':
                    os.system('cls || clear')
                    if len(party) == 0:
                        print("Belum ada data class.")
                    else:
                        print(line1)
                        print("=== DAFTAR PARTY D&D ===".center(50))
                        print(line1)
                        for key, member in party.items():
                            print(f"{key}. Class : {member['kelas']}")
                            print(f"   Nama : {member['nama']}")
                            print(f"   Lv   : {member['lv']}")
                            print(f"   Skill: {member['skill']}")
                            print(f"   ras  : {member['ras']}")
                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')

                # UPDATE
                elif pilih_admin == '3':
                    os.system('cls || clear')
                    if len(party) == 0:
                        print("Belum ada data untuk diupdate.")
                    else:
                        print(line1)
                        print("=== Update Anggota Party ===".center(50))
                        print(line1)
                        for key, member in party.items():
                            print(f"{key}. {member['kelas']} - {member['nama']}")
                        ubah = int(input("\nPilih nomor yang ingin diupdate: "))
                        if ubah in party:
                            print("\nMasukkan Data Baru : ")
                            party[ubah]['kelas'] = input("Class baru: ")
                            party[ubah]['nama'] = input("Nama baru: ")
                            party[ubah]['lv'] = input("Lv baru: ")
                            party[ubah]['skill'] = input("Skill baru: ")
                            party[ubah]['ras'] = input("Ras baru : ")
                            print("Data berhasil diupdate!")
                        else:
                            print("Nomor tidak valid.")
                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')

                # DELETE
                elif pilih_admin == '4':
                    os.system('cls || clear')
                    if len(party) == 0:
                        print("Belum ada data untuk dihapus.")
                    else:
                        print(line1)
                        print("\n===Daftar Anggota Untuk Dihapus===".center(50))
                        print(line1)
                        for key, member in party.items():
                            print(f"{key}. {member['kelas']} - {member['nama']}")
                        hapus = int(input("Pilih nomor yang ingin dihapus: "))
                        if hapus in party:
                            nama_hapus = party[hapus]['nama']
                            print("\nAlasan dihapus : ")
                            print("1. Meninggalkan Party")
                            print("2. Gugur Dalam Pertempuran")
                            alasan = input("Pilih alasan(1/2 :  ")

                            if alasan == '1':
                                print(f"\n{nama_hapus} telah meninggalkan party.")
                            elif alasan == '2':
                                print(f"\n{nama_hapus} telah gugur dalam pertempuran.")
                            else:
                                print(f"\n{nama_hapus} telah dikeluarkan dari party.")
                            del party[hapus]
                        else:
                            print("Nomor tidak valid.")
                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')

                elif pilih_admin == '5':
                    print("Logout berhasil.")
                    input("\nTekan Enter untuk kembali ke menu login...")
                    break

                else:
                    print("Pilihan tidak valid.")
                    input("\nTekan Enter untuk kembali ke menu...")

        # MENU USER
        elif role_user == 'user':
            karakter_user = {}
            karakter_id = 1
            print(f"\nLogin berhasil! Selamat datang, {username} (User)")
            input("\nTekan Enter untuk masuk ke menu utama...")

            while True:
                os.system('cls || clear')
                print(line1)
                print("=== MENU USER D&D ===".center(50))
                print(line1)
                print("1. Lihat anggota party".center(50))
                print("2. Buat karakter sendiri".center(50))
                print("3. Lihat karakter sendiri".center(50))
                print("4. Logout".center(50))
                print(line1)
                pilih_user = input("Pilih menu : ")
                os.system('cls || clear')
                
                #READ
                if pilih_user == '1':
                    os.system('cls || clear')
                    if len(party) == 0:
                        print("Belum ada data class.")
                    else:
                        print(line1)
                        print("=== DAFTAR PARTY D&D ===".center(50))
                        print(line1)
                        for key, member in party.items():
                            print(f"{key}. Class : {member['kelas']}")
                            print(f"   Nama  : {member['nama']}")
                            print(f"   Lv    : {member['lv']}")
                            print(f"   Skill : {member['skill']}")
                            print(f"   Ras   : {member['ras']}")
                        print('*' * 50)
                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')

                #CREATE
                elif pilih_user == '2':
                    os.system('cls || clear')
                    print(line1)
                    print("=== Buat Karakter Sendiri ===".center(50))
                    print(line1)
                    kelas = input("Class : ")
                    nama = input("Nama : ")
                    lv = input("Lv : ")
                    skill = input("Skill utama : ")
                    ras = input(" Ras : ")
                    karakter_user[karakter_id] = {
                        'kelas': kelas,
                        'nama': nama,
                        'lv': lv,
                        'skill': skill,
                        'ras': ras
                    }
                    print(f"\nKarakter {nama} berhasil dibuat!")
                    karakter_id += 1
                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')
                
                #READ
                elif pilih_user == '3':
                    os.system('cls || clear')
                    if len(karakter_user) == 0:
                        print("Belum ada karakter yang dibuat.")
                    else:
                        print(line1)
                        print("=== KARAKTER ===".center(50))
                        print(line1)
                        for key, karakter in karakter_user.items():
                            print(f"{key}. Class : {karakter['kelas']}")
                            print(f"   Nama  : {karakter['nama']}")
                            print(f"   Lv    : {karakter['lv']}")
                            print(f"   Skill : {karakter['skill']}")
                            print(f"   Ras   : {karakter['ras']}")
                            
                        print('*' * 50)
                    input("\nTekan Enter untuk kembali ke menu...")
                    os.system('cls || clear')

                elif pilih_user == '4':
                    print("Logout berhasil.")
                    input("\nTekan Enter untuk kembali ke menu login...")
                    break

                else:
                    print("Pilihan tidak valid.")
                    input("\nTekan Enter untuk kembali ke menu...")

        else:
            print("Login gagal. Username atau password salah.")
            input("\nTekan Enter untuk kembali ke menu...")

    #  REGISTER 
    elif pilih == '2':
        os.system('cls')
        print(line1)
        print("=== REGISTER AKUN ===".center(50))
        print(line1)
        Newusn = input("Buat Username : ")
        
        if Newusn in users:
            print(f"\nMaaf, username '{Newusn}' telah digunakan.")
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            Newpas = input("Buat Password : ")
            users[Newusn] = {'password': Newpas, 'role': 'user'}
            print(f"\nPengguna '{Newusn}' berhasil terdaftar!")
            input("\nTekan Enter untuk kembali ke menu...")
    elif pilih == '3':
        print("Keluar dari program. Terimakasih Adventures,Sampai jumpa lagi!")
        break

    else:
        print("Pilihan tidak valid.")
        input("\nTekan Enter untuk kembali ke menu...")