import requests
from bs4 import BeautifulSoup
import pandas as pd
from app.utils.database import save_dataframe_to_db

def get_producao_data():
    all_data = [] 
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"

    primeiro_ano = 1970
    ultimo_ano = 2023

    for ano in range(primeiro_ano, ultimo_ano + 1):
        url = f"{base_url}&ano={ano}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados do ano {ano}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        linhas_tabela = table.find_all('tr')

        dados = []
        for linha in linhas_tabela:
            cells = linha.find_all(['th', 'td'])
            cells_text = [cell.get_text(strip=True) for cell in cells]
            dados.append(cells_text)

        df = pd.DataFrame(dados[1:], columns=dados[0])
        df['Ano'] = ano
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)

    # Salvar no banco:
    save_dataframe_to_db(final_df, "producao")
    #return final_df

def get_processamento_data():
    all_data = [] 
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"

    primeiro_ano = 1970
    ultimo_ano = 2023

    for ano in range(primeiro_ano, ultimo_ano + 1):
        url = f"{base_url}&ano={ano}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados do ano {ano}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        linhas_tabela = table.find_all('tr')

        dados = []
        for linha in linhas_tabela:
            cells = linha.find_all(['th', 'td'])
            cells_text = [cell.get_text(strip=True) for cell in cells]
            dados.append(cells_text)

        df = pd.DataFrame(dados[1:], columns=dados[0])
        df['Ano'] = ano
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)
    
    # Salvar no banco:
    save_dataframe_to_db(final_df, "processamento")
    #return final_df

def get_comercializacao_data():
    all_data = [] 
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"

    primeiro_ano = 1970
    ultimo_ano = 2023

    for ano in range(primeiro_ano, ultimo_ano + 1):
        url = f"{base_url}&ano={ano}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados do ano {ano}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        linhas_tabela = table.find_all('tr')

        dados = []
        for linha in linhas_tabela:
            cells = linha.find_all(['th', 'td'])
            cells_text = [cell.get_text(strip=True) for cell in cells]
            dados.append(cells_text)

        df = pd.DataFrame(dados[1:], columns=dados[0])
        df['Ano'] = ano
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)
    
    # Salvar no banco:
    save_dataframe_to_db(final_df, "comercializacao")
    #return final_df

def get_importacao_data():
    all_data = [] 
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"

    primeiro_ano = 1970
    ultimo_ano = 2023

    for ano in range(primeiro_ano, ultimo_ano + 1):
        url = f"{base_url}&ano={ano}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados do ano {ano}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        linhas_tabela = table.find_all('tr')

        dados = []
        for linha in linhas_tabela:
            cells = linha.find_all(['th', 'td'])
            cells_text = [cell.get_text(strip=True) for cell in cells]
            dados.append(cells_text)

        df = pd.DataFrame(dados[1:], columns=dados[0])
        df['Ano'] = ano
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)
        
    # Salvar no banco:
    save_dataframe_to_db(final_df, "importacao")
    #return final_df

def get_exportacao_data():
    all_data = [] 
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"

    primeiro_ano = 1970
    ultimo_ano = 2023

    for ano in range(primeiro_ano, ultimo_ano + 1):
        url = f"{base_url}&ano={ano}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Erro ao buscar dados do ano {ano}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        linhas_tabela = table.find_all('tr')

        dados = []
        for linha in linhas_tabela:
            cells = linha.find_all(['th', 'td'])
            cells_text = [cell.get_text(strip=True) for cell in cells]
            dados.append(cells_text)

        df = pd.DataFrame(dados[1:], columns=dados[0])
        df['Ano'] = ano
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)
        
    # Salvar no banco:
    save_dataframe_to_db(final_df, "exportacao")
    #return final_df