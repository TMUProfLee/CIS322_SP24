import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../"))

#from source.CardGames import *
from source.flask_file import app
from source import templates