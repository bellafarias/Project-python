nascimentoI=1984
nascimentoII=1988
anoAtual=2023

def calculoIdade(nascimento,anoAtual):
    Idade= anoAtual- nascimento
    return Idade


Idade2=calculoIdade(nascimentoII,anoAtual)
Idade1=calculoIdade(nascimentoI,anoAtual)
print("Idade 1 é", Idade2, "anos")
print("Idade 2 é", Idade1, "anos")

