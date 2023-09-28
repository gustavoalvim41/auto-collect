## Sobre o projeto

O objetivo do projeto é automatizar o processo de coleta de informações de estabelecimentos a partir do Google e criar uma simples planilha no Excel contendo essas informações de forma organizada.

## Funcionalidades

* Entrada de Dados: O script permite ao usuário inserir o tipo de comércio e a cidade para realizar a pesquisa no Google.
* Pesquisa no Google: O script realiza uma pesquisa usando as informações fornecidas pelo usuário (por exemplo, "Loja de Roupas em Florianópolis").
* Web Scraping: O script utiliza técnicas de web scraping para extrair os resultados da pesquisa, incluindo nome do estabelecimento, endereço e telefone de contato.
* Coleta de Informações: As informações extraídas (nome, endereço e telefone) de todos os resultados da pesquisa são armazenadas em estruturas de dados adequadas.
* Criação da Tabela Excel: O script gera automaticamente uma simples planilha no Excel, onde cada linha corresponde a um estabelecimento e as colunas contêm as informações coletadas (nome, endereço e telefone).
* Manipulação de Erros: O script lida com possíveis cenários de erro durante o web scraping e a coleta de informações, garantindo que o processo seja robusto e confiável.

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: Git e Python.

## Instalação

Siga as instruções abaixo:
```bash
  # Clone este repositório
  $ git clone https://github.com/gustavoalvim41/auto-collect.git

  # Acesse a pasta do projeto no terminal/cmd
  $ cd auto-collect

  # Instale as dependências
  $ pip install -r requirements.txt

  # Certifique-se que o Python está corretamente instalado em sua máquina
  # Execute este comando no terminal/cmd para iniciar o projeto
  $ python3 main.py
```