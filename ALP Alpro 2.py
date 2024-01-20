# Simple Task Management App in Python

from datetime import datetime

# Bold text 
class TextStyle:
    BOLD = '\033[1m'
    END = '\033[0m'

#Character stats
character_stats = {'poin': 0, 'level': 1, 'nyawa': 3}

# User data storage
users = {}

# Task data storage
tasks = []

# Function to display the welcome message
def welcome_questlist():
    welcome_text = """
=========================================================
  Selamat Datang di Aplikasi QuestList! 🚀🔍
=========================================================

QuestList bukan hanya Task Manager biasa, ini adalah
simulasi kehidupan nyata versi digitalmu sendiri..

Dalam dunia QuestList, setiap pencapaian adalah kemenangan,
dan setiap tugas adalah tantangan yang menanti untuk
dijelajahi. Kamu bukan sekadar menyelesaikan tugas,
tapi meraih prestasi dalam sebuah perjalanan seru.

Mulailah dengan menetapkan quest, selesaikan tugas,
dan raih reward yang menantimu. Tantang dirimu sendiri
dan tingkatkan level karaktermu!

Selamat berpetualang di dunia QuestList! 🌟
=========================================================
"""
    print(welcome_text)

# Function for user login
def login():
    username = input("Masukkan username anda: ")
    password = input("Masukkan password anda: ")

    if username in users and users[username]['password'] == password:
        print("\nLogin berhasil!")
        return True
    else:
        print("Anda belum registrasi, harap registrasi terlebih dahulu.")
        return False

# Function for user registration
def register():
    username = input("Masukkan username anda: ")

    if username not in users:
        email = input("Masukkan email anda: ")
        password = input("Masukkan password anda: ")
        users[username] = {'email': email, 'password': password}
        print("Registrasi berhasil!")
        return True
    else:
        print("User telah registrasi! Harap login")
        return False

# Function to display the home page
def home_page():
    print("\nHome Page")
    print(f"{TextStyle.BOLD}Statistik Karakter: Poin - {character_stats['poin']} , Level - {character_stats['level']}, Nyawa - {character_stats['nyawa']}{TextStyle.END}")

    # Menampilkan daftar tugas yang belum selesai
    incomplete_tasks = [task for task in tasks if task['status'] == 'belum selesai']

    if incomplete_tasks:
        print("\nDaftar Tugas Belum Selesai:")
        for i, task in enumerate(incomplete_tasks, 1):
            print(f"{i}. {task['name']} - Deadline: {task['deadline']}, Difficulty: {difficulty_to_string(task['difficulty'])}, Poin: {task['points']}")
    else:
        print("\nBelum ada tugas.")

    print("\nOpsi:")
    print("1. Tambahkan tugas")
    print("2. Akumulasi poin")
    print("3. Hapus tugas")
    print("4. Keluar")

# Function to add a task
def add_task():
    name = input("Masukkan nama tugas: ")

    while True:
        try:
            deadline_str = input("Masukkan deadline tugas (Tanggal-Bulan-Tahun): ")
            deadline = datetime.strptime(deadline_str, "%d-%m-%Y")
            break
        except ValueError:
            print("Format tanggal tidak valid! Coba lagi.")
    
    print("Pilih tingkat kesulitan:")
    print("1. Mudah")
    print("2. Sedang")
    print("3. Sulit")

    while True:
        try:
            difficulty= int(input("Masukkan nomor tingkat kesulitan: "))
            if 1 <= difficulty <= 3:
                break
            else:
                print("Pilihan tidak valid! Harap masukkan angka antara 1 dan 3.")
        except ValueError:
            print("Masukkan angka yang valid.")
    
    status = 'belum selesai'

    points = calculate_points(difficulty)

    task = {
        'name': name,
        'deadline': deadline,
        'difficulty': difficulty,
        'points': points,
        'status': status
    }

    tasks.append(task)
    print("\nTugas berhasil ditambahkan!")

# Function to calculate points based on task difficulty
def calculate_points(difficulty):
    if difficulty == 1:
        return 1
    elif difficulty == 2:
        return 3
    elif difficulty == 3:
        return 5
    else:
        return 0

# Mengubah difficulty ke tipe data string
def difficulty_to_string(difficulty):
    if difficulty == 1:
        return "Mudah"
    elif difficulty == 2:
        return "Sedang"
    elif difficulty == 3:
        return "Sulit"
    else:
        return "Tidak valid"

# Function to delete a task
def delete_task():
    if tasks:
        print("Pilih tugas yang ingin dihapus:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']}")

        choice = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        deleted_task = tasks.pop(choice - 1)
        print(f"Tugas '{deleted_task['name']}' dihapus.")
    else:
        print("Belum ada tugas untuk dihapus")


# Function to complete task
def complete_task():
    incomplete_tasks = [task for task in tasks if task['status'] == 'belum selesai']

    if incomplete_tasks:
        print("Daftar Tugas Belum Selesai:")
        for i, task in enumerate(incomplete_tasks):
            print(f"{i+1}. {task['name']} - Deadline: {task['deadline']}, Difficulty: {difficulty_to_string(task['difficulty'])}, Poin: {task['points']}")

        # Meminta pengguna memilih nomor tugas yang ingin diselesaikan
        while True:
            try:
                choice = int(input("Pilih nomor tugas yang ingin diselesaikan: "))
                selected_task = incomplete_tasks[choice-1]
                break
            except (ValueError, IndexError):
                print("Masukkan nomor tugas yang valid.")
        # Menyelesaikan tugas yang dipilih
        earned_points = selected_task['difficulty']
        character_stats['poin'] += earned_points
        selected_task['status'] = 'selesai'  # Tandai tugas sebagai selesai
        print(f"\nTugas '{selected_task['name']}' selesai! Anda mendapatkan {earned_points} poin.")
        print(f"Stats Karakter Terupdate: Poin - {character_stats['poin']}")
    else:
        print("Belum ada tugas untuk diselesaikan.")

# Main program loop
while True:
    welcome_questlist()

    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    option = input("Pilih opsi: ")

    if option == '1':
        if login():
            while True:
                home_page()

                choice = input("Masukkan pilihan anda (1-3, '4/exit' untuk keluar): ")

                if choice == '1':
                    add_task()
                elif choice == '2':
                    complete_task()
                elif choice == '3':
                    delete_task()
                elif choice == '4':
                    break
                elif choice.lower() == 'exit':
                    break
                else:
                    print("Pilihan tidak valid! Coba pilihan yang tertera.")

    elif option == '2':
        register()

    elif option == '3':
        print("Goodbye!")
        break

    else:
        print("Pilihan tidak valid! Coba pilihan yang tertera.")
