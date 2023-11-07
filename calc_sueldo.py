sueldos_Juan={
    'ene':300,
    'feb':300,
    'mar':300,
    'abr':300,
    'may':300,
    'jun':300,
    'jul':500,
    'ago':500,
    'sep':500,
    'oct':500,
    'nov':700,
    'dic':700
}
sueldo_anual=0
for value in sueldos_Juan.values():
    
    sueldo_anual = value + sueldo_anual
#print('Sueldo anual: ', sueldo_anual)

sueldo_promedio = sueldo_anual/len(sueldos_Juan)
print(f'Sueldo promedio: ${sueldo_promedio}')

if sueldo_promedio>300:
    if sueldo_promedio>900:
        print("Sueldo superior a lo normal")
    else:
        print("Sueldo normal")
else:
    print("Sueldo bajo")