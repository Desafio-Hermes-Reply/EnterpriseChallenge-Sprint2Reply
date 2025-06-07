# 📡 Sensor API - Django REST Framework

Uma API RESTful para gerenciamento de sensores, construída com **Django** e **Django REST Framework**.

---

## 🧱 Estrutura do Projeto

```bash
API\_REST/
├── api_sensor/         # App Django principal da API
│   ├── models.py       # Definição dos modelos (ex: Sensor)
│   ├── serializers.py  # Conversão de dados (JSON <-> Python)
│   ├── views.py        # Lógica das requisições (GET, POST)
│   ├── urls.py         # Rotas da aplicação
│   └── tests.py        # Testes automatizados
│
├── src/                # Configurações do projeto Django
│   ├── settings.py     # Configurações gerais
│   ├── urls.py         # URLs globais do projeto
│   ├── wsgi.py         # Interface WSGI para deploys
│   └── asgi.py         # Interface ASGI para deploys async
│
├── staticfiles/        # Arquivos estáticos (caso necessário)
├── db.sqlite3          # Banco de dados SQLite (dev)
├── requirements.txt    # Dependências do projeto
├── Procfile            # Arquivo necessário para o Heroku
├── runtime.txt         # Versão do Python no Heroku
├── .env                # Variáveis de ambiente (NÃO subir para o Git)
├── manage.py           # Comando de gerenciamento Django
└── README.md           # Este documento

````

---

## 🚀 Funcionalidades

- 🔹 Cadastro de sensores via método `POST`
- 🔹 Listagem de sensores via método `GET`
- 🔒 Validação de dados com serializers
- 🧪 Pronto para testes unitários e integração

---

## 📦 Instalação Local

1. Clone o repositório:

```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo
````

2. Crie um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:

```bash
   pip install -r requirements.txt
```

4. Aplique as migrações:

```bash
   python manage.py migrate
```

5. Rode o servidor local:

   ```bash
   python manage.py runserver
   ```

---

## 🌐 Rotas da API

| Método | Rota       | Descrição           |
| ------ | ---------- | ------------------- |
| GET    | `/sensor/` | Lista sensores      |
| POST   | `/sensor/` | Cria um novo sensor |

> As rotas estão registradas em `api_sensor/urls.py` e incluídas no roteador principal (`src/urls.py`).

---

## 🧪 Testes

Execute os testes com:

```bash
python manage.py test
```

---

## ☁️ Deploy no Heroku

### Pré-requisitos:

* Conta no Heroku
* Heroku CLI instalado

### Passos:

1. Faça login no Heroku CLI:

   ```bash
   heroku login
   ```

2. Crie um app:

   ```bash
   heroku create nome-do-app
   ```

3. Adicione o banco de dados (opcional):

   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. Faça o push do código:

   ```bash
   git push heroku main
   ```

5. Aplique as migrações no Heroku:

   ```bash
   heroku run python manage.py migrate
   ```

6. Acesse:

   ```bash
   heroku open
   ```

---

## ⚙️ Variáveis de Ambiente (.env)

Exemplo de `.env`:

```
SECRET_KEY=chave-secreta-do-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

> **Importante**: Nunca suba o `.env` para o GitHub.

---

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 🤝 Contribuindo

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue antes para discutir o que você gostaria de mudar.

---

## 📧 Contato

Seu Nome – [seuemail@exemplo.com](mailto:seuemail@exemplo.com)
LinkedIn / GitHub: [@seu-usuario](https://github.com/seu-usuario)
