import subprocess
import time
import random
from keywords import generate_long_query

# cek adb
adb_check = subprocess.run("adb --version", shell=True)


# Jumlah pencarian
search_count = 25

# Delay antara pencarian (detik)
delay_between_searches = 2

# Koordinat kolom pencarian Bing
first_search_bar_position = (500, 1400)  # Saat pertama kali membuka aplikasi (tengah layar)
second_search_bar_position = (500, 200)  # Setelah pencarian pertama (atas layar)

def run_adb_command(command):
    """Fungsi untuk menjalankan perintah ADB"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def open_bing():
    """Buka aplikasi Bing di Android"""
    run_adb_command("adb shell monkey -p com.microsoft.bing -c android.intent.category.LAUNCHER 1")
    time.sleep(5)  # Tunggu aplikasi terbuka

def tap_search_bar(position):
    """Ketuk kolom pencarian di posisi tertentu"""
    x, y = position
    run_adb_command(f"adb shell input tap {x} {y}")
    time.sleep(1)

def clear_search_bar():
    """Menghapus query di kolom pencarian dengan backspace"""
    # Tekan tombol backspace beberapa kali untuk menghapus teks
    # for _ in range(20):  # Tekan backspace 20 kali untuk menghapus teks
    run_adb_command("adb shell input tap 945 180")
    time.sleep(0.1)

def search_bing(query, is_first_search):
    """Melakukan pencarian di aplikasi Bing"""
    # Gunakan koordinat yang sesuai
    if is_first_search:
        tap_search_bar(first_search_bar_position)  # Klik tengah layar saat pertama kali
    else:
        tap_search_bar(second_search_bar_position)  # Klik bagian atas setelah pencarian pertama
        clear_search_bar()  # Hapus query sebelumnya sebelum mengetik yang baru
    
    time.sleep(1)

    # Ketik query pencarian baru
    run_adb_command(f'adb shell input text "{query}"')
    time.sleep(1)

    # Tekan Enter untuk mencari
    run_adb_command("adb shell input keyevent 66")
    time.sleep(random.uniform(3, 6))

# Mulai otomatisasi
open_bing()

for i in range(search_count):
    query = generate_long_query().replace(" ", "%s") # Pilih query acak
    search_bing(query, is_first_search=(i == 0))  # Gunakan tap pertama hanya untuk pencarian pertama
    time.sleep(delay_between_searches)

print("Pencarian di Bing selesai!")
