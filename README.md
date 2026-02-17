# Gen-qrcode

## 📋 Descrição

Gen-qrcode é um utilitário em Python que converte o conteúdo de arquivos de texto em códigos QR. O script lê um arquivo especificado pelo usuário e gera uma imagem PNG contendo o QR code com o texto do arquivo.

## 🚀 Funcionalidades

- **Validação automática de dependências**: O script verifica e instala automaticamente as dependências necessárias
- **Entrada interativa**: Solicita ao usuário o nome do arquivo a ser convertido
- **Geração de QR code**: Converte o conteúdo do arquivo em um código QR
- **Saída em PNG**: Salva o QR code como imagem PNG

## ⚙️ Como Funciona

1. Verifica se as dependências (`wheel`, `pillow`, `qrcode`) estão instaladas
2. Instala automaticamente qualquer dependência faltante via pip
3. Solicita ao usuário o nome do arquivo de entrada
4. Lê o conteúdo completo do arquivo em UTF-8
5. Gera um QR code com o conteúdo
6. Salva o QR code como `{nome_arquivo}-qrcode.png`

## 📦 Dependências

- **qrcode**: Biblioteca para gerar códigos QR
- **pillow**: Biblioteca para manipulação de imagens
- **wheel**: Ferramentas para distribuição de pacotes Python

As dependências são instaladas automaticamente na primeira execução, caso não estejam presentes.

## 🔧 Como Usar

```bash
python Gen-qrcode.py
```

O script pedirá o nome do arquivo:
```
Digitie o nome do arquivo: seu_arquivo.txt
QRCode Criado
Presione [Enter] para sair!
```

O arquivo `seu_arquivo-qrcode.png` será criado no diretório atual.

## 📝 Exemplo

Se você possuir um arquivo `dados.txt` com conteúdo:
```
https://www.exemplo.com
```

Ao executar o script e informar `dados.txt`, será gerado `dados-qrcode.png` contendo o QR code da URL.