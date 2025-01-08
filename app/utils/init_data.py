from app.services.scraping_service import (
    get_producao_data,
    get_processamento_data,
    get_comercializacao_data,
    get_importacao_data,
    get_exportacao_data,
)

def main():
    print("Iniciando scraping e salvando dados no banco...")
    try:
        get_producao_data()
        print("Dados de produção salvos com sucesso.")

        get_processamento_data()
        print("Dados de processamento salvos com sucesso.")

        get_comercializacao_data()
        print("Dados de comercialização salvos com sucesso.")

        get_importacao_data()
        print("Dados de importação salvos com sucesso.")

        get_exportacao_data()
        print("Dados de exportação salvos com sucesso.")
        
        print("Scraping concluído com sucesso!")
    except Exception as e:
        print(f"Erro durante o scraping: {str(e)}")

# Certifique-se de que o código só seja executado diretamente
if __name__ == "__main__":
    main()
