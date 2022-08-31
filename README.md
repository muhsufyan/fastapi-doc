# fastapi-doc bagian 3
INPUT FORM, FILE UPLOAD
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
# HANDLING ERROR
misalnya 404, tidak punya hak akses, harus login, bug code (500)<br>
When raising an HTTPException, you can pass any value that can be converted to JSON as the parameter detail, not only str<BR>
bagian FastAPI's HTTPException vs Starlette's HTTPException baca https://fastapi.tiangolo.com/tutorial/handling-errors/#fastapis-httpexception-vs-starlettes-httpexception