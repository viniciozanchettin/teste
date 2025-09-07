# Flask Web App (Exemplo)

Pequena aplicação web em **Flask** com templates Jinja2, testes e CI.

## 🚀 Rodando localmente
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app.app run --debug
```
Acesse: http://127.0.0.1:5000

## ✅ Testes
```bash
python -m unittest -v
```

## 🐳 Docker
```bash
docker build -t flask-web-app .
docker run -p 8000:8000 flask-web-app
```
Então acesse: http://127.0.0.1:8000

## 🌐 Deploy simples (gunicorn)
O Dockerfile já usa `gunicorn` ouvindo na porta 8000.