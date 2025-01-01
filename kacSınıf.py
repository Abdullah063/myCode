import os
from collections import Counter


def analiz_et_gorsel_siniflari(klasor_yolu):
    # Desteklenen görüntü formatları
    gorsel_uzantilar = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

    try:
        # Tüm dosyaları al
        dosyalar = os.listdir(klasor_yolu)

        # Sadece görüntü dosyalarını filtrele
        gorsel_dosyalar = [f for f in dosyalar if f.lower().endswith(gorsel_uzantilar)]

        if not gorsel_dosyalar:
            print("Klasörde görüntü dosyası bulunamadı!")
            return

        # Dosya isimlerinden sınıf isimlerini çıkar
        sinif_isimleri = []
        for dosya in gorsel_dosyalar:
            # Dosya uzantısını kaldır
            isim = os.path.splitext(dosya)[0]
            # Sayıları ve özel karakterleri kaldır (opsiyonel)
            isim = ''.join([i for i in isim if not i.isdigit()]).strip('_- ')
            sinif_isimleri.append(isim)

        # Sınıfları say
        sinif_sayaci = Counter(sinif_isimleri)

        # Sonuçları yazdır
        print("\nBulunan sınıflar ve görsel sayıları:")
        for sinif, sayi in sinif_sayaci.items():
            print(f"- {sinif}: {sayi} görsel")

        print(f"\nToplam {len(sinif_sayaci)} farklı sınıf bulundu.")
        print(f"Toplam {len(gorsel_dosyalar)} görsel dosya var.")

        return sinif_sayaci

    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None


# Kullanım örneği:
# # Kendi klasör yolunuzu buraya yazın
klasor_yolu = "/Users/altun/Desktop/train/dataSet"
siniflar = analiz_et_gorsel_siniflari(klasor_yolu)
#------------------------------------------------------
import os
import shutil


def dosyalari_siniflandir(kaynak_klasor, hedef_klasor):
    try:
        # Hedef ana klasörü oluştur
        os.makedirs(hedef_klasor, exist_ok=True)

        # İşlem sayaçları
        basarili = 0
        hatali = 0

        # Tüm dosyaları al
        dosyalar = os.listdir(kaynak_klasor)

        for dosya in dosyalar:
            try:
                if dosya.endswith(('.jpg', '.jpeg', '.png')):
                    # Dosya adını parçalara ayır
                    parcalar = dosya.split('_')

                    # Örnek dosya adı yapısı: "139_0_lemon_wob_26.jpg"
                    if len(parcalar) >= 4:  # En az 4 parça olmalı
                        # Son parçayı temizle (sayı ve uzantıyı kaldır)
                        son_parca = parcalar[-1].split('.')[0]

                        # Sınıf adını bul
                        if 'raspberry' in dosya or 'blackberries' in dosya:
                            # Özel durumlar için
                            sinif_adi = parcalar[2]
                        else:
                            # Normal durumlar için (örn: lemon_wob)
                            sinif_adi = f"{parcalar[2]}_{parcalar[3]}"

                        # Sınıf klasörünü oluştur
                        sinif_klasoru = os.path.join(hedef_klasor, sinif_adi)
                        os.makedirs(sinif_klasoru, exist_ok=True)

                        # Dosyayı kopyala
                        kaynak = os.path.join(kaynak_klasor, dosya)
                        hedef = os.path.join(sinif_klasoru, dosya)
                        shutil.copy2(kaynak, hedef)
                        basarili += 1
                        print(f"Kopyalandı: {dosya} -> {sinif_adi}")
                    else:
                        print(f"Uygun olmayan dosya adı formatı: {dosya}")
                        hatali += 1

            except Exception as e:
                print(f"Dosya işlenirken hata: {dosya} - {str(e)}")
                hatali += 1
                continue

        print("\nİşlem tamamlandı!")
        print(f"Başarıyla kopyalanan dosya sayısı: {basarili}")
        print(f"Hatalı dosya sayısı: {hatali}")

        # Her sınıftaki dosya sayısını göster
        print("\nSınıflara göre dosya sayıları:")
        for sinif in os.listdir(hedef_klasor):
            sinif_yolu = os.path.join(hedef_klasor, sinif)
            dosya_sayisi = len(os.listdir(sinif_yolu))
            print(f"- {sinif}: {dosya_sayisi} görsel")

    except Exception as e:
        print(f"Genel hata oluştu: {e}")


# Kullanım
kaynak_klasor = "/Users/altun/Desktop/train/dataSet/img"  # Görsellerin bulunduğu klasör
hedef_klasor = "/Users/altun/Desktop/train/dataSet"  # Görsellerin kopyalanacağı ana klasör

# dosyalari_siniflandir(kaynak_klasor, hedef_klasor)