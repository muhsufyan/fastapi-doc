# fastapi-doc

## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run Metadata for API => uvicorn main:app --reload<br>
run Metadata for tags => uvicorn main2:app --reload<br>
run OpenAPI URL => uvicorn main3:app --reload<br>
* dimana app adlh root dir, main adlah file main.py & app adlah FastAPI()<br>
# note
di python 3.6, OR pd param func menggunakan union<br>
=> q: Union[str, None] = None<br>
sedangkan untuk 3.10<br>
=>  q: str | None = None

# Metadata & Docs URL
BACA TABEL DISINI https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api<br>