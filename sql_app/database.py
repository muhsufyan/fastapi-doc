# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a database URL for SQLAlchemy
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = 'mysql://username:password@localhost/db_name'
SQLALCHEMY_DATABASE_URL = "mysqlsql://root@localhost/db"


# create a SQLAlchemy "engine". NOTE untuk connect_args={"check_same_thread": False} hanya diperlukan oleh SQLite yg lainnya (mysql, postgresql) tdk perlu.
# alasannya adlh to prevent accidentally sharing the same connection for different things (for different requests).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class
# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet
# But once we create an instance of the SessionLocal class, this instance will be the actual database session
# We name it SessionLocal to distinguish(membedakan) it from the Session we are importing from SQLAlchemy
# To create the SessionLocal class, use the function sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class. declarative_base() that returns a class
Base = declarative_base()
