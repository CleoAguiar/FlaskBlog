from flask import Flask

app = Flask(__name__)

# Imports at the bottom avoids the error that results from 
# the mutual references between these two files
from app import routes
