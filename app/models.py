from sqlalchemy import Column, Integer, String
from .db_connector import Base, engine




class Operations(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String)
    result = Column(String)

Base.metadata.create_all(bind=engine)