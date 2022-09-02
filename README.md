# fastapi-doc

## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn main:app --reload<br>
* dimana main adlah file main.py & app adlah FastAPI()<br>
# note
di python 3.6, OR pd param func menggunakan union<br>
=> q: Union[str, None] = None<br>
sedangkan untuk 3.10<br>
=>  q: str | None = None

# Static Files
ex asset logo, logo perusahaan/startup, dll<br>
serve static files automatically from a directory using <b>StaticFiles</b><br>
buat folder namanya static, karena directory isinya static => StaticFiles(directory="static/"), name="static")<br>