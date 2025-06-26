import random

palavra_secreta = "girafa"
f = open("palavras.txt")
tamanhoDoArquivo = int(f.readline()) - 1
randomLineInt = random.randint(1, tamanhoDoArquivo)
j = 1
tamanhoPalavra = len(palavra_secreta)
while j < randomLineInt + 1:
    palavra_secreta = f.readline()
    j += 1
f.close()

letras_acertadas = []
tentativas = 6
for letra in palavra_secreta:
    letras_acertadas.append("_")
tamanhoLetrasAcertadas = len(letras_acertadas)

letras_acertadas.pop(tamanhoLetrasAcertadas - 1)
print(palavra_secreta)
print(randomLineInt)

while tentativas > 0 and "_" in letras_acertadas:
  palpite = input("Digite uma letra: ").lower()
  if palpite in palavra_secreta:
    index = 0
    for letra in palavra_secreta:
      if palpite == letra:
        letras_acertadas[index] = letra
      index += 1
  else:
    tentativas -= 1
    print(f"Você tem {tentativas} tentativas restantes.")

  print(" ".join(letras_acertadas))
if "_" not in letras_acertadas:
  print("Parabéns, você ganhou!")
else:
  print("Que pena, você perdeu. A palavra era:", palavra_secreta)
