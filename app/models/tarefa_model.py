from sqlalchemy import Column, Integer, String
from app.database import Base 

class ItemGerenciavel:
    def exibir_detalhes(self):
        raise NotImplementedError("As filhas devem implementar isso")

class Tarefa(Base, ItemGerenciavel):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    prioridade = Column(String)
    status = Column(String, default="pendente")
    prazo = Column(String, nullable=True)
    tipo = Column(String, default="comum")


    def exibir_detalhes(self):
        return f"Tarefa Comum: {self.titulo} ({self.status})"


class TarefaPrioritaria(Tarefa):
    
    def exibir_detalhes(self):
        return f"URGENTE: {self.titulo} - Prazo: {self.prazo}!!!"