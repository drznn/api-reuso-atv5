import axios

base_url = "http://127.0.0.1:5000/cursos"

def listar_cursos():
    response = axios.get(base_url)
    print(response.json())

def adicionar_curso():
    curso = {
        "titulo": "Python Básico",
        "descricao": "Curso introdutório de Python",
        "carga_horaria": 40
    }
    response = axios.post(base_url, json=curso)
    print(response.json())

listar_cursos()
adicionar_curso()
