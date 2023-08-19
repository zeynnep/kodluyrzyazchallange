import math

# Kullanıcıdan bir sayı al
sayi = float(input("Bir sayı girin: "))

# Karekökünü hesapla
karekok = math.sqrt(sayi)

# Eğer sayının karekökü tam sayıya eşitse
if karekok == int(karekok):
    print("Sayının karekökü:", int(karekok))
else:
    print("Bu sayının karekökü tam olarak çıkmıyor.")