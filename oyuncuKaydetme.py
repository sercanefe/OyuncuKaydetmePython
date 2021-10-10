print("Oyuncu Kaydetme Programı")
print(" ")
ad = input("Oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun Takımı: ")

bilgiler = [ad,soyad,takım]

print(" ")
print("Yükleniyor...")
print(" ")

print("Oyuncunun Adı: {}\nOyuncunun Soyadı: {}\nOyuncunun Takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))