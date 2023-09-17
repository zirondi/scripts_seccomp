# %%
import json
import ctypes
import os
import sys

# %%
FNAME = 'data.json'
FNAME_HMTL = [
    'Nome-Direita.html', 
    'Nome-Esquerda.html', 
    'Nome-Host.html',
    'Nome-Remoto-1.html', 
    'Nome-Remoto-2.html',
    'Nome-Remoto-3.html', 
    'Nome-Remoto-4.html'
    ]
CURR_FOLDER = os.path.abspath('')

# %%
def validate_files():
    if not os.path.isfile(FNAME):
        ctypes.windll.user32.MessageBoxW(0, u"Arquivo data.json nao econtrado.", u"Erro", 0)
    for html_file in FNAME_HMTL:
        if not os.path.isfile(html_file):
            ctypes.windll.user32.MessageBoxW(0, u"Arquivo {} nao econtrado.".format(html_file), u"Erro", 0)

def validate_dict(data: dict):
    with open(FNAME, 'r') as f:
        data = json.load(f)
        for key in data:
            if key not in FNAME_HMTL:
                ctypes.windll.user32.MessageBoxW(0, f"Ha um erro na chave {key} em data.json.", u"Erro", 0)
                sys.exit(1)
    


# %%
if True:#__name__ == '__main__':
    data = {}
    validate_files()
    validate_dict(data)
    print(data)


