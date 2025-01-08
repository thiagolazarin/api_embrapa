from flask import jsonify
from app import app, auth, cache
from app.utils.database import get_connection
import pandas as pd

@app.route('/')
@auth.login_required
@cache.cached()
def home():
    """
    Página inicial do projeto.
    ---
    responses:
      200:
        description: Retorna a mensagem da página inicial.
    """
    return "Projeto FIAP primeira etapa"

@app.route('/api/producao', methods=['GET'])
@auth.login_required
@cache.cached()
def producao():
    """
    Obter dados de produção.
    ---
    responses:
      200:
        description: Dados de produção retornados com sucesso.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
      500:
        description: Erro ao obter os dados de produção.
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
    Obter dados de processamento.
    ---
    responses:
      200:
        description: Dados de processamento retornados com sucesso.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
      500:
        description: Erro ao obter os dados de processamento.
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
    Obter dados de comercialização.
    ---
    responses:
      200:
        description: Dados de comercialização retornados com sucesso.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
      500:
        description: Erro ao obter os dados de comercialização.
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
    Obter dados de importação.
    ---
    responses:
      200:
        description: Dados de importação retornados com sucesso.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
      500:
        description: Erro ao obter os dados de importação.
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
    Obter dados de exportação.
    ---
    responses:
      200:
        description: Dados de exportação retornados com sucesso.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
      500:
        description: Erro ao obter os dados de exportação.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM exportacao"
        df = pd.read_sql(query, conn)
        conn.close()

        return df.to_json(orient='records', force_ascii=False), 200
    except Exception as e:
        return jsonify({"error": f"Falha ao obter os dados: {str(e)}"}), 500
