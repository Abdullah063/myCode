import os
import shutil


def organize_files(source_folder):
    # Hedef klasörleri oluştur
    img_folder = os.path.join(source_folder, "img")
    label_folder = os.path.join(source_folder, "label")
    os.makedirs(img_folder, exist_ok=True)
    os.makedirs(label_folder, exist_ok=True)

    # Kaynak klasör içindeki dosyaları tarayın
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)

        # Sadece dosyalarla işlem yap
        if os.path.isfile(source_file):
            if filename.endswith(".jpg"):
                shutil.move(source_file, os.path.join(img_folder, filename))
            elif filename.endswith(".txt"):
                shutil.move(source_file, os.path.join(label_folder, filename))

    print("Dosyalar başarıyla taşındı!")


# Kullanım
source_folder_path = "/Users/altun/Desktop/bitirme projesi /veriSetleri /archive/test/test"  # Buraya klasör yolunu yazın
organize_files(source_folder_path)