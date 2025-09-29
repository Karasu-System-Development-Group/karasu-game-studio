from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import datetime
import os

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def publish(path, date) -> None:
    confirmation: str = input('> Publicar o post? S/N ')
    if confirmation.lower() == 's':
        # Adiciona o arquivo
        os.system(f'git add "{path}"')
        # Cria o commit
        os.system(f'git commit -m "{date} devblog post added"')
        # Dá push para o branch main
        os.system('git push origin main')
        print(Fore.GREEN + 'O post foi publicado com sucesso.')
    elif confirmation.lower() == 'n':
        print(Fore.RED + '> O post não foi publicado.')
        print('> Publicação cancelada/negada pelo autor.')
    else:
        print('> Opção inválida, por favor, tente novamente.')
        publish(path, date)



def current_folder() -> str:
    ano: int = pegar_data()[1]
    mes: int = int(pegar_data()[2])
    mes_final = months[mes - 1]
    final_path: str = os.path.join("pages", "devblog", str(ano), mes_final)

    # Cria a pasta se não existir
    if not os.path.exists(final_path):
        os.makedirs(final_path)
        print("Pasta criada!")
    else:
        print("A pasta já existe.")
    return final_path
        


def pegar_data() -> str: 
    dt = datetime.datetime.now()
    ano: int = dt.year
    mes: int = dt.month
    dia: int = dt.day
    if mes < 10:
        mes = f'0{mes}'
    if dia < 10:
        dia = f'0{dia}'
    data_formatada: str = (f'{dia}-{mes}-{ano}')
    return data_formatada, ano, mes, dia




def escrever_post(arquivo: str, conteudo: str, data: str, title: str):
    # Abre o HTML existente
    with open(fr"{arquivo}", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    soup.title.string = title
    h2_tag = soup.find("div", class_="section-text").h2
    h2_tag.string = fr'//devblog - {title}'

    # Encontra a div que vai receber o post
    container = soup.find("div", class_="simple-container")

    ## Cria um novo parágrafo ##
    novo_p = soup.new_tag("p")
    novo_p.string = conteudo

    # Adicionar depois do que já existe
    container.append(novo_p)

    # Salva de volta no HTML
    # Salva de volta no HTML no caminho correto
    with open(arquivo_final, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))






if __name__ == "__main__":
    continuar: bool = True
    contagem: int = 0
    data: str = pegar_data()[0]
    print(data)
    pasta = current_folder()
    arquivo_final = os.path.join(pasta, f"{data}.html")
    os.system('cls')
    print(f'Criando a postagem do dia {data}.')
    print(' ')
    title: str = input('Por favor, escolha o título da postagem: ')
    while continuar:
        if contagem == 0:
            arquivo: str = r".utils\blog\template.html"
        else:
            arquivo: str = arquivo_final
        conteudo: str = input(f'Escreva o {contagem+1}° parágrafo: ')
        escrever_post(arquivo, conteudo, data, title)
        contagem = contagem+1
        print(contagem)
        escolha: str = input(Fore.RED + 'Continuar? S/N ')
        if escolha.lower() == 'n':
            continuar = False
            os.system('cls')
            print('> Arquivo do post criado com sucesso!')
            print(f'> O post pode ser encontrado em {arquivo_final}')
            print(f'> Você pode clicar com a teclar CTRL + BOTÃO ESQUERDO para acessar o arquivo.')
            print(f'> O total de parágrafos escritos nesta postagem foi de: {contagem}')
            publish(arquivo_final, data)


