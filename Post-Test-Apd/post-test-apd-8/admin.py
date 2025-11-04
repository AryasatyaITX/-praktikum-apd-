import os
from prettytable import PrettyTable
import inquirer
import data 
from colorama import Fore,Style



def clear():
    os.system('cls || clear')


def addparty():
    try:
        clear()
        print(data.line1)
        print("=== Tambah Anggota Party ===".center(50))
        print(data.line1)
        jumlah = int(input("Berapa anggota yang ingin ditambahkan? "))

        for i in range(jumlah):
            clear()
            print(f"\nAnggota ke-{i+1}")
            
            questions = [
                inquirer.Text('kelas', message="Class"),
                inquirer.Text('nama', message="Nama"),
                inquirer.Text('lv', message="Lv"),
                inquirer.Text('skill', message="Skill utama"),
                inquirer.Text('ras', message="Ras")
            ]
            answers = inquirer.prompt(questions)
            
            data.party[data.party_id] = {
                'kelas': answers['kelas'],
                'nama': answers['nama'],
                'lv': answers['lv'],
                'skill': answers['skill'],
                'ras': answers['ras']
            }
            print(f"{answers['nama']} berhasil ditambahkan ke party!")
            data.party_id += 1
        input("\nTekan Enter untuk kembali ke menu...")
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")


def readparty():
    try:
        clear()
        if len(data.party) == 0:
            raise IndexError("Belum ada data class.")
        else:
            print(data.line1)
            print("=== DAFTAR PARTY D&D ===".center(50))
            print(data.line1)
            
            table = PrettyTable()
            table.field_names = ["No", "Class", "Nama", "Lv", "Skill", "Ras"]

            table.align = "l"              
            table.align["Lv"] = "r"        
            table.hrules = 1               
            table.border = True            
            table.header = True            
            table.padding_width = 2        
            table.presets = "pretty"
            
            for key, member in data.party.items():
                table.add_row([
                    key,
                    member['kelas'],
                    member['nama'],
                    member['lv'],
                    member['skill'],
                    member['ras']
                ])
            
            print(table)
            print(data.line1)

    except IndexError as e:
        print(f"Terjadi kesalahan : {e}")

    input("\nTekan Enter untuk melanjutkan...")
    clear()


def update():
    clear()
    if len(data.party) == 0:
        print("Belum ada data untuk diupdate.")
    else:
        clear()
        readparty()
        try:
            print(data.line1)
            print("=== Update Anggota Party ===".center(50))
            print(data.line1)           
            ubah = int(input("\nPilih nomor yang ingin diupdate: "))
            if ubah in data.party:
                print("\nMasukkan Data Baru : ")
                
                questions = [
                    inquirer.Text('kelas', message="Class baru"),
                    inquirer.Text('nama', message="Nama baru"),
                    inquirer.Text('lv', message="Lv baru"),
                    inquirer.Text('skill', message="Skill baru"),
                    inquirer.Text('ras', message="Ras baru")
                ]
                answers = inquirer.prompt(questions)
                
                data.party[ubah]['kelas'] = answers['kelas']
                data.party[ubah]['nama'] = answers['nama']
                data.party[ubah]['lv'] = answers['lv']
                data.party[ubah]['skill'] = answers['skill']
                data.party[ubah]['ras'] = answers['ras']
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
    if len(data.party) == 0:
        print("Belum ada data untuk dihapus.")
    else:
        readparty()
        try:
            print(data.line1)
            print("\n=== Daftar Anggota Untuk Dihapus ===".center(50))
            print(data.line1)
            hapus = int(input("Pilih nomor yang ingin dihapus: "))
            if hapus in data.party:
                nama_hapus = data.party[hapus]['nama']
                
                questions = [
                    inquirer.List('alasan',
                                message="Pilih alasan penghapusan",
                                choices=['Meninggalkan Party', 'Gugur Dalam Pertempuran', 'Lainnya'])
                ]
                answers = inquirer.prompt(questions)

                if answers['alasan'] == 'Meninggalkan Party':
                    print(f"{nama_hapus} telah meninggalkan party.")
                elif answers['alasan'] == 'Gugur Dalam Pertempuran':
                    print(f"{nama_hapus} telah gugur dalam pertempuran.")
                else:
                    print(f"{nama_hapus} telah dikeluarkan dari party.")

                del data.party[hapus]
                
                input("\nTekan Enter untuk melanjutkan...")
                clear()
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")

    input("Tekan Enter untuk kembali ke menu...")
    clear()


def total_lv(party, key_list=None, index=0):
    clear()
    print(data.line1)
    print("=== Total Level Party ===".center(50))
    print(data.line1)

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

def midPrint(text, width, color=Fore.CYAN+Style.BRIGHT):
    return color + text.center(width) + Style.RESET_ALL


def adminmenu():
    while True:
        try:
            clear()
            print("=" * 50)
            print(midPrint("=== MENU ADMIN D&D ===", 50))
            print("=" * 50)

            questions = [
                inquirer.List('menu',
                            message="Pilih menu",
                            choices=[
                                '1. Tambah anggota',
                                '2. Lihat semua anggota',
                                '3. Update anggota',
                                '4. Hapus anggota',
                                '5. Total Level Party',
                                '6. Logout'
                            ])
            ]
            answers = inquirer.prompt(questions)
            pilih = int(answers['menu'][0])

            if pilih == 1:
                addparty()
            elif pilih == 2:
                readparty()
            elif pilih == 3:
                update()
            elif pilih == 4:
                delparty()
            elif pilih == 5:
                hasil = total_lv(data.party)
                print(f"\nTotal Level Party adalah: {hasil}")
                input("\nTekan Enter untuk kembali ke menu...")
            elif pilih == 6:
                clear()
                print(data.line1)
                print("Logout berhasil!".center(50))
                print(data.line1)
                input("Tekan Enter untuk kembali ke menu awal...")
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk kembali ke menu...")
        except ValueError:
            print("Input harus angka!")
            input("Tekan Enter untuk melanjutkan...")