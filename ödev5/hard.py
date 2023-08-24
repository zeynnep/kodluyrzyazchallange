import math

n = 30  # Toplam öğrenci sayısı
k = 4   # Seçilecek öğrenci sayısı

farkli_sekiller = math.comb(n, k)
print("Farklı şekillerde öğrenci seçim sayısı:", farkli_sekiller)

# Bu kod, math modülündeki comb fonksiyonunu kullanarak farklı şekillerde 4 öğrenci seçme sayısını hesaplar. 
# Bu kombinasyon hesaplamasıyla, 30 öğrenciden 4 kişiyi seçmenin kaç farklı şekilde yapılabileceğini bulabilirsiniz.