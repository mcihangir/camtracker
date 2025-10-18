import os

# Değişiklik yapılacak klasörün yolu
library_folder = r"D:\Projects\CamTracker\04_Hardware\PCBs\CamTracker\KiCad_Libs\CamTracker.pretty"  # Buraya değiştirmek istediğiniz klasör yolunu yazın

# Eski ve yeni yol metinleri
old_text = "D:/Projects/SmartNFC/04_Hardware/PCBs/SmartNFC/KiCad_Libs"
new_text = "${KIPRJMOD}/KiCad_Libs"

# Klasördeki tüm .kicad_mod dosyalarını gez
for root, dirs, files in os.walk(library_folder):
    for file in files:
        if file.endswith(".kicad_mod"):  # Yalnızca .kicad_mod dosyalarını seç
            file_path = os.path.join(root, file)
            
            # Dosyayı oku
            with open(file_path, "r", encoding="utf-8") as f:
                file_data = f.read()

            # Eski metni yeni metinle değiştir
            if old_text in file_data:
                new_data = file_data.replace(old_text, new_text)
                
                # Değiştirilen veriyi dosyaya geri yaz
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_data)
                print(f"Updated 3D model path in: {file_path}")
            else:
                print(f"No change needed in: {file_path}")
