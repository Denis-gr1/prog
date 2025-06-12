from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import date

Base = declarative_base()

участие_в_проекте = Table(
    'участие_в_проекте',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('разработчик_id', Integer, ForeignKey('разработчик.id')),
    Column('проект_id', Integer, ForeignKey('проект.id')),
    Column('роль', String(50))
)

class Разработчик(Base):
    __tablename__ = 'разработчик'
    id = Column(Integer, primary_key=True)
    имя = Column(String(100), nullable=False)
    должность = Column(String(100))
    email = Column(String(100))
    проекты = relationship("Проект", secondary=участие_в_проекте, back_populates="разработчики")

class Менеджер(Base):
    __tablename__ = 'менеджер'
    id = Column(Integer, primary_key=True)
    имя = Column(String(100), nullable=False)
    email = Column(String(100))
    проекты = relationship("Проект", back_populates="менеджер")

class Проект(Base):
    __tablename__ = 'проект'
    id = Column(Integer, primary_key=True)
    название = Column(String(100), nullable=False)
    описание = Column(String(500))
    срок_сдачи = Column(Date)
    менеджер_id = Column(Integer, ForeignKey('менеджер.id'))
    менеджер = relationship("Менеджер", back_populates="проекты")
    разработчики = relationship("Разработчик", secondary=участие_в_проекте, back_populates="проекты")

def init_db():
    engine = create_engine('sqlite:///project_management.db')
    Base.metadata.create_all(engine)
    return engine