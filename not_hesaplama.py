def not_hesapla():
    try:
        vize = float(input("Vize notunuzu girin: "))
        final = float(input("Final notunuzu girin: "))

        if vize < 0 or final < 0:
            print("Hata: Notlar negatif olamaz!")
            return
        
        ortalama = (vize * 0.4) + (final * 0.6)

        if ortalama >= 50:
            print("Dersi geçtiniz! Ortalama:", ortalama)
        else:
            print("Dersi geçemediniz! Ortalama:", ortalama)
    
    except ValueError:
        print("Hata: Geçerli bir sayı giriniz.")

not_hesapla()
