import os


def klasor_icerik_sayisi(ana_klasor):
    try:
        # Desteklenen görüntü formatları
        gorsel_uzantilar = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

        # Ana klasördeki tüm alt klasörleri al
        alt_klasorler = [d for d in os.listdir(ana_klasor)
                         if os.path.isdir(os.path.join(ana_klasor, d))]

        print("Klasörlerdeki görsel sayıları:")
        toplam_gorsel = 0

        # Her alt klasör için görsel sayısını hesapla
        for klasor in sorted(alt_klasorler):  # Alfabetik sıralama
            klasor_yolu = os.path.join(ana_klasor, klasor)

            # Klasördeki görsel dosyalarını say
            gorsel_sayisi = len([f for f in os.listdir(klasor_yolu)
                                 if f.lower().endswith(gorsel_uzantilar)])

            print(f"{klasor} klasörü: {gorsel_sayisi} adet görsel")
            toplam_gorsel += gorsel_sayisi

        print(f"\nToplam {len(alt_klasorler)} klasör")
        print(f"Toplam {toplam_gorsel} görsel")

    except Exception as e:
        print(f"Hata oluştu: {e}")


# Kullanım
dataset_yolu = "/Users/altun/Desktop/train/dataSet"  # Dataset klasörünün yolunu buraya yazın
klasor_icerik_sayisi(dataset_yolu)