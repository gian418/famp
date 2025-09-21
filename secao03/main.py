from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programção para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programção",
        "aulas": 87,
        "horas": 67
    }
}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)