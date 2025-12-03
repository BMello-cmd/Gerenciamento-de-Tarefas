from sqlalchemy.orm import Session
from app.models.tarefa_model import Tarefa, TarefaPrioritaria

def listar_tarefas(db: Session):
    tarefas = db.query(Tarefa).all()
    return [t.to_dict() for t in tarefas]

def criar_tarefa(db: Session, titulo: str, descricao: str, prioridade: str, prazo: str = None):
    
    query = db.query(Tarefa).filter(Tarefa.titulo == titulo)

    if prazo:
        query = query.filter(Tarefa.prazo == prazo)
    else:
        query = query.filter(Tarefa.prazo.is_(None))
        
    tarefa_encontrada = query.first()

    if tarefa_encontrada:
        raise ValueError("Já existe uma tarefa com o mesmo Título e Prazo.")
    
    if prazo:
        nova_tarefa = TarefaPrioritaria(titulo=titulo, descricao=descricao, prioridade=prioridade, prazo=prazo)
        nova_tarefa.tipo = "prioritaria"
    else:
        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, prioridade=prioridade, tipo="comum")

    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    
    return nova_tarefa.to_dict()

def atualizar_status(db: Session, tarefa_id: int, novo_status: str):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    
    if tarefa:
        tarefa.status = novo_status
        db.commit()
        db.refresh(tarefa)
        return tarefa.to_dict()
    return None

def buscar_por_id(db: Session, tarefa_id: int):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    
    if not tarefa:
        raise ValueError("Tarefa não encontrada.")
    
    return tarefa.to_dict()

def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    
    if tarefa:
        db.delete(tarefa)
        db.commit()
    return {"msg": "Deletado"}