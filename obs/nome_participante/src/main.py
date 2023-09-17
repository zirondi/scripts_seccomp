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
FNAME_TEMPLATE = 'Template.html'

# %%
# functions

def validate_files():
    if not os.path.isfile(FNAME_DATA):
        ctypes.windll.user32.MessageBoxW(0, "Arquivo data.json nao econtrado.", "Erro", ICON_EXCLAIM | MB_OK)
        sys.exit(1)

    if not os.path.isfile(FNAME_TEMPLATE):
        ctypes.windll.user32.MessageBoxW(0, "Arquivo Template.html nao econtrado.", "Erro", ICON_EXCLAIM | MB_OK)
        sys.exit(1)

def get_htmls() -> list:
    with open(FNAME_TEMPLATE, 'r') as f:
        html = f.read()
    return html.split('<!-- SPLIT -->')
    
def make_html(html_upper: str, html_lower: str):
    with open(FNAME_DATA, 'r') as f:
        data = json.load(f)
    
    for key in data:
        with open(key, 'w') as f:
            f.write(html_upper)
            f.write(data[key])
            f.write(html_lower)
    
    ctypes.windll.user32.MessageBoxW(0, f"Arquivo(s) alterados com sucesso!", u"Sucesso!", ICON_INFO | MB_OK)
    
# %%
# main
if __name__ == '__main__':
    validate_files()
    html_upper, html_lower = get_htmls()
    make_html(html_upper, html_lower)
    


