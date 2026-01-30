import requests
from bs4 import BeautifulSoup
from datetime import datetime

def previsao_do_tempo():
    url = 'https://www.google.com/search?q=previs%C3%A3o+do+tempo&oq=previs%C3%A3o+do+tempo&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE4MzBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        # Inicia a busca
        soup = BeautifulSoup(page.content, 'html.parser')
        local = soup.find_all('span', class_='BBwThe')
        dia = soup.find_all('div', class_='wob_dts')
        temperatura = soup.find_all('span', class_='wob_t q8U8x')

        if temperatura:
            print(f'Local: {local[0].text}')
            print(f'Dia: {dia[0].text}')
            print(f'Temperatura atual: {temperatura[0].text}°C')

            # Salvando os dados em um arquivo .txt
            data_atual = datetime.now().strftime('%d_%m_%Y')
            nome_arquivo = f'Clima {data_atual}.txt'

            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                texto = (
                    f'local: {local[0].text}\n'
                    f'Dia: {dia[0].text}\n'
                    f'Temperatura atual: {temperatura[0].text}°C'
                )
                arquivo.write(texto)
        else:
            print('Dado não localizado')
    else:
        print(f'Erro de requisição: Status code: {page.status_code}')


print('Escolha uma opção:\n')
print('1 - Receber informações de clima\n')

op = int(input('Digite o número referente a opção escolhida: '))

if op == 1:
    print('\n')
    previsao_do_tempo()
    print('\nArquivo salvo na pasta!')
else:
    print('Opção inválida')
    
