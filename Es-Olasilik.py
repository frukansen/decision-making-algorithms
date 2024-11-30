<<<<<<< HEAD
def es_olasilik_olcutu():
    print("Eş Olasılık Ölçütü Programı")

    # Kullanıcıdan koşulları alma
    kosullar = []
    print("\nKoşulları girin (bittiğinde 'tamam' yazın):")
    while True:
        kosul = input("Koşul: ").strip()
        if kosul.lower() == "tamam":
            break
        if not kosul:  # Boş bir koşul girildiyse çık
            print("Boş bir koşul girdiniz. Programdan çıkılıyor.")
            return
        kosullar.append(kosul)

    # Eğer hiç koşul girilmediyse çık
    if not kosullar:
        print("Hiç koşul girilmedi. Programdan çıkılıyor.")
        return

    # Kullanıcıdan seçenekleri ve değerlerini alma
    secenekler = {}
    print("\nSeçenekleri ve her koşul için değerlerini girin:")
    while True:
        secenek = input("Seçenek ismi (bittiğinde 'tamam' yazın): ").strip()
        if secenek.lower() == "tamam":
            break
        if not secenek:  # Boş bir seçenek girildiyse çık
            print("Boş bir seçenek girdiniz. Programdan çıkılıyor.")
            return

        secenek_degerleri = []
        for kosul in kosullar:
            while True:
                try:
                    deger = input(f"'{secenek}' için '{kosul}' koşulundaki değeri girin: ").strip()
                    if not deger:  # Değer girilmediyse çık
                        print("Boş bir değer girdiniz. Programdan çıkılıyor.")
                        return
                    deger = float(deger)
                    secenek_degerleri.append(deger)
                    break
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")
        
        secenekler[secenek] = secenek_degerleri

    # Eğer hiç seçenek girilmediyse çık
    if not secenekler:
        print("Hiç seçenek girilmedi. Programdan çıkılıyor.")
        return

    # Ortalama değerleri hesaplama
    ortalama_degerler = {
        secenek: sum(degerler) / len(degerler) for secenek, degerler in secenekler.items()
    }

    # En iyi seçeneği bulma
    en_iyi_secenek = max(ortalama_degerler, key=ortalama_degerler.get)

    # Sonuçları gösterme
    print("\nSonuçlar:")
    for secenek, ortalama in ortalama_degerler.items():
        print(f"{secenek}: Ortalama Değer = {ortalama:.2f}")
    print(f"\nEn iyi seçenek: {en_iyi_secenek}")


# Programı çalıştır
es_olasilik_olcutu()
=======
def es_olasilik_olcutu():
    print("Eş Olasılık Ölçütü Programı")

    # Kullanıcıdan koşulları alma
    kosullar = []
    print("\nKoşulları girin (bittiğinde 'tamam' yazın):")
    while True:
        kosul = input("Koşul: ").strip()
        if kosul.lower() == "tamam":
            break
        if not kosul:  # Boş bir koşul girildiyse çık
            print("Boş bir koşul girdiniz. Programdan çıkılıyor.")
            return
        kosullar.append(kosul)

    # Eğer hiç koşul girilmediyse çık
    if not kosullar:
        print("Hiç koşul girilmedi. Programdan çıkılıyor.")
        return

    # Kullanıcıdan seçenekleri ve değerlerini alma
    secenekler = {}
    print("\nSeçenekleri ve her koşul için değerlerini girin:")
    while True:
        secenek = input("Seçenek ismi (bittiğinde 'tamam' yazın): ").strip()
        if secenek.lower() == "tamam":
            break
        if not secenek:  # Boş bir seçenek girildiyse çık
            print("Boş bir seçenek girdiniz. Programdan çıkılıyor.")
            return

        secenek_degerleri = []
        for kosul in kosullar:
            while True:
                try:
                    deger = input(f"'{secenek}' için '{kosul}' koşulundaki değeri girin: ").strip()
                    if not deger:  # Değer girilmediyse çık
                        print("Boş bir değer girdiniz. Programdan çıkılıyor.")
                        return
                    deger = float(deger)
                    secenek_degerleri.append(deger)
                    break
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")
        
        secenekler[secenek] = secenek_degerleri

    # Eğer hiç seçenek girilmediyse çık
    if not secenekler:
        print("Hiç seçenek girilmedi. Programdan çıkılıyor.")
        return

    # Ortalama değerleri hesaplama
    ortalama_degerler = {
        secenek: sum(degerler) / len(degerler) for secenek, degerler in secenekler.items()
    }

    # En iyi seçeneği bulma
    en_iyi_secenek = max(ortalama_degerler, key=ortalama_degerler.get)

    # Sonuçları gösterme
    print("\nSonuçlar:")
    for secenek, ortalama in ortalama_degerler.items():
        print(f"{secenek}: Ortalama Değer = {ortalama:.2f}")
    print(f"\nEn iyi seçenek: {en_iyi_secenek}")


# Programı çalıştır
es_olasilik_olcutu()
>>>>>>> origin/main
