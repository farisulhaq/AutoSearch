import pyautogui
import random
import time
from keywords import generate_long_query

# Jumlah pencarian yang akan dilakukan
search_count = 35

# Delay antara aksi (dalam detik)
delay_between_actions = 5

# Delay antara setiap karakter saat mengetik (meniru gaya mengetik manusia)
typing_delay = 0.1

def google_search(query):
    pyautogui.typewrite(query, interval=0.04) #Increase typing speed in Searching time {slow = 1 , fast = 0.02}
    pyautogui.press('enter')
    time.sleep(random.uniform(1,4))  

# Buka Microsoft Edge
def open_edge():
    pyautogui.hotkey('winleft')  # Tekan tombol Windows
    time.sleep(1)
    pyautogui.typewrite('microsoft edge')  # Ketik "microsoft edge" dengan gaya mengetik manusia
    time.sleep(1)
    pyautogui.press('enter')  # Tekan Enter untuk membuka Edge
    time.sleep(5)  # Tunggu Edge terbuka

open_edge()

for i in range(search_count):
    # Fokus ke address bar (Ctrl + L)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)

    # Ketik query pencarian dengan gaya mengetik manusia
    google_search(generate_long_query())

    time.sleep(delay_between_actions)

print("Pencarian selesai!")
pyautogui.hotkey('ctrl', 'w')

