#  Bir kutuda 5 kırmızı, 4 yeşil ve 3 mavi top bulunuyor. Kutudan rastgele çekilen 2 topun aynı renk olma olasılığı nedir?


# İstenilen renklerin toplarının sayıları
kirmizi_toplar = 5
yesil_toplar = 4
mavi_toplar = 3

# Toplam topların sayısı
toplam_toplar = kirmizi_toplar + yesil_toplar + mavi_toplar

# İki topun aynı renkte olma olasılığını hesapla
ayni_renk_olasiligi = (kirmizi_toplar/toplam_toplar) * ((kirmizi_toplar-1)/(toplam_toplar-1)) + \
                     (yesil_toplar/toplam_toplar) * ((yesil_toplar-1)/(toplam_toplar-1)) + \
                     (mavi_toplar/toplam_toplar) * ((mavi_toplar-1)/(toplam_toplar-1))

print("İki topun aynı renkte olma olasılığı:", ayni_renk_olasiligi)