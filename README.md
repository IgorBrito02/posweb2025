# 📊 Posweb2025

Projeto de integração entre **MySQL** e **MongoDB** com **Flask**, implementando um sistema simples de **Clientes, Produtos e Vendas** com dashboard consolidado no MongoDB.

---

## 🚀 Descrição
Este projeto demonstra um **sistema backend** usando Flask, com:
- Persistência de dados em banco **relacional (MySQL)** para o CRUD de clientes, produtos e vendas.  
- Um banco **NoSQL (MongoDB)** para armazenar dados consolidados em um dashboard.  
- Testes realizados com **Postman**, **MySQL Workbench** e **MongoDB Compass**.

---

## 🔑 Funcionalidades
- CRUD completo para **Clientes, Produtos e Vendas**.  
- **Rotas RESTful** com JSON para integração fácil.  
- **Atualização automática** do dashboard no MongoDB após alterações no SQL.  
- Dashboard com estatísticas como:  
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
- Postman  
- MySQL Workbench  
- MongoDB Compass  

---

## 📂 Estrutura do projeto
```
app/
 ├── main.py          # API Flask com rotas CRUD
 ├── models.py        # Modelos do banco SQL
 ├── sql_service.py   # Serviços para manipulação dos dados SQL
 ├── nosql_service.py # Serviços para manipulação dos dados MongoDB
 ├── config.py        # Configurações dos bancos de dados
 └── init_db.py       # Script para criar tabelas no MySQL

requirements.txt      # Dependências Python
```

---

## ▶️ Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/IgorBrito02/posweb2025.git
cd posweb2025
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure os bancos de dados:
- **MySQL**: Crie um banco chamado `bdpos` e ajuste o usuário/senha no arquivo `app/config.py`.  
- **MongoDB**: Certifique-se de que o serviço está rodando em `mongodb://localhost:27017`.  

5. Crie as tabelas no MySQL:
```bash
python -m app.init_db
```

6. Rode o servidor Flask:
```bash
python -m app.main
```

O servidor estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Endpoints principais

### 📌 Clientes
- `GET /clientes` → Lista clientes  
- `POST /clientes` → Cria cliente  
- `GET /clientes/<id>` → Obtém cliente  
- `PUT /clientes/<id>` → Atualiza cliente  
- `DELETE /clientes/<id>` → Deleta cliente  

### 📌 Produtos
- `GET /produtos` → Lista produtos  
- `POST /produtos` → Cria produto  
- `PUT /produtos/<id>` → Atualiza produto  
- `DELETE /produtos/<id>` → Deleta produto  

### 📌 Vendas
- `GET /vendas` → Lista vendas  
- `POST /vendas` → Cria venda  
- `GET /vendas/<id>` → Obtém venda  
- `PUT /vendas/<id>` → Atualiza venda  
- `DELETE /vendas/<id>` → Deleta venda  

### 📌 Dashboard (MongoDB)
- `GET /dashboard/total_clientes` → Retorna total de clientes  
- `GET /dashboard/geral` → Retorna estatísticas gerais (totais e produto mais vendido)  

---

📌 Projeto desenvolvido na disciplina **Bancos de Dados (POSWeb2025)**.  