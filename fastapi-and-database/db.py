# Connection to Database
from sqlalchemy import create_engine

DB_URL = "sqlite:///./masai.db"

engine = create_engine(url=DB_URL, echo=True)