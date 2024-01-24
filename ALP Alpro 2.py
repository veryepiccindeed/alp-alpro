# Simple Task Management App in Python

from datetime import datetime

# Bold text 
class TextStyle:
    BOLD = '\033[1m'
    END = '\033[0m'

#Character stats
character_stats = {'poin': 0, 'level': 1, 'nyawa': 3, 'exp': 0}

#Shop
shop_items = {
    'baju': {
        'items': [
            {'nama': 'Baju Merah', 'harga': 10, 'poin_bonus': 2, 'warna': 'merah'},
            {'nama': 'Baju Hijau', 'harga': 8, 'poin_bonus': 1, 'warna': 'hijau'}
        ]
    },
    'celana': {
        'items': [
            {'nama': 'Celana Merah', 'harga': 15, 'poin_bonus': 3, 'warna': 'merah'},
            {'nama': 'Celana Hijau', 'harga': 12, 'poin_bonus': 2, 'warna': 'hijau'}
        ]
    },
    'topi': {
        'items': [
            {'nama': 'Topi Merah', 'harga': 20, 'poin_bonus': 5, 'warna': 'merah'},
            {'nama': 'Topi Hijau', 'harga': 18, 'poin_bonus': 4, 'warna': 'hijau'}
        ]
    }
}

#Item yang telah dibeli
owned_items = {
    'baju': None,
    'celana': None,
} 

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
    print(f"{TextStyle.BOLD}Statistik Karakter: Poin - {character_stats['poin']} , Level - {character_stats['level']}, Exp - {character_stats['exp']}, Nyawa - {character_stats['nyawa']}{TextStyle.END}")

    display_equipped_items()

    # Menampilkan daftar tugas yang belum selesai
    incomplete_tasks = [task for task in tasks if task['status'] == 'belum selesai']

    if incomplete_tasks:
        print(f"{TextStyle.BOLD}\nDaftar Tugas Belum Selesai:{TextStyle.END}")
        for i, task in enumerate(incomplete_tasks, 1):
            print(f"{TextStyle.BOLD}{i}. {task['name']} - Deadline: {task['deadline']}, Difficulty: {difficulty_to_string(task['difficulty'])}, Poin: {task['points']}{TextStyle.END}")
    else:
        print("\nBelum ada tugas.")

    print("\nOpsi:")
    print("1. Tambahkan tugas")
    print("2. Selesaikan tugas")
    print("3. Hapus tugas")
    print("4. Shop")
    print("5. Topup Gems")
    print("6. Logout")

# Function to add a task
def add_task():
    print(f"Sekarang tanggal: {TextStyle.BOLD}{datetime.now().strftime('%d-%m-%Y')}{TextStyle.END}") 
    name = input("Masukkan nama tugas: ")

    while True:
        try:
            deadline_str = input("Masukkan deadline tugas (Tanggal-Bulan-Tahun): ")
            deadline = datetime.strptime(deadline_str, "%d-%m-%Y")
            if deadline < datetime.now():
                print(F"{TextStyle.BOLD}DEADLINE TIDAK BISA SEBELUM TANGGAL SEKARANG!{TextStyle.END}")
            else:
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
    
def calculate_experience(difficulty):
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 20
    elif difficulty == 3:
        return 30
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
        print(f"{TextStyle.BOLD}\nDaftar Tugas Belum Selesai:{TextStyle.END}")
        for i, task in enumerate(incomplete_tasks):
            print(f"{TextStyle.BOLD}{i+1}. {task['name']} - Deadline: {task['deadline']}, Difficulty: {difficulty_to_string(task['difficulty'])}, Poin: {task['points']}{TextStyle.END}")

        # Meminta pengguna memilih nomor tugas yang ingin diselesaikan
        while True:
            try:
                choice = int(input("Pilih nomor tugas yang ingin diselesaikan: "))
                selected_task = incomplete_tasks[choice-1]
                break
            except (ValueError, IndexError):
                print("Masukkan nomor tugas yang valid.")
        # Menyelesaikan tugas yang dipilih
        earned_points = calculate_points(selected_task['difficulty'])
        character_stats['poin'] += earned_points
        selected_task['status'] = 'selesai'  # Tandai tugas sebagai selesai

        exp_earned = calculate_experience(selected_task['difficulty'])
        exp(exp_earned)

        print(f"\nTugas '{selected_task['name']}' selesai! Anda mendapatkan {earned_points} poin dan exp {exp_earned}.")
        print(f"Stats Karakter Terupdate: Poin - {character_stats['poin']}, Exp - {character_stats['exp']}.")

    else:
        print("Belum ada tugas untuk diselesaikan.")

def exp(exp_earned):
    # Menentukan persyaratan exp untuk naik level
    level_exp_required = 100 + (character_stats['level'] - 1) * 50

    # Menambahkan exp yang diperoleh dari tugas yang selesai
    character_stats['exp'] += exp_earned

    # Cek apakah karakter telah mencapai atau melebihi persyaratan exp untuk naik level
    if character_stats['exp'] >= level_exp_required:
        # Menaikkan level karakter
        character_stats['level'] += 1
        # Mengurangkan exp yang digunakan untuk naik level dari total exp karakter
        character_stats['exp'] -= level_exp_required
        # Menampilkan pesan bahwa karakter telah naik level
        print(f"\nSelamat! Karakter Anda naik ke Level {character_stats['level']}!")

# Function to handle level up
def level_up():
    character_stats['level'] += 1
    character_stats['next_level_exp'] += 50  # Menambahkan 50 exp untuk mencapai level berikutnya
    print(f"Selamat! Anda naik ke Level {character_stats['level']}!")
    print(f"Exp yang dibutuhkan untuk mencapai Level berikutnya: {character_stats['next_level_exp']}")

# Function shop
def shop():
    while True:
        print("\nSelamat datang di Shop Karakter!")
        print("Pilih kategori item yang ingin dibeli:")
        print("1. Baju")
        print("2. Celana")
        print("3. Topi" if character_stats['level'] >= 4 else "3. Topi (Terbuka di Level 4)")  # Menampilkan opsi topi dengan peringatan
        print("4. Kembali ke Halaman Utama")

        choice = input("Masukkan nomor kategori (1-4): ")

        if choice == '1':
            buy_item('baju')
        elif choice == '2':
            buy_item('celana')
        elif choice == '3' and character_stats['level'] >= 4:
            buy_item('topi')  # Memanggil fungsi buy_item untuk kategori topi jika level karakter mencapai 4 atau lebih
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid! Coba pilihan yang tertera.")

# Function membeli item
def buy_item(category):
        global character_stats
        global owned_items

        shop_category = shop_items.get(category)

        if not shop_category:
            print(f"Kategori {category.capitalize()} tidak valid.")
            return

        items = shop_category.get('items')

        if not items:
            print(f"Item dalam kategori {category.capitalize()} tidak lengkap.")
            return

        print(f"\nItem yang tersedia di kategori {category.capitalize()}:")
        for i, item in enumerate(items, 1):
            color_code = '\033[91m' if item['warna'] == 'merah' else '\033[92m'
            print(f"{i}. {color_code}{item['nama']}\033[0m - Harga: {item['harga']} poin, Bonus Poin: {item['poin_bonus']}")

        # Menambahkan pemberitahuan untuk kategori yang memerlukan level 4
        if category == 'topi' and character_stats['level'] < 4:
            print("Catatan: Kategori Topi hanya dapat diakses saat mencapai Level 4.")
            return

        print("0. Kembali")

        choice = input("Pilih nomor item yang ingin dibeli (0 untuk kembali): ")

        if choice == '0':
            return  # Kembali ke bagian sebelumnya
        else:
            try:
                index = int(choice) - 1
                selected_item = items[index]

                if owned_items[category] and owned_items[category]['nama'] == selected_item['nama']:
                    print(f"Anda sudah memiliki {selected_item['nama']}. Pembelian dibatalkan.")
                    return
                
            except (ValueError, IndexError):
                print("Pilihan tidak valid! Pembelian dibatalkan.")
                return

            confirm = input(f"Apakah Anda ingin membeli {selected_item['nama']}? (ya/tidak): ")

            if confirm.lower() == 'ya':
                if character_stats['poin'] >= selected_item['harga']:
                    character_stats['poin'] -= selected_item['harga']
                    owned_items[category] = {'nama': selected_item['nama'], 'poin_bonus': selected_item['poin_bonus']}
                    print(f"Item '{selected_item['nama']}' berhasil dibeli!")
                else:
                    print(f"{TextStyle.BOLD}POIN ANDA TIDAK MENCUKUPI UNTUK MEMBELI ITEM!{TextStyle.END}")
            elif confirm.lower() == 'tidak':
                return
            else:
                print("Masukkan yang tidak valid! Pembelian dibatalkan.")

def display_equipped_items():
    equipped_items = {category.capitalize(): item['nama'] if item else None for category, item in owned_items.items()}
    
    print("\nItem yang dipakai oleh karakter:")
    
    # Menampilkan item yang dipakai untuk setiap kategori
    for category, item in equipped_items.items():
        if item:
            color_code = '\033[91m' if category.lower() == 'baju' and item.lower() == 'merah' else '\033[92m' 
            print(f"{category}: {color_code}{item}\033[0m")
    
    if not any(equipped_items.values()):
        print("Tidak ada item yang dipakai.")

def gem():
  print(f"\n{TextStyle.BOLD}Coming Soon! Fitur ini masih dalam pengembangan :){TextStyle.END}")

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

                choice = input("Masukkan pilihan anda (1-4, 5 untuk Log Out): ")

                if choice == '1':
                    add_task()
                elif choice == '2':
                    complete_task()
                elif choice == '3':
                    delete_task()
                elif choice == '4':
                    shop()
                elif choice.lower() == '5':
                    gem()
                elif choice.lower() == '6':
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
