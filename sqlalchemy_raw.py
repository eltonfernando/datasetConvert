from sqlalchemy import create_engine,Table,Column,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError,PendingRollbackError
# Configuracoes
engine = create_engine('sqlite:///test.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
meta_data = MetaData()

user = Table(
    "filmes",
    meta_data,
    Column("titulo",String, primary_key=True),
    Column("genero",String, nullable=False),
    Column("ano",Integer, nullable=False)
)
meta_data.create_all(engine)  
# Entidades
class Filmes(Base):
    __table__ = user

    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"


# SQL
# Insert
data_isert = Filmes(titulo="jfasasufy2w3", genero="Acao", ano=1111)
try:
    session.add(data_isert)
    session.commit()
except IntegrityError as error:
    print("erro ",error)
    session.rollback()


# Select
data = session.query(Filmes).all()
#print(data)

session.close()