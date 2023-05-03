

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    name = Column(String(350), nullable=False)
    zear_of_production = Column(Integer(), nullable=True)
    
    
def db_init():
    db_engine = create_engine('sqlite:///db_movies.db')
    Base.metadata.create_all(db_engine)
        
    