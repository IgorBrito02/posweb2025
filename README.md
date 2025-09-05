# 📊 Posweb2025

Projeto de integração entre **MySQL** e **MongoDB** com **Flask**, implementando um sistema simples de **Clientes, Produtos e Vendas** com dashboard consolidado no MongoDB.

---

## 🚀 Descrição
Este projeto demonstra um **sistema backend** usando Flask, com:

- Persistência de dados em banco **relacional (MySQL)** para o CRUD de clientes, produtos e vendas.  
- Um banco **NoSQL (MongoDB)** para armazenar dados consolidados em um dashboard.  
- Testes realizados com **Postman**, **MySQL Workbench** e **MongoDB Compass**.

Serve como **exemplo de integração SQL + NoSQL** e construção de dashboards dinâmicos.

---

## 🔑 Funcionalidades

- CRUD completo para **Clientes, Produtos e Vendas**.  
- **Rotas RESTful** com JSON para integração fácil.  
- **Atualização automática** do dashboard no MongoDB após alterações no SQL.  
- Dashboard com estatísticas:
  - Total de clientes  
  - Total de produtos  
  - Total de vendas  
  - Produto mais vendido  
- Integração **SQL (MySQL) + NoSQL (MongoDB)**.

---

## 🛠 Tecnologias utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy  
- PyMySQL  
- PyMongo  
- MySQL  
- MongoDB  
- Postman / Insomnia  
- MySQL Workbench  
- MongoDB Compass  

---

## 📂 Estrutura do projeto

```
posweb2025/
├── app/
│   ├── main.py          # API Flask com rotas CRUD
│   ├── models.py        # Modelos do banco SQL
│   ├── sql_service.py   # Serviços para manipulação dos dados SQL
│   ├── nosql_service.py # Serviços para manipulação dos dados MongoDB
│   ├── config.py        # Configurações dos bancos de dados
│   └── init_db.py       # Script para criar tabelas no MySQL
├── requirements.txt     # Dependências Python
└── README.md
```

---

## ▶️ Como rodar o projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/IgorBrito02/posweb2025.git
cd posweb2025
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure os bancos de dados:**
- **MySQL:** Crie um banco chamado `bdpos` e ajuste usuário/senha em `app/config.py`.  
- **MongoDB:** Certifique-se de que o serviço está rodando (`mongodb://localhost:27017`).

5. **Crie as tabelas no MySQL:**
```bash
python -m app.init_db
```

6. **Rode o servidor Flask:**
```bash
python -m app.main
```

Servidor disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Endpoints principais

### 📌 Clientes
- **GET /clientes** → Lista todos os clientes  
- **POST /clientes** → Cria cliente  
```json
{
  "nome": "João",
  "email": "joao@email.com",
  "cpf": "12345678901",
  "data_nascimento": "1995-05-10"
}
```
- **GET /clientes/<id>** → Obtém cliente por ID  
- **PUT /clientes/<id>** → Atualiza cliente  
```json
{
  "nome": "João da Silva"
}
```
- **DELETE /clientes/<id>** → Deleta cliente  

### 📌 Produtos
- **GET /produtos** → Lista todos os produtos  
- **POST /produtos** → Cria produto  
```json
{
  "nome": "Notebook",
  "preco": 2500,
  "descricao": "Dell i5",
  "categoria": "Informática"
}
```
- **PUT /produtos/<id>** → Atualiza produto  
- **DELETE /produtos/<id>** → Deleta produto  

### 📌 Vendas
- **GET /vendas** → Lista todas as vendas  
- **POST /vendas** → Cria venda  
```json
{
  "id_cliente": 1,
  "id_produto": 1,
  "valor_total": 2500
}
```
- **GET /vendas/<id>** → Obtém venda por ID  
- **PUT /vendas/<id>** → Atualiza venda  
- **DELETE /vendas/<id>** → Deleta venda  

### 📌 Dashboard (MongoDB)
- **GET /dashboard/total_clientes** → Total de clientes  
- **GET /dashboard/geral** → Estatísticas gerais (totais e produto mais vendido)  

> ⚡ Observação: Após criar clientes, produtos e vendas, o dashboard é atualizado automaticamente no MongoDB Compass (`vendas > dashboard`).

---

## ✅ Testes realizados

- CRUD completo de clientes, produtos e vendas usando Postman e Insomnia  
- Verificação de dados consolidados no **MongoDB Compass**  
- Confirmação da persistência no **MySQL Workbench**  

---

📌 Projeto desenvolvido na disciplina **Bancos de Dados (posweb2025)**.