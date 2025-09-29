from bs4 import BeautifulSoup
import datetime


def definir_mes() -> str: 
    dt = datetime.datetime.now()
    ano: int = dt.year
    mes: int = dt.month
    dia: int = dt.day
    if mes < 10:
        mes = f'0{mes}'
    if dia < 10:
        dia = f'0{dia}'
    data_formatada: str = (f'{dia}-{mes}-{ano}')
    return data_formatada




def escrever_post(conteudo, data):
    # Abre o HTML existente
    with open(r".utils\blog\template.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Encontra a div que vai receber o post
    container = soup.find("div", class_="simple-container")

    ## Cria um novo parágrafo ##
    novo_p = soup.new_tag("p")
    novo_p.string = conteudo

    # Adicionar depois do que já existe
    container.append(novo_p)

    # Salva de volta no HTML
    with open(f"{data}.html", "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))





if __name__ == "__main__":
    contagem: int = 0
    data = definir_mes()
    print(data)
    conteudo = input(f'Escreva o {contagem+1}° parágrafo:')
    escrever_post(conteudo, data)
