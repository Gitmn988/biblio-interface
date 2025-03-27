import sys
import os

# Aggiungi la directory principale al path per permettere l'importazione di moduli
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa l'app Flask
from app import app

# Questa è la funzione che Vercel cercherà
def handler(request, **kwargs):
    # Creiamo una risposta WSGI
    return app