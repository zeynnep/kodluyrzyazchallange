total_animals = 36   # Toplam hayvan sayısı
total_legs = 100     # Toplam bacak sayısı

# Tavukların bacak sayısı (2 bacak)
chicken_legs = 2

# Koyunların bacak sayısı (4 bacak)
sheep_legs = 4

# Denklemler:
# Tavuk sayısı + Koyun sayısı = Toplam hayvan sayısı
# Tavuk sayısı * 2 + Koyun sayısı * 4 = Toplam bacak sayısı

# İki denklemi çözerek tavuk ve koyun sayısını bulalım
# Tavuk sayısı = total_animals - Koyun sayısı
# total_animals - Koyun sayısı * 2 + Koyun sayısı * 4 = total_legs
# total_animals * 2 - Koyun sayısı * 2 = total_legs
# Koyun sayısı * 2 = total_animals * 2 - total_legs
# Koyun sayısı = (total_animals * 2 - total_legs) / 2

sheep_count = int((total_animals * 2 - total_legs) / 2)
chicken_count = total_animals - sheep_count

print(f"Çiftlikte {chicken_count} tavuk ve {sheep_count} koyun bulunmaktadır.")