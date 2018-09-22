from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Imports at the bottom avoids the error that results from 
# the mutual references between these two files
from app import routes
