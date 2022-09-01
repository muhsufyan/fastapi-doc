# fastapi-doc

## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn sql_app.main:app --reload<br>
* dimana sql_app adlh root dir, main adlah file main.py & app adlah FastAPI()<br>
# note
di python 3.6, OR pd param func menggunakan union<br>
=> q: Union[str, None] = None<br>
sedangkan untuk 3.10<br>
=>  q: str | None = None

# SQL
Kita gunakan SQLAlchemy as ORM sql<br>
pip install sqlalchemy<br>
buat file sql_app/database.py berisi config untuk konek ke sql (file tsb untuk koneksi ke db)<br>
file sql_app/models.py untuk Create the database models<br>
sql_app/schemas.py untuk Create the Pydantic models<br>
To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file models.py with the SQLAlchemy models, and the file schemas.py with the Pydantic models<br>
sql_app/crud.py untuk CRUD<br>
sql_app/main.py untuk main app<br>
sql_app/__init__.py: is an empty file<br>
## cara passing
Instead of passing each of the keyword arguments to Item and reading each one of them from the Pydantic model, we are generating a dict with the Pydantic model's data with:<br>
item.dict()<br>
and then we are passing the dict's key-value pairs as the keyword arguments to the SQLAlchemy Item, with:<br>
Item(**item.dict())<br>
And then we pass the extra keyword argument owner_id that is not provided by the Pydantic model, with:<br>
Item(**item.dict(), owner_id=user_id)<br>
### untuk migrasi gunakan alembic
### uvicorn sql_app.main:app --reload