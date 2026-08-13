#Deve criar o arquivo 'TesteOpen.txt' caso não exista e preenche-lo com uma frase
with open("TesteOpen.txt", "w", encoding="utf-8") as file:
  file.write("Arquivo criado com sucesso pela função open()\n\n")
  file.write("As Borboletas \n \n Brancas \n Azuis \n Amarelas \n E pretas \n Brincam \n Na luz \n As belas \n Borboletas \n \n Borboletas brancas \n São alegres e francas \n \n Borboletas azuis \n Gostam muito de luz \n \n As amarelinhas \n São tão bonitinhas! \n \n E as pretas, então \n Oh, que escuridão!\n")