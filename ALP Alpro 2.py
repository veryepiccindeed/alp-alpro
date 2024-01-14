# Simple Task Management App in Python

#Character stats
character_stats = {'poin': 0, 'level': 1, 'nyawa': 3}

# User data storage
users = {}

# Task data storage
tasks = []

# Function to display the welcome message
def welcome_text():
    print("Selamat datang di aplikasi kami!")

# Function for user login
def login():
    username = input("Masukkan username anda: ")
    password = input("Masukkan password anda: ")

    if username in users and users[username]['password'] == password:
        print("Login berhasil!")
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
    print(f"Statistik Karakter: Poin - {character_stats['poin']} , Level - {character_stats['level']}, Nyawa - {character_stats['nyawa']}")

    if tasks:
        print("\nDaftar Tugas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']} - Deadline: {task['deadline']}, Difficulty: {task['difficulty']}, Points: {task['points']}")
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
    deadline = input("Masukkan deadline tugas (Tanggal/Bulan/Tahun): ")
    difficulty = input("Masukkan tingkat kesulitan tugas (Mudah/Sedang/Sulit): ")

    task = {
        'name': name,
        'deadline': deadline,
        'difficulty': difficulty,
        'points': calculate_points(difficulty)
    }

    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

# Function to calculate points based on task difficulty
def calculate_points(difficulty):
    if difficulty.lower() == 'mudah':
        return 1
    elif difficulty.lower() == 'sedang':
        return 3
    elif difficulty.lower() == 'sulit':
        return 5
    else:
        return 0

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
    if tasks:
        completed_task = tasks.pop(0)
        earned_points = completed_task['points']

        character_stats['poin'] += earned_points
        print(f"Tugas '{completed_task['name']}' selesai! Anda mendapatkan {completed_task['points']} poin.")
        print(f"Stats Karakter Terupdate: Poin - {character_stats['poin']}")
    else:
        print("Belum ada tugas untuk diselesaikan.")


# Main program loop
while True:
    welcome_text()

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
                    print("Pilihan tidak valid, coba pilihan yang tertera.")

    elif option == '2':
        register()

    elif option == '3':
        print("Goodbye!")
        break

    else:
        print("Pilihan tidak valid, coba pilihan yang tertera.")
