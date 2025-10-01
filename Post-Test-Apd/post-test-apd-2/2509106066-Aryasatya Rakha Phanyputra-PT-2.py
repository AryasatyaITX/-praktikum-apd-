# List suhu dalam Celcius
suhu = [27,33,46,55,67,92]

# Rumus konversi suhu
# Rumus Celcius ke Fahrenheit : ⁰F = (9/5) * ⁰C + 32
Fahrenheit_1 = (9/5) * suhu[0] + 32
Fahrenheit_2 = (9/5) * suhu[1] + 32

# Rumus Celcius ke Kelvin : (K= ⁰C + 273,15)
Kelvin_3 = suhu[2] + 273.15
Kelvin_4 = suhu[3] + 273.15
# Rumus Celcius ke Reamur : ⁰R = (4/5) × ⁰C 
Reamur_5 = (4/5) * suhu[4]
Reamur_6 = (4/5) * suhu[5]

# Jumlahkan semua suhu
jumlah = Fahrenheit_1 + Fahrenheit_2 + Kelvin_3 + Kelvin_4 + Reamur_5 + Reamur_6

# Hitung rata-rata
rata2=jumlah/6

# Masukkan NIM ke variabel
NIM=66

#Bandingkan variabel
bool=NIM<rata2

# Output semua variabel
print("Suhu dalam Celcius:", suhu)
print("Fahrenheit 1:", Fahrenheit_1)
print("Fahrenheit 2:", Fahrenheit_2)
print("Kelvin 3:", Kelvin_3)
print("Kelvin 4:", Kelvin_4)
print("Reamur 5:", Reamur_5)
print("Reamur 6:", Reamur_6)
print("Jumlah:", jumlah)
print("Rata-rata:", rata2)
print("NIM:", NIM)
print("Bolean:", bool)

# Slice suhu dari 46 sampai 92 dengan index negatif
print("Slice (46 sampai 92):", suhu[-4:])