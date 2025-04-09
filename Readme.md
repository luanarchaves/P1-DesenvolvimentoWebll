# Trabalho para P1 de Desenvolvimento WebII

**Luana Chaves**  
**Vanessa Macedo**  

**Desenvolvimento de Software Multiplataforma – Fatec Itaquera**  

##  👩‍🎓​Integrantes
📧 luana.chaves@fatec.sp.gov.br  
📧 vanessa.macedo@fatec.sp.gov.br  

---

## 📘​ Resumo
Este projeto tem como objetivo o desenvolvimento de uma aplicação web utilizando a arquitetura **MVC** para gerenciar **produtos e usuários**. A aplicação permite operações **CRUD** (Cadastro, Leitura, Atualização e Exclusão) com dados armazenados em um banco **MySQL**. Foram criadas páginas específicas para o cadastro de produtos e usuários, com **validações rigorosas** antes da persistência dos dados. O projeto foi estruturado em pastas organizadas para **controllers, models, views, banco de dados e templates**, seguindo boas práticas de desenvolvimento. Durante a implementação, desafios como a **integração com o banco de dados** e a **validação de dados** foram superados através do estudo de documentação e refatoração de código. O resultado final foi uma aplicação **modular, funcional e escalável**.

## 🌎 Abstract
This project aims to develop a web application using the **MVC** architecture to manage **products and users**. The application enables **CRUD** (Create, Read, Update, and Delete) operations with data stored in a **MySQL database**. Dedicated pages were created for product and user registration, and all input data is strictly validated before being saved. The project structure was organized into specific folders for **controllers, models, views, database configuration, and templates**, following best development practices. During the implementation, challenges such as **database integration** and **input validation** were overcome through **documentation research** and **code refactoring**. The final result is a **modular, functional, and scalable application**.

---

## 🎯 Caso
Uma empresa está desenvolvendo um **sistema de gerenciamento de produtos** e precisa de uma aplicação que permita **cadastrar, atualizar, listar e excluir produtos**.

---

## 🛠 Desenvolvimento da Aplicação
A aplicação foi desenvolvida para permitir **o cadastro, atualização, listagem e exclusão de produtos e usuários**, seguindo a arquitetura **MVC** (**Model-View-Controller**). 

- **Banco de Dados:** MySQL
- **Arquitetura:** MVC
- **API:** RESTful

### 🔖​ Arquitetura MVC
A estrutura **MVC** garante organização e separação de responsabilidades:

- **Model:** Define as entidades **Produto** e **Usuário**, além de interagir diretamente com o **banco de dados**.
- **View:** Páginas principais para **cadastro de produtos e usuários**, conectadas aos controllers via **requisições HTTP**.
- **Controller:** Recebe as requisições, **valida os dados** e encaminha para o **Model**.

Essa divisão proporciona **manutenção, escalabilidade e reutilização de código**.

### ​🗂️​ Estrutura de Pastas do Projeto
A organização da estrutura de pastas facilita a **manutenção do código** e a colaboração entre desenvolvedores.

---

## ⚙️ Funcionalidades Desenvolvidas

### **🗃️​ CRUD de Produtos**
- `GET /produtos` → Retorna todos os produtos.
- `GET /produtos/{id}` → Retorna um produto específico.
- `POST /produtos` → Cria um novo produto com validação.
- `PUT /produtos/{id}` → Atualiza um produto existente.
- `DELETE /produtos/{id}` → Exclui um produto.

### **👤 CRUD de Usuários**
- `GET /usuarios` → Retorna todos os usuários.
- `GET /usuarios/{id}` → Retorna um usuário específico.
- `POST /usuarios` → Cria um novo usuário.
- `PUT /usuarios/{id}` → Atualiza um usuário existente.
- `DELETE /usuarios/{id}` → Exclui um usuário.

### ☑️​ **Validação dos Campos**
Antes de qualquer inserção ou atualização no banco de dados, os dados passam por validação:

#### **Produto**
- `nome:` Mínimo de **3 caracteres**.
- `preço:` Deve ser um **número positivo**.
- `estoque:` Deve ser um **inteiro maior ou igual a zero**.

#### **Usuário**
- Validação de **nome, e-mail e senha**, garantindo **integridade dos dados**.

Se houver erro, o sistema **retorna mensagens claras**, orientando o usuário na correção.

---

## ⁉️​ Dificuldades Encontradas e Soluções

🔹 **Integração com o Banco de Dados:** Inicialmente, houve dificuldades na configuração do **ORM** e na persistência dos dados. A solução foi **estudar a documentação** e configurar corretamente a **string de conexão**.

🔹 **Validação de Dados no Backend:** A validação antes de salvar exigiu uma organização no **Controller**. A solução foi criar **middlewares** para centralizar essas validações.

🔹 **Atualização e Exclusão de Registros:** Para evitar erros, foi implementada uma **verificação antes da alteração/exclusão**, retornando **404** caso o registro não existisse.

🔹 **Organização do Código:** O crescimento da aplicação tornou necessária a **refatoração** do projeto, separando **Controllers, Services, Models e Rotas**.

---

## 📚 Referências Utilizadas
- **Documentação oficial do MySQL:** [MySQL Docs](https://dev.mysql.com/doc/)  
- **Framework Backend FastAPI:** [FastAPI Docs](https://fastapi.tiangolo.com/)  
- **Artigo sobre arquitetura MVC:** [DIO - MVC](https://www.dio.me/articles/introducao-aos-padroes-de-arquitetura-mvc-model-view-controller-em-aplicacoes-java-web-c7cca2dfded8)

---

## 🏆 Conclusão
O desenvolvimento desta aplicação foi uma oportunidade prática de aplicar os princípios da **arquitetura MVC**, garantindo **organização, clareza e escalabilidade** ao projeto.

🔹 **Separação de camadas** tornou o código mais limpo e reutilizável.
🔹 **Estrutura bem definida** facilitou a leitura e manutenção do projeto.
🔹 **Validações rigorosas** garantiram **integridade dos dados**.

Desafios como **integração com MySQL** e **validações** foram superados, resultando em uma aplicação **robusta e preparada para evoluções futuras**. Além de fortalecer conhecimentos técnicos, este projeto proporcionou uma **visão prática do ciclo completo de uma aplicação web estruturada**.
