import sys
import subprocess
import pkg_resources

required = {'wheel','pillow', 'qrcode'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
try:
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
except:
    exit()

try:
    import qrcode
except ImportError as e:
    input("Falha ao importar paocte qrcode")
    exit()

print("Gen-qrcode")

nomeArquivo = input('Digite o nome do arquivo: ')

nomeArquivoQrCode = nomeArquivo.split('.')[0]+"-qrcode"

try:
    arquivo = open(nomeArquivo,'r',encoding='utf8')
except:
    exit()

texto = arquivo.read()

arquivo.close()

img = qrcode.make(texto)
type(img)
img.save(nomeArquivoQrCode+".png")

print("QRCode Criado")
input("Presione [Enter] para sair!")