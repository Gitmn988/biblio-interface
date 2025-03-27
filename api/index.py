import logging
import traceback
import os
import sys

# Configurazione del logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    logger.debug("Inizializzazione dell'handler Vercel")
    
    # Aggiungi la directory principale al path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    sys.path.insert(0, root_dir)
    logger.debug(f"Cartella corrente: {current_dir}")
    logger.debug(f"Directory root: {root_dir}")
    logger.debug(f"Path di sistema: {sys.path}")

    # Importa l'app Flask
    from api.app import app
    logger.debug("App importata con successo")
    
    # Necessario per Vercel
    handler = app
    logger.debug("Handler configurato correttamente")

except Exception as e:
    logger.critical(f"Errore durante l'inizializzazione: {str(e)}")
    logger.critical(traceback.format_exc())
    
    from flask import Flask, jsonify
    
    # Crea un'app Flask di emergenza
    app = Flask(__name__)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        error_info = {
            "error": f"Errore critico nell'inizializzazione: {str(e)}",
            "traceback": traceback.format_exc(),
            "path": path,
            "environment": dict(os.environ)
        }
        return jsonify(error_info), 500
    
    handler = app