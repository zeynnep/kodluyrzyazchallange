# Hız hesaplamaları
first_inflow_rate = 1/10
second_inflow_rate = 1/15
outflow_rate = -1/30

# Toplam giriş hızı hesaplama
total_inflow_rate = first_inflow_rate + second_inflow_rate + outflow_rate

# Havuzun ne kadar sürede dolduğunu hesaplama
pool_volume = float(input("Havuzun hacmini girin: "))  # Havuzun hacmi (örneğin metreküp cinsinden)
fill_time = pool_volume / total_inflow_rate

print(f"Havuz {fill_time:.2f} saatte dolar.")