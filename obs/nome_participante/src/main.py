# %%
import json
import ctypes
import os
import sys

# %%
# buttons

MB_OK = 0x0

# icons

ICON_EXCLAIM = 0x30
ICON_INFO = 0x40

# %%
# consts

FNAME_DATA = 'data.json'
FNAME_TEMPLATE_DEFAULT = 'Template.html'
FNAME_TEMPLATE_DIREITA = 'Template-Direita.html'

# %%
# functions

def validate_files() -> None:
    if not os.path.isfile(FNAME_DATA):
        ctypes.windll.user32.MessageBoxW(0, "Arquivo data.json nao econtrado.", "Erro", ICON_EXCLAIM | MB_OK)
        sys.exit(1)

    if not os.path.isfile(FNAME_TEMPLATE_DEFAULT):
        ctypes.windll.user32.MessageBoxW(0, f"Arquivo {FNAME_TEMPLATE_DEFAULT} nao econtrado.", "Erro", ICON_EXCLAIM | MB_OK)
        sys.exit(1)

    if not os.path.isfile(FNAME_TEMPLATE_DIREITA):
        ctypes.windll.user32.MessageBoxW(0, f"Arquivo {FNAME_TEMPLATE_DIREITA} nao econtrado.", "Erro", ICON_EXCLAIM | MB_OK)
        sys.exit(1)

def get_htmls() -> list:
    with open(FNAME_TEMPLATE_DEFAULT, 'r') as f:
        html_default = f.read()
    
    with open(FNAME_TEMPLATE_DIREITA, 'r') as f:
        html_direita = f.read()
    
    return html_default.split('<!-- SPLIT -->'), html_direita.split('<!-- SPLIT -->')
    
def make_html(htmls: list) -> None:
    with open(FNAME_DATA, 'r') as f:
        data = json.load(f)
    
    for key in data:
        if not 'Direita' in key:
            with open(key, 'w') as f:
                f.write(htmls[0][0])
                f.write(data[key])
                f.write(htmls[0][1])
        else:
            with open(key, 'w') as f:
                f.write(htmls[1][0])
                f.write(data[key])
                f.write(htmls[1][1])
    
    ctypes.windll.user32.MessageBoxW(0, f"Arquivo(s) alterados com sucesso!", u"Sucesso!", ICON_INFO | MB_OK)

# %%
# main
if __name__ == '__main__':
    validate_files()
    htmls = get_htmls()
    make_html(htmls)


