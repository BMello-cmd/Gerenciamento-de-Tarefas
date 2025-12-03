from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.services.tarefa_service as service

router = APIRouter()

@router.get("/tarefas/")
def listar(db: Session = Depends(get_db)):
    return service.listar_tarefas(db)

@router.post("/tarefas/")
def criar(titulo: str, descricao: str, prioridade: str, prazo: str = None, db: Session = Depends(get_db)):
    return service.criar_tarefa(db, titulo, descricao, prioridade, prazo)

@router.get("/tarefas/{id}")
def exibir_detalhes(id: int, db: Session = Depends(get_db)):
    try:
        return service.buscar_por_id(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put("/tarefas/{id}")
def atualizar(id: int, status: str, db: Session = Depends(get_db)):
    return service.atualizar_status(db, id, status)

@router.delete("/tarefas/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    return service.deletar_tarefa(db, id)

