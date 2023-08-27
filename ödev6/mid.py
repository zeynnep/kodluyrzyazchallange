# Bir öğrenci kitap okuma hedefi olarak yılda 36 kitap okumayı belirledi. Eğer her ay eşit sayıda kitap okursa kaç kitap okumuş olur?



def kitap_okuma_hesapla(yillik_hedef):
    aylik_hedef = yillik_hedef / 12
    return aylik_hedef

yillik_kitap_hedefi = 36
aylik_kitap_hedefi = kitap_okuma_hesapla(yillik_kitap_hedefi)

print(f"Bir ayda okunması gereken kitap sayısı: {aylik_kitap_hedefi}")