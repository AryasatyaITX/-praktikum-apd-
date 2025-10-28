import os


users = {
    "admin": {'password': 'dungeon master', 'role': 'admin'}
}

party = {}
party_id = 1
karakter_user = {}
karakterid = 1
line1 = '=' * 50


def clear():
    os.system('cls || clear')


def LOGIN():
    clear()
    print(line1)
    print("=== LOGIN ===".center(50))
    print(line1)
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if username in users and users[username]['password'] == password:
        clear()
        print(line1)
        print(f"Login berhasil! Selamat datang, {username} ({users[username]['role'].capitalize()})")
        print(line1)
        input("Tekan Enter untuk melanjutkan ke menu...")
        return {
            "username": username,
            "password": users[username]['password'],
            "role": users[username]['role']
        }

    print("Login gagal. Username atau password salah.")
    input("Tekan Enter untuk melanjutkan...")
    return None



def REGISTER():
    try:
        clear()
        print(line1)
        print("=== REGISTER AKUN USER ===".center(50))
        print(line1)
        Newusn = input("Buat username : ")

        if Newusn in users:
            print(f"\nMaaf, username '{Newusn}' telah digunakan.")
            input("Tekan Enter untuk melanjutkan...")
            return

        Newpas = input("Buat password : ")
        users[Newusn] = {'password': Newpas, 'role': 'user'}
        print(f"\nPengguna '{Newusn}' berhasil terdaftar!")
        input("\nTekan Enter untuk kembali ke menu...")
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi : {str(e)}")
        input("Tekan Enter untuk melanjutkan...")


def addparty():
    global party_id
    try:
        clear()
        print(line1)
        print("=== Tambah Anggota Party ===".center(50))
        print(line1)
        jumlah = int(input("Berapa anggota yang ingin ditambahkan? "))

        for i in range(jumlah):
            clear()
            print(f"\nAnggota ke-{i+1}")
            kelas = input("Class : ")
            nama = input("Nama : ")
            lv = input("Lv : ")
            skill = input("Skill utama : ")
            ras = input("Ras : ")
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
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")


def readparty():
    try:
        clear()
        if len(party) == 0:
            raise IndexError("Belum ada data class.")
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
                print(line1)

    except IndexError as e:
        print(f"Terjadi kesalahan : {e}")

    input("\nTekan Enter untuk melanjutkan...")
    clear()


def update():
    clear()
    if len(party) == 0:
        print("Belum ada data untuk diupdate.")
    else:
        clear()
        readparty()
        try:
            print(line1)
            print("=== Update Anggota Party ===".center(50))
            print(line1)           
            ubah = int(input("\nPilih nomor yang ingin diupdate: "))
            if ubah in party:
                print("\nMasukkan Data Baru : ")
                party[ubah]['kelas'] = input("Class baru : ")
                party[ubah]['nama'] = input("Nama baru : ")
                party[ubah]['lv'] = input("Lv baru : ")
                party[ubah]['skill'] = input("Skill baru : ")
                party[ubah]['ras'] = input("Ras baru : ")
                print("\nData berhasil diupdate!")
                clear()
            else:
                print("Nomor tidak valid!")

        except ValueError:
            print("Input harus berupa angka!")
    input("Tekan Enter untuk kembali ke menu...")
    clear()


def delparty():
    clear()
    if len(party) == 0:
        print("Belum ada data untuk dihapus.")
    else:
        readparty()
        try:
            print(line1)
            print("\n=== Daftar Anggota Untuk Dihapus ===".center(50))
            print(line1)
            hapus = int(input("Pilih nomor yang ingin dihapus: "))
            if hapus in party:
                nama_hapus = party[hapus]['nama']
                print("\nAlasan dihapus : ")
                print("1. Meninggalkan Party")
                print("2. Gugur Dalam Pertempuran")
                alasan = input("Pilih alasan (1/2): ")

                if alasan == '1':
                    print(f"{nama_hapus} telah meninggalkan party.")
                elif alasan == '2':
                    print(f"{nama_hapus} telah gugur dalam pertempuran.")
                else:
                    print(f"{nama_hapus} telah dikeluarkan dari party.")

                del party[hapus]
                clear()
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")

    input("Tekan Enter untuk kembali ke menu...")
    clear()


def total_lv(party, key_list=None, index=0):
    clear()
    print(line1)
    print("=== Total Level Party ===".center(50))
    print(line1)

    if len(party) == 0:
        return 0

    if key_list is None:
        key_list = list(party.keys())

    if index >= len(key_list):
        return 0

    try:
        lv_skrg = int(party[key_list[index]]['lv'])
    except ValueError:
        print(f"Level {party[key_list[index]]['nama']} tidak valid, dilewati!")
        lv_skrg = 0

    return lv_skrg + total_lv(party, key_list, index + 1)
    


def addchar():
    global karakterid
    try:
        clear()
        print(line1)
        print("=== Buat Karakter Sendiri ===".center(50))
        print(line1)

        kelas = input("Class : ")
        nama = input("Nama : ")
        lv = input("Lv : ")
        skill = input("Skill utama : ")
        ras = input("Ras : ")

        if not all([kelas, nama, lv, skill, ras]):
            raise Exception("Semua field harus diisi.")

        karakter_user[karakterid] = {
            'kelas': kelas,
            'nama': nama,
            'lv': lv,
            'skill': skill,
            'ras': ras
        }
        print(f"\nKarakter {nama} berhasil dibuat!")
        karakterid += 1

    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
    input("\nTekan Enter untuk kembali ke menu...")


def readchar():
    try:
        clear()
        if len(karakter_user) == 0:
            raise IndexError("Belum ada karakter yang dibuat.")
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
                print(line1)
    except IndexError as e:
        print(f"Terjadi kesalahan : {e}")

    input("\nTekan Enter untuk kembali ke menu...")
    clear()


def adminmenu():
    while True:
        try:
            clear()
            print(line1)
            print("=== MENU ADMIN D&D ===".center(50))
            print(line1)
            print("1. Tambah anggota".center(50))
            print("2. Lihat semua anggota".center(50))
            print("3. Update anggota".center(50))
            print("4. Hapus anggota".center(50))
            print("5. Total Level Party".center(50))
            print("6. Logout".center(50))
            print(line1)
            pilih = int(input("Pilih menu : "))

            if pilih == 1:
                addparty()
            elif pilih == 2:
                readparty()
            elif pilih == 3:
                update()
            elif pilih == 4:
                delparty()
            elif pilih == 5:
                hasil = total_lv(party)
                print(f"\nTotal Level Party adalah: {hasil}")
                input("\nTekan Enter untuk kembali ke menu...")
            elif pilih == 6:
                clear()
                print(line1)
                print("Logout berhasil!".center(50))
                print(line1)
                input("Tekan Enter untuk kembali ke menu awal...")
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk kembali ke menu...")
        except ValueError:
            print("Input harus angka!")
            input("Tekan Enter untuk melanjutkan...")


def usermenu(username):
    while True:
        try:
            clear()
            print(line1)
            print(f"=== MENU USER D&D ({username}) ===".center(50))
            print(line1)
            print("1. Lihat anggota party".center(50))
            print("2. Buat karakter sendiri".center(50))
            print("3. Lihat karakter sendiri".center(50))
            print("4. Logout".center(50))
            print(line1)
            pilih = int(input("Pilih menu : "))

            if pilih == 1:
                readparty()
            elif pilih == 2:
                addchar()
            elif pilih == 3:
                readchar()
            elif pilih == 4:
                clear()
                print(line1)
                print("Logout berhasil!".center(50))
                print(line1)
                input("Tekan Enter untuk kembali ke menu awal...")
                break
            else:
                print("Pilihan tidak valid.")
                input("\nTekan Enter untuk kembali ke menu...")
        except ValueError:
            print("Input harus angka!")
            input("Tekan Enter untuk melanjutkan...")


def menuwal():
    while True:
        clear()
        print(line1)
        print("=== MENU LOGIN ===".center(50))
        print(line1)
        print("1. Login(admin/user)".center(50))
        print("2. Register Akun User".center(50))
        print("3. Logout".center(50))
        print(line1)
        pilih = input("\nMasukkan pilihan akun : ")

        if pilih == '1':
            user_login = LOGIN()
            if user_login:
                if user_login['role'] == 'admin':
                    adminmenu()
                else:
                    usermenu(user_login['username'])
        elif pilih == '2':
            REGISTER()
        elif pilih == '3':
            clear()
            print("Keluar dari program. Terima kasih Adventurer, sampai jumpa lagi!")
            break
        else:
            print("Pilihan tidak valid.")
            input("\nTekan Enter untuk kembali ke menu...")


menuwal()