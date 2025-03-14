import csv

# Abrir o arquivo CSV original
with open('eventos-atos-preparatorios-2024-ponto-virgula.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    data = list(reader)

# Salvar o arquivo CSV convertido
with open('eventos-atos-preparatorios-2024-virgula.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(data)

print("Conversão concluída!")