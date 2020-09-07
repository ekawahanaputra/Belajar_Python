# PROGRAM KONVERSI TEMPERATURE FAHRENHEIT & KELVIN

# Fahrenheit to Kelvin
print ("\n=====FAHRENHEIT to KELVIN=====\n")

Fahrenheit = float(input("Masukan suhu dalam F = "))
Kelvin = (5/9 * (Fahrenheit - 32)) + 273
#rumus diatas didapat dari google

print ("Hasil = ", Kelvin, "Kelvin")


# Kelvin to Fahrenheit
print ("\n=====KELVIN to FAHRENHEIT=====\n")

Kelvin = float(input("Masukan suhu dalam K = "))
Fahrenheit = (9/5 * (Kelvin - 273)) + 32
#rumus diatas didapat dari google

print ("Hasil = ", Fahrenheit, "Fahrenheit")