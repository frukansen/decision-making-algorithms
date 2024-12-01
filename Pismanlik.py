def karar_ver():

    durum = input("Girilecek veriler kazanç mı (k) yoksa maliyet mi (m)? (k/m): ").lower()
    
    if durum not in ['k', 'm']:
        print("Geçersiz seçenek. Program sonlandırılıyor.")
        return
    
    print("Koşulları girin (çıkmak için 'q'):")
    kosullar = []
    while True:
        kosul = input("Koşul (çıkmak için 'q'): ")
        if kosul.lower() == 'q':
            break
        kosullar.append(kosul)
    
    # Seçenekler
    print("\nSeçenekleri girin (çıkmak için 'q'):")
    secenekler = []
    while True:
        secenek = input("Seçenek (çıkmak için 'q'): ")
        if secenek.lower() == 'q':
            break
        secenekler.append(secenek)
    
    print("\nHer seçeneğin farklı koşullardaki sonuçlarını girin:")
    sonuc_dict = {secenek: {} for secenek in secenekler}
    for secenek in secenekler:
        for kosul in kosullar:
            sonuc = float(input(f"{secenek} seçeneği için '{kosul}' koşulundaki sonucu girin: "))
            sonuc_dict[secenek][kosul] = sonuc
    
    toplam_pismanlik = {secenek: 0 for secenek in secenekler}
    
    for kosul in kosullar:
        # Bu koşul altında tüm seçeneklerin sonuçları
        kosul_sonuclari = {secenek: sonuc_dict[secenek][kosul] for secenek in secenekler}
        
        # Kazanç veya maliyet durumuna göre en iyi seçenek bulunacak
        if durum == 'k':  # Kazanç algoritması
            en_iyi_secenek = max(kosul_sonuclari, key=kosul_sonuclari.get)
        elif durum == 'm':  # Maliyet algoritması
            en_iyi_secenek = min(kosul_sonuclari, key=kosul_sonuclari.get)
        
        # Diğer seçenekler için pişmanlık değerlerini hesapla
        for secenek in secenekler:
            if secenek != en_iyi_secenek:
                # Pişmanlık: olası en iyi sonuç ile kişinin yaptığı seçim arasındaki fark.
                pişmanlık = abs(kosul_sonuclari[secenek] - kosul_sonuclari[en_iyi_secenek])
                toplam_pismanlik[secenek] += pişmanlık
    
    # En düşük toplam pişmanlık değerine sahip seçeneği seç
    secim = min(toplam_pismanlik, key=toplam_pismanlik.get)
    
    # Sonuçları yazdır
    print("\nPişmanlık değerleri toplamı:")
    for secenek, pişmanlık in toplam_pismanlik.items():
        print(f"{secenek}: {pişmanlık}")
    
    print(f"\nPişmanlık değerleri toplamı en az olan seçenek: {secim}")

# Fonksiyonu çalıştır
karar_ver()
