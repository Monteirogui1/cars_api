<h1 align="center"> API de Carros </h1>

Este projeto é uma API desenvolvida com Django REST framework para gerenciar marcas, modelos e carros, além de permitir a realização de reviews dos carros cadastrados.

## Funcionalidades

- **Cadastro de Marcas, Modelos e Carros**: Permite o registro de informações detalhadas sobre marcas, modelos e carros.
- **Reviews de Carros**: Usuários podem adicionar reviews para os carros, incluindo uma nota.
- **Cálculo de Média de Notas**: A API calcula a média das notas dos reviews para cada carro.
- **Segurança JWT**: Todas as requisições são protegidas por autenticação JWT.

## Instalação

**1. Clone o repositório**:

      ```bash
      git clone https://github.com/Monteirogui1/cars_api.git
      cd cars-api

**2. Crie um ambiente virtual e ative-o**:</br>

      python -m venv env
      source env/bin/activate  # No Windows, use `env\Scripts\activate`

**3. Instale as dependências:**</br>

      pip install -r requirements.txt

**4. Execute as migrações:**</br>

      python manage.py migrate
      python manage.py makemigrations

**5. Inicie o servidor de desenvolvimento:**</br>

	 python manage.py runserver


**Endpoints:**</br>
      api/v1/brand/: CRUD para marcas de carros.</br>
      api/v1/type/: CRUD para modelos de carros.</br>
      api/v1/cars/: CRUD para carros.</br>
      api/v1/reviews/: CRUD para reviews de carros.</br>


**Autenticação**</br>
A API utiliza JWT para autenticação. Para acessar os endpoints protegidos, é necessário incluir o token JWT no header das requisições:</br>
      Authorization: Bearer <seu_token_jwt></br>
