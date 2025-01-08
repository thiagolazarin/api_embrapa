from app import app

def start_flask_server():
    print("Iniciando servidor Flask...")
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    start_flask_server()
