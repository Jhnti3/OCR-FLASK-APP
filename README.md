# 🧠 OCR - Extração de Texto de Imagens (Flask + Python)

Projeto simples e funcional para extrair texto de imagens usando OCR com **Python**, **Flask** e **Tesseract**.  
Você pode **colar um print (Ctrl+V)** ou **enviar uma imagem** e obter o texto extraído, direto pelo navegador.

---

## 🔍 Funcionalidades

- Upload de imagem (.png, .jpg, .jpeg)
- Colagem direta via **Ctrl+V** (clipboard)
- Visualização prévia da imagem colada
- Botão para **copiar o texto extraído**
- Interface leve, responsiva e limpa com CSS
- Integração com **Tesseract OCR**

---

## 📷 Exemplo de uso

1. Acesse o site local: `http://127.0.0.1:5000`
2. Faça o upload de uma imagem **ou apenas cole o print com Ctrl+V**
3. Clique em **Extrair Texto**
4. Veja o texto extraído em uma área de texto editável
5. Clique em **Copiar Texto** para usar como quiser

---

## 🛠 Tecnologias Utilizadas

- Python 3.11+
- Flask
- Tesseract OCR (v5.5+)
- Pillow (PIL)
- HTML5 + CSS3
- Font Awesome (ícones visuais)
- Git + GitHub

---

## ▶️ Como rodar localmente

### Pré-requisitos:
- Python instalado
- Git instalado
- Tesseract OCR instalado

### Passos:

```bash
# Clone o projeto
git clone https://github.com/Jhnti3/OCR-FLASK-APP.git
cd OCR-FLASK-APP

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows PowerShell
# ou
venv\Scripts\activate.bat  # CMD

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py

## 📂 Estrutura do Projeto

ocr/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── uploads/
│       └── (imagens temporárias)


📝 Autor
Desenvolvido por Johnata Boaventura Alves
GitHub • LinkedIn

📌 Observações
O arquivo clipboard.png é sobrescrito automaticamente a cada nova colagem de imagem.

As imagens são salvas em static/uploads/ temporariamente.

Para uso online, considere fazer deploy em serviços como Render, Hugging Face Spaces ou Heroku.
