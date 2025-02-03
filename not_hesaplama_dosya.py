import os

def not_hesapla():
    input_path = os.path.join(os.getcwd(), "notlar.txt")
    output_path = os.path.join(os.getcwd(), "sonuc.txt")

    if not os.path.exists(input_path):
        with open(input_path, "w") as file:
            file.write("60 75")  # Varsayılan vize ve final notları
    
    try:
        with open(input_path, "r") as file:
            notlar = file.read().strip().split()
            vize, final = float(notlar[0]), float(notlar[1])

        ortalama = (vize * 0.4) + (final * 0.6)

        with open(output_path, "w") as file:
            if ortalama >= 50:
                file.write(f"Dersi geçtiniz! Ortalama: {ortalama}")
            else:
                file.write(f"Dersi geçemediniz! Ortalama: {ortalama}")

        print("Sonuç dosyaya yazıldı:", output_path)

    except ValueError:
        print("Hata: Dosyada geçerli bir sayı olmalıdır.")

not_hesapla()
