# 🧠 TechFit Blog

Blog desenvolvido com **Django** que une dois universos: **tecnologia e fitness**.
O projeto faz parte do meu portfólio como desenvolvedor e explora como inovação, IA e desenvolvimento de software estão transformando o mundo do treinamento físico.

---

## 🚀 Tecnologias utilizadas

* Python
* Django
* Bootstrap
* HTML / CSS
* SQLite
* Git e GitHub

---

## 📚 Funcionalidades

✔️ Listagem de posts
✔️ Página individual de cada artigo
✔️ Sistema de **tempo estimado de leitura**
✔️ Upload de imagens nos posts
✔️ Layout responsivo com Bootstrap
✔️ Estrutura preparada para expansão do blog

---

## 🧩 Estrutura do projeto

```
blog/
│
├── config/        # Configurações do projeto Django
├── posts/         # App responsável pelos posts
│
├── templates/     # Templates HTML
├── static/        # Arquivos estáticos (CSS, JS)
├── media/         # Upload de imagens
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Como rodar o projeto localmente

Clone o repositório:

```
git clone https://github.com/seuusuario/blog-techfit.git
```

Entre na pasta do projeto:

```
cd blog-techfit
```

Crie o ambiente virtual:

```
python -m venv venv
```

Ative o ambiente virtual:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

Execute as migrations:

```
python manage.py migrate
```

Inicie o servidor:

```
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## 🎯 Objetivo do projeto

Este projeto foi criado para:

* praticar desenvolvimento web com Django
* explorar integração entre **tecnologia e fitness**
* construir um **projeto real de portfólio**

---

## 👨‍💻 Autor

**Matheus Batista**

Desenvolvedor em formação com interesse em:

* Desenvolvimento Backend
* Inteligência Artificial
* Tecnologia aplicada ao Fitness

---

## 📌 Futuras melhorias

* Sistema de comentários
* Tags e categorias
* Busca de posts
* SEO para blog
* Deploy em produção
* Integração com APIs de IA
