import os
import shutil

downloads = os.path.join(os.path.expanduser("~"), "Downloads")

tipos = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".jfif"],
    "Documentos": [".doc", ".docx", ".txt"],
    "PDFs": [".pdf"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi"],
    "Musica": [".mp3", ".wav"],
}

for arquivo in os.listdir(downloads):
    caminho_arquivo = os.path.join(downloads, arquivo)

    if os.path.isfile(caminho_arquivo):

        movido = False

        for pasta, extensoes in tipos.items():
            for ext in extensoes:
                if arquivo.lower().endswith(ext):

                    pasta_destino = os.path.join(downloads, pasta)

                    if not os.path.exists(pasta_destino):
                        os.mkdir(pasta_destino)

                    shutil.move(caminho_arquivo, os.path.join(
                        pasta_destino, arquivo))
                    movido = True
                    break

            if movido:
                break

        if not movido:
            outros = os.path.join(downloads, "Outros")
            if not os.path.exists(outros):
                os.mkdir(outros)

            shutil.move(caminho_arquivo, os.path.join(outros, arquivo))

print("Downloads organizados.")
