from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = 'postgresql://postgres:Admin@localhost:5432/QuizApplicationforYT'

engine = create_engine(URL_DATABASE)

Sessionlocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()
