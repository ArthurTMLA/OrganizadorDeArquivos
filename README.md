📂 Downloads Organizer
------------------------------------------------------------------------------------------------------------------
Script em Python que organiza automaticamente os arquivos da pasta Downloads com base no tipo de arquivo.

Ele cria pastas automaticamente e move os arquivos para suas respectivas categorias.

🚀 Funcionalidades
------------------------------------------------------------------------------------------------------------------
Organiza arquivos automaticamente por formato

Cria pastas caso elas não existam

Funciona em qualquer computador com Python

Fácil de modificar e adicionar novos formatos

Código simples e didático

🗂 Estrutura criada
------------------------------------------------------------------------------------------------------------------
Exemplo de como sua pasta Downloads pode ficar após rodar o script:

Downloads
 
 ├── Imagens
 
 ├── Documentos
 
 ├── PDFs
 
 ├── Planilhas
 
 ├── Compactados

 ├── Programas
 
 ├── Musica
 
 └── Outros

⚙️ Como funciona
------------------------------------------------------------------------------------------------------------------
O script:

Localiza a pasta Downloads do usuário.

Verifica todos os arquivos dentro dela.

Identifica a extensão do arquivo.

Move o arquivo para a pasta correspondente.
_______________________________________________


*Trecho principal do código:*
```
for arquivo in os.listdir(downloads):
```
*Isso percorre todos os arquivos da pasta.*

_______________________________________________



*Depois o script verifica a extensão:*
```
if arquivo.lower().endswith(ext):
```
_______________________________________________
*Se a extensão corresponder, o arquivo é movido:*
```
shutil.move(caminho_arquivo, destino)
```
_______________________________________________
📦 Categorias de arquivos
------------------------------------------------------------------------------------------------------------------
| Pasta       | Extensões                 |
| ----------- | ------------------------- |
| Imagens     | png, jpg, jpeg, gif, webp |
| Documentos  | doc, docx, txt            |
| PDFs        | pdf                       |
| Planilhas   | xls, xlsx, csv            |
| Compactados | zip, rar, 7z              |
| Programas   | exe, msi                  |
| Musica      | mp3, wav                  |
| Outros | Arquivos não presentes no dicionario 'TIPOS' |

🔧 Personalizando para outras pastas
------------------------------------------------------------------------------------------------------------------
Você pode organizar qualquer pasta, não apenas Downloads.

Basta alterar esta linha:
```
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
```
Exemplo para Desktop:
```
downloads = os.path.join(os.path.expanduser("~"), "Desktop")
```
Exemplo para uma pasta específica:
```
downloads = r"C:\Users\Arthur\Documents"
```

➕ Adicionando novos tipos de arquivos
----
Os formatos ficam dentro do dicionário tipos.

Exemplo:

"Videos": [".mp4", ".mkv", ".avi"]

Exemplo completo:

tipos = {
    "Videos": [".mp4", ".mkv", ".avi"],
}

💡 Melhorias futuras
------------------------------------------------------------------------------------------------------------------
Interface gráfica

Organização automática em tempo real

Log de arquivos movidos

Ignorar arquivos duplicados

Suporte para Linux e Mac

📚 Tecnologias usadas
------------------------------------------------------------------------------------------------------------------
Python

os

shutil

👨‍💻 Autor
------------------------------------------------------------------------------------------------------------------
Arthur de Araújo Santos


