fiyat_kitap = 80  # TL
fiyat_defter = 20  # TL
fiyat_kalem = 5  # TL

adet_kitap = 2
adet_defter = 3
adet_kalem = 4

toplam_odeme = (fiyat_kitap * adet_kitap) + (fiyat_defter * adet_defter) + (fiyat_kalem * adet_kalem)
print("Müşteri ödemesi gereken toplam tutar:", toplam_odeme, "TL")