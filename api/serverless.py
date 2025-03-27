from flask import Flask
import os
import sys

# Aggiungi la directory principale al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa la tua app Flask
from app import app as flask_app

def handler(request, **kwargs):
    return flask_app