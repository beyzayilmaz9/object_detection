import serial
import tkinter as tk
from tkinter import filedialog

# Tkinter dosya seçici açılır
root = tk.Tk()
root.withdraw()  # Ana pencereyi gizle

file_path = filedialog.askopenfilename(title="Veri dosyasını seçin", filetypes=[("Text files", "*.txt")])

if file_path:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()  # Dosya içeriğini oku

        # Arduino'ya bağlan
        ser = serial.Serial("COM9", 9600, timeout=1)
        ser.write(data.encode())  # Veriyi gönder
        ser.close()  # Bağlantıyı kapat

        print("Veri başarıyla Arduino'ya gönderildi!")

    except Exception as e:
        print("Hata:", e)
else:
    print("Dosya seçilmedi.")
