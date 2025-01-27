import axios

base_url = "http://127.0.0.1:5000/cursos"

def listar_cursos():
    """Lista todos os cursos disponíveis."""
    try:
        response = axios.get(base_url)
        print(response.json())
    except Exception as e:
        print(f"Erro ao listar cursos: {str(e)}")

def adicionar_curso():
    """Adiciona um novo curso ao sistema."""
    curso = {
        "titulo": "Python",
        "descricao": "Curso básico",
        "carga_horaria": 40
    }
    try:
        response = axios.post(base_url, json=curso)
        print(response.json())
    except Exception as e:
        print(f"Erro ao adicionar curso: {str(e)}")

listar_cursos()
adicionar_curso()
