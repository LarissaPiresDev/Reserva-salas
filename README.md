# 📚 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** que faz parte de um sistema maior de [School System](https://github.com/LarissaPiresDev/API---School-System)
, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se a **Turma** existe (`GET /turmas/<id>`)
- (Opcional) Se o **Aluno** existe (`GET /alunos/<id>`) – pode ser desativado se não usado.

---

## 🚀 Tecnologias Utilizadas

- Python
- Flask
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/LarissaPiresDev/Reserva-salas.git
cd Reserva-salas
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python .\api\app.py
```

A aplicação estará disponível em:
📍 `http://127.0.0.1:5001`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /reservas` – Lista todas as reservas
- `POST /reservas` – Cria uma nova reserva
- `GET /reservas/<id>` – Detalha uma reserva

### Exemplo de corpo JSON para criação:

```json
    {
        "data": "2025-07-10",
        "hora_fim": "10:00",
        "hora_inicio": "8:00",
        "sala": "101",
        "turma_id": 1
    }
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://127.0.0.1:5003
```

---

## 📦 Estrutura do Projeto

```
reserva-salas/
│
├── 📁 api/
│   ├── 📁 instance/
│   │   └── 🛢️ reserva.db
│   ├── 📁 reservasalas/
│   │   ├── 🐍 reserva_model.py
│   │   └── 🐍 reserva_routes.py
│   ├── 🐍 app.py
│   └── 🐍 config.py
│
├── 🐳 Dockerfile
├── 📄 requirements.txt
└── 📄 README.md
```
