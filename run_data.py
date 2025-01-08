from app.utils.init_data import main as run_scraping

if __name__ == "__main__":
    # Passo 1: Executar o init_data.py (garantir que isso só rode na primeira inicialização)
    print("Executando scraping e inicializando dados...")
    try:
        run_scraping()
        print("Scraping concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao executar o scraping: {str(e)}")