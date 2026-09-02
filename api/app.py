from flask import Flask, jsonify
import os
import pymysql

HARDCODED_PASSWORD = "SuperSecretPassword123!"

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'adso_user'),
        password=os.environ.get('DB_PASSWORD', 'adso_password'),
        database=os.environ.get('DB_NAME', 'adso_db')
    )

@app.route('/')
def home():
    return jsonify({"status": "success", "message": "API ADSO Operativa"}), 200

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "UP", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "DOWN", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
