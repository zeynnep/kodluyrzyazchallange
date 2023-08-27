# ir yarış pistinde iki yarışmacı aynı anda start alıyor.
#  İlk yarışmacı saatte 15 km hızla, ikinci yarışmacı ise saatte 20 km hızla koşuyor. 
# İkinci yarışmacı kaç saat sonra ilk yarışmacıyı yakalar?

def yakalama_zamani(hiz1, hiz2):
    hiz_farki = hiz2 - hiz1  # İkinci yarışmacının hızıyla ilk yarışmacının hızı arasındaki farkı hesaplar.
    yakalama_zamani = 0

    if hiz_farki <= 0:
        return "İkinci yarışmacı ilk yarışmacıyı yakalayamaz."  # İkinci yarışmacının hızı ilk yarışmacıdan düşük veya eşitse yakalayamaz.
    else:
        yakalama_zamani = hiz1 / hiz_farki  # İlk yarışmacının kaç saat sonra yakalanacağını hesaplar.
        return yakalama_zamani

ilk_yarismaci_hizi = 15  # İlk yarışmacının hızı (km/saat)
ikinci_yarismaci_hizi = 20  # İkinci yarışmacının hızı (km/saat)

# Yakalama zamanını hesapla ve sonucu yazdır.
sonuc = yakalama_zamani(ilk_yarismaci_hizi, ikinci_yarismaci_hizi)
if isinstance(sonuc, float):  # Eğer sonuç bir ondalık sayıysa
    print(f"İkinci yarışmacı ilk yarışmacıyı {sonuc:.2f} saat sonra yakalar.")  # Sonucu iki ondalık basamakla yazdır.
else:
    print(sonuc)  # İkinci yarışmacı ilk yarışmacıyı yakalayamazsa mesajı yazdır.







