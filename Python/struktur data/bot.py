import pyautogui
import time

# Tentukan koordinat klik
koordinat = (500, 200)

# Tentukan jumlah klik
jumlah_klik = 10

# Tunggu 5 detik sebelum mulai
time.sleep(2)

# Lakukan klik sebanyak jumlah_klik
for i in range(jumlah_klik):
    pyautogui.click(koordinat)

