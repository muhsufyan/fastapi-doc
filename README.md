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
# Headers Parameters
can define Header parameters the same way you define Query, Path and Cookie parameters.