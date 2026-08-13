#Deve ler o arquivo .txt criado pelo script de openW.py
with open("TesteOpen.txt", "r", encoding="utf-8") as file:
  content = file.read()
print(content)

print("-" *100)

#Lê o arquivo linha por linha
# with open("TesteOpen.txt", "r", encoding="utf-8") as file_copy:
#     for index, line in enumerate(file_copy, start=1):
#         print(f"{index} - {line.strip()}")
