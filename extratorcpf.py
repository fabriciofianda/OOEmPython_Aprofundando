import re

endereco = "Rua do Limoeiro, nº123, Jardim Alvorada, Alfenas - MG, cep - 37.130-000"

padrao = re.compile("[0-9]{2}[.]{0,1}?[0-9]{3}[-]{0,1}?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)