arancel = 1800000
valor_matricula = 90000
descuento_arancel = 0
descuento_matricula = 0

promedio_final = float(input("Ingresa el promedio final con el que saliste del colegio o el liceo: "))
print("Ingresa tu nivel socioeconomico, donde 1 representa mayor vulnerabilidad y 5 menor vulnerabilidad: ")
quintil = int(input("1-5: "))



if promedio_final > 6.0 and (quintil == 1 or quintil == 2):
    descuento_arancel = arancel - (arancel * 0.2)
elif promedio_final > 6.0 and (quintil == 3 or quintil == 4):
    descuento_arancel = arancel - (arancel * 0.15)
elif(promedio_final > 5.0 and promedio_final <= 6.0) and (quintil == 1 or quintil == 2):
    descuento_arancel = arancel - (arancel * 0.13)
elif(promedio_final > 5.0 and promedio_final <= 6.0) and (quintil == 3 or quintil == 4):
    descuento_arancel = arancel - (arancel * 0.1)
else:
    descuento_arancel = 180000

if (quintil == 1 or quintil == 2 or quintil == 3) and promedio_final >= 5.5:
    descuento_matricula = valor_matricula - (valor_matricula * 0.15)
elif quintil == 1 or quintil == 2 or quintil == 3:
    descuento_matricula = valor_matricula - (valor_matricula * 0.1)
else:
    descuento_matricula = valor_matricula

print("El valor final del arancel es: ", descuento_arancel)
print("El valor final de la Matricula es: ", descuento_matricula)