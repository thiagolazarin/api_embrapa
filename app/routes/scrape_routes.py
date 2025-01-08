from flask import jsonify
from app import app, auth, cache
#from app.services.scraping_service import get_producao_data, get_processamento_data, get_comercializacao_data, get_importacao_data, get_exportacao_data
from app.utils.database import get_connection
import pandas as pd

@app.route('/')
@auth.login_required
@cache.cached()
def home():
    return "Desafio FIAP"

@app.route('/api/producao', methods=['GET'])
@auth.login_required
@cache.cached()
def producao():
    """
    Endpoint para obter os dados de produção.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM producao"
        df = pd.read_sql(query, conn)
        conn.close()

        return df.to_json(orient='records', force_ascii=False), 200
    except Exception as e:
        return jsonify({"error": f"Falha ao obter os dados: {str(e)}"}), 500

@app.route('/api/processamento', methods=['GET'])
@auth.login_required
@cache.cached()
def processamento():
    """
    Endpoint para obter os dados de processamento.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM processamento"
        df = pd.read_sql(query, conn)
        conn.close()

        return df.to_json(orient='records', force_ascii=False), 200
    except Exception as e:
        return jsonify({"error": f"Falha ao obter os dados: {str(e)}"}), 500

@app.route('/api/comercializacao', methods=['GET'])
@auth.login_required
@cache.cached()
def comercializacao():
    """
    Endpoint para obter os dados de comercializacao.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM comercializacao"
        df = pd.read_sql(query, conn)
        conn.close()

        return df.to_json(orient='records', force_ascii=False), 200
    except Exception as e:
        return jsonify({"error": f"Falha ao obter os dados: {str(e)}"}), 500

@app.route('/api/importacao', methods=['GET'])
@auth.login_required
@cache.cached()
def importacao():
    """
    Endpoint para obter os dados de importacao.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM importacao"
        df = pd.read_sql(query, conn)
        conn.close()

        return df.to_json(orient='records', force_ascii=False), 200
    except Exception as e:
        return jsonify({"error": f"Falha ao obter os dados: {str(e)}"}), 500

@app.route('/api/exportacao', methods=['GET'])
@auth.login_required
@cache.cached()
def exportacao():
    """
    Endpoint para obter os dados de exportacao.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM exportacao"
        df = pd.read_sql(query, conn)
        conn.close()

        return df.to_json(orient='records', force_ascii=False), 200
    except Exception as e:
        return jsonify({"error": f"Falha ao obter os dados: {str(e)}"}), 500
