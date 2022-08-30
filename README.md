# fastapi-doc bagian 2
membahas cookies, headers, response ke user, kode http response
## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
pip install "fastapi[all]" <br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn main:app --reload<br>
* dimana main adlah file main.py & app adlah FastAPI()<br>
# note
di python 3.6, OR pd param func menggunakan union<br>
=> q: Union[str, None] = None<br>
sedangkan untuk 3.10<br>
=>  q: str | None = None
# Response Model
adlh data model yg akan diberikan sebagai response ke user<br>
DIREKOMENDASIKAN RESPONSE DATA MODEL ITU BERBEDA DENGAN DATA MODEL UNTUK DATABASE KARENA USER TDK BUTUH SEMUA DATA YG TER/DI- SIMPAN DLM DATABASE UNTUK DIPERLIHATKAN (AS RESPONSE DATA MODEL)<br>
EmailString hars install dulu pip install email-validator or pip install pydantic[email].

Use the path operation decorator's parameter response_model to define response models and especially to ensure private data is filtered out.

Use response_model_exclude_unset to return only the values explicitly set.
## ADA ERROR
