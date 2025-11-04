import os
import inquirer
from prettytable import PrettyTable
from autentikasi import LOGIN,REGISTER
from admin import adminmenu
from user import usermenu
from data import line1
from colorama import Fore,Style

def clear():
    os.system('cls || clear')


def menuwal():
    while True:
        clear()
        print(line1)
        print(Fore.CYAN + Style.BRIGHT + "=== MENU LOGIN ===".center(50) + Style.RESET_ALL)
        print(line1)

        table = PrettyTable()
        table.field_names = ["No", "=== MENU LOGIN ==="]
        table.add_row(["1", "Login (admin/user)"])
        table.add_row(["2", "Register Akun User"])
        table.add_row(["3", "Keluar"])

        print(Fore.YELLOW + "\nDaftar Menu:" + Style.RESET_ALL)
        print(Fore.GREEN + str(table) + Style.RESET_ALL)
        


        pertanyaan = [
            inquirer.List(
                'pilihan',
                message="Pilih menu",
                choices=['1. Login(admin/user)', '2. Register Akun User', '3. Keluar'],
            ),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        pilih = jawaban['pilihan'][0]

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