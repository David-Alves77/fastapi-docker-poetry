
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas com Docker")

tarefas = {}


class Tarefa(BaseModel):
    nome: str
    concluida: bool = False


@app.get("/")
def inicio():
    return {"mensagem": "API funcionando com Docker!"}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    identificador = max(tarefas.keys(), default=0) + 1
    tarefas[identificador] = tarefa.model_dump()
    return {"id": identificador, "tarefa": tarefas[identificador]}


@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    del tarefas[tarefa_id]
    return {"mensagem": "Tarefa excluída"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas com Docker")

tarefas = {}


class Tarefa(BaseModel):
    nome: str
    concluida: bool = False


@app.get("/")
def inicio():
    return {"mensagem": "API funcionando com Docker!"}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    identificador = max(tarefas.keys(), default=0) + 1
    tarefas[identificador] = tarefa.model_dump()
    return {"id": identificador, "tarefa": tarefas[identificador]}


@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    del tarefas[tarefa_id]
    return {"mensagem": "Tarefa excluída"}
