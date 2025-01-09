from app.utils.init_data import main as run_scraping

if __name__ == "__main__":
    print("Executando scraping e inicializando dados...")
    try:
        run_scraping()
        print("Scraping concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao executar o scraping: {str(e)}")