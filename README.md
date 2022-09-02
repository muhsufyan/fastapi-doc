# fastapi-doc

## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn main:app --reload<br>
* dimana app adlh root dir, main adlah file main.py & app adlah FastAPI()<br>
# note
di python 3.6, OR pd param func menggunakan union<br>
=> q: Union[str, None] = None<br>
sedangkan untuk 3.10<br>
=>  q: str | None = None

# Background Task
menjalankan fungsi/class/code dibelakang layar (background) tanpa mengganggu user<br>
ex mengirim notif ke user via email dimana kode untuk notif akan dijalankan dibelakang layar (background)<br>
di doc nya disbt background task adlh run after returning a response<br>
js client doesn't really have to be waiting for the operation to complete before receiving the response<br>
ex lainnya, Processing data: let's say you receive a file that must go through a slow process, you can return a response of "Accepted" (HTTP 202) and process it in the background.