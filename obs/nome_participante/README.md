# nome_participantes

Script para editar o html que será carregado ao OBS com o nome dos participantes.

## Pré-Requisitos

No folder onde se encontra nome_participantes.exe é preciso conter os seguintes arquivos:

### data.json

Arquivo .json aonde deve conter o nome do arquivo html para ser gerado e o nome do host/palestrante/convidado a ser inserido no html.

Ex.:

```json
{
    "Nome-Direita.html": "Este eh o nome da direita",
    "Nome-Esquerda.html": "Este eh o nome da esquerda",
    "Nome-Host.html": "Este eh o nome do Host",
    "Nome-Remoto-1.html": "Este eh o nome do Remoto-1",
    "Nome-Remoto-2.html": "Este eh o nome do Remoto-2",
    "Nome-Remoto-3.html": "Este eh o nome do Remoto-3",
    "Nome-Remoto-4.html": "Este eh o nome do Remoto-4"
}
```

Chaves com a keyword "Direita" (case sensitve), utilizaram o Template-Direita.html como base para criação do arquivo.

### Template.html

Arquivo do template html default que será replicado para criar os htmls especificados em data.json.

### Template-Direita.html

Arquivo do template html estiliados para a direita que será replicado para criar os htmls especificados em data.json.

Os arquivos Templates são separados no comentário `<!-- SPLIT -->` dentro deles.

## Uso

1. Configurar os arquivos de pré-requisito.
2. Executar o nome_participantes.exe

## Build

Feito com [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) utilizando as seguintes configurações:

```bash
pyinstaller --noconfirm --onefile --console --icon "path/to/ico" --name "nome_participantes"  "path/to/script"
```
