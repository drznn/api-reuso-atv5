# Projeto API de Cursos

## Descrição do Projeto
Este é um projeto de uma API RESTful para gerenciamento de cursos. A aplicação permite:
- **Criar** novos cursos.
- **Listar** todos os cursos ou um curso específico.
- **Atualizar** informações de cursos existentes.
- **Excluir** cursos.

### Proposta
O projeto feito em Python, utiliza Flask e Flask-RESTful para criar uma API organizada e escalável. O banco de dados é gerido com SQLite, e o código segue boas práticas de desenvolvimento, incluindo organização modular, tratamento de erros e uma base de dados inicial pré-populada.

---

## Pré-requisitos
Antes de começar, certifique-se de que você possui as ferramentas abaixo instaladas:
- **Python** (versão 3.8 ou superior)
- **Insomnia/Postman** (ou outro cliente HTTP para testar a API)

---

## Configuração do Projeto

### Passo 1: Clonar o Repositório
Clone o repositório para sua máquina local:
```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_REPOSITORIO>
```

### Passo 2: Criar o Ambiente Virtual
Crie e ative um ambiente virtual:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/MacOS:
source venv/bin/activate
```
### Passo 3: Instalar as Dependências
Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

### Passo 1: Iniciar o Servidor
Execute o servidor localmente:
```bash
python run.py
```

O servidor estará disponível no endereço: http://127.0.0.1:5000

## Testando a API

### Rotas da API

1. Listar Todos os Cursos

Método: GET

URL: http://127.0.0.1:5000/cursos

Resposta:

```json
[
    {
        "id": 1,
        "titulo": "Engenharia de Software",
        "descricao": "Curso avançado de desenvolvimento",
        "carga_horaria": 200
    },
    {
        "id": 2,
        "titulo": "Design Digital",
        "descricao": "Curso sobre design gráfico e digital",
        "carga_horaria": 150
    }
]
```
2. Listar um Curso Específico

Método: GET

URL: http://127.0.0.1:5000/cursos/<ID_DO_CURSO>

Exemplo de URL: http://127.0.0.1:5000/cursos/1


3. Criar um Novo Curso

Método: POST

URL: http://127.0.0.1:5000/cursos

Corpo da Requisição (JSON):

```json
{
    "titulo": "Curso de Python",
    "descricao": "Aprenda Python do básico ao avançado",
    "carga_horaria": 100
}
```

4. Atualizar um Curso

Método: PUT

URL: http://127.0.0.1:5000/cursos/<ID_DO_CURSO>

Corpo da Requisição (JSON):

```json

{
    "titulo": "Curso de Python Avançado",
    "descricao": "Curso para desenvolvedores experientes",
    "carga_horaria": 120
}
```

5. Deletar um Curso

Método: DELETE

URL: http://127.0.0.1:5000/cursos/<ID_DO_CURSO>


### Estrutura do Projeto
A estrutura de diretórios está organizada como segue:

```bash
ATV5/
├── app/
│   ├── __init__.py         # Configuração do Flask e inicialização do banco de dados
│   ├── models.py           # Modelo do banco de dados
│   ├── routes.py           # Configuração das rotas
│   ├── resources/
│   │   ├── __init__.py
│   │   └── curso.py        # Lógica das operações de API para cursos
├── client/
│   └── cliente.py          # Cliente para consumir a API
├── instance/
│   └── cursos.db           # Banco de dados SQLite
├── migrations/             # Pasta reservada para futuras migrações
├── tests/                  # Pasta reservada para testes automatizados
├── venv/                   # Ambiente virtual
├── .gitignore              # Arquivos ignorados pelo Git
├── LICENSE                 # Licença do projeto
├── README.md               # Este arquivo
└── run.py                  # Arquivo principal para rodar o servidor
```

## Boas Práticas Implementadas
Organização Modular:
Separação de responsabilidades em arquivos dedicados para rotas, modelos e recursos.

Tratamento de Erros:
Retorno de mensagens claras para erros, como curso não encontrado ou dados inválidos.

Pré-população do Banco:
Dois cursos padrão são criados automaticamente ao iniciar o projeto pela primeira vez.

Comando Personalizado:
Um comando específico (flask recriar_banco) foi criado para facilitar a reinicialização do banco.

## Licença
Este projeto está licenciado sob a GNU General Public License v3.0. Consulte o arquivo LICENSE para obter mais detalhes sobre os termos de uso e redistribuição.


