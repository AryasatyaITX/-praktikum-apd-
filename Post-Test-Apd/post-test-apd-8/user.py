import os
from prettytable import PrettyTable
import inquirer
from colorama import Fore,Style
import data
from admin import readparty


def clear():
    os.system('cls || clear')


def addchar():
    try:
        clear()
        print(data.line1)
        print("=== Buat Karakter Sendiri ===".center(50))
        print(data.line1)

        questions = [
            inquirer.Text('kelas', message="Class"),
            inquirer.Text('nama', message="Nama"),
            inquirer.Text('lv', message="Lv"),
            inquirer.Text('skill', message="Skill utama"),
            inquirer.Text('ras', message="Ras")
        ]
        answers = inquirer.prompt(questions)

        if not all([answers['kelas'], answers['nama'], answers['lv'], answers['skill'], answers['ras']]):
            raise Exception("Semua field harus diisi.")

        data.karakter_user[data.karakterid] = {
            'kelas': answers['kelas'],
            'nama': answers['nama'],
            'lv': answers['lv'],
            'skill': answers['skill'],
            'ras': answers['ras']
        }
        print(f"\nKarakter {answers['nama']} berhasil dibuat!")
        data.karakterid += 1

    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
    input("\nTekan Enter untuk kembali ke menu...")


def readchar():
    try:
        clear()
        if len(data.karakter_user) == 0:
            raise IndexError("Belum ada karakter yang dibuat.")
        else:
            print(data.line1)
            print("=== KARAKTER ===".center(50))
            print(data.line1)
            
            table = PrettyTable()
            table.field_names = ["No", "Class", "Nama", "Lv", "Skill", "Ras"]
            
            for key, karakter in data.karakter_user.items():
                table.add_row([
                    key,
                    karakter['kelas'],
                    karakter['nama'],
                    karakter['lv'],
                    karakter['skill'],
                    karakter['ras']
                ])
            
            print(table)
            print(data.line1)
            
    except IndexError as e:
        print(f"Terjadi kesalahan : {e}")

    input("\nTekan Enter untuk kembali ke menu...")
    clear()

def midPrint(text, width, color=Fore.CYAN+Style.BRIGHT):
    return color + text.center(width) + Style.RESET_ALL


def usermenu(username):
    while True:
        try:
            clear()
            print(Fore.CYAN + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)
            print(midPrint(f"=== MENU USER D&D ({username}) ===", 50))
            print(Fore.CYAN + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)
            
            questions = [
                inquirer.List('menu',
                            message="Pilih menu",
                            choices=[
                                '1. Lihat anggota party',
                                '2. Buat karakter sendiri',
                                '3. Lihat karakter sendiri',
                                '4. Logout'
                            ])
            ]
            answers = inquirer.prompt(questions)
            pilih = int(answers['menu'][0])

            if pilih == 1:
                readparty()
            elif pilih == 2:
                addchar()
            elif pilih == 3:
                readchar()
            elif pilih == 4:
                clear()
                print(data.line1)
                print("Logout berhasil!".center(50))
                print(data.line1)
                input("Tekan Enter untuk kembali ke menu awal...")
                break
            else:
                print("Pilihan tidak valid.")
                input("\nTekan Enter untuk kembali ke menu...")
        except ValueError:
            print("Input harus angka!")
            input("Tekan Enter untuk melanjutkan...")