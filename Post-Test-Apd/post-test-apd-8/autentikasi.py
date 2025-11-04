import os
import inquirer
from data import users, line1


def clear():
    os.system('cls || clear')


def LOGIN():
    clear()
    print(line1)
    print("=== LOGIN ===".center(50))
    print(line1)
    
    questions = [
        inquirer.Text('username', message="Masukkan username"),
        inquirer.Password('password', message="Masukkan password")
    ]
    answers = inquirer.prompt(questions)
    
    username = answers['username']
    password = answers['password']

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
        
        questions = [
            inquirer.Text('username', message="Buat username"),
            inquirer.Password('password', message="Buat password")
        ]
        answers = inquirer.prompt(questions)
        
        Newusn = answers['username']
        Newpas = answers['password']

        if Newusn in users:
            print(f"\nMaaf, username '{Newusn}' telah digunakan.")
            input("Tekan Enter untuk melanjutkan...")
            return

        users[Newusn] = {'password': Newpas, 'role': 'user'}
        print(f"\nPengguna '{Newusn}' berhasil terdaftar!")
        input("\nTekan Enter untuk kembali ke menu...")
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi : {str(e)}")
        input("Tekan Enter untuk melanjutkan...")