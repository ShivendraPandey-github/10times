from sqlalchemy import create_engine
from models import Base

engine = create_engine('postgresql://root:12345678@localhost:5432')
Base.metadata.create_all(engine)
