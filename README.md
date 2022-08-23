# fastapi-doc
## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
pip install "fastapi[all]" <br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn main:app --reload<br>
* dimana main adlah file main.py & app adlah FastAPI()<br>

# query parameter
http://127.0.0.1:8000/items/?skip=0&limit=10 ==  http://127.0.0.1:8000/items/ <br>
query param are skip & limit (after quetion mark "?"). default for skip and limit for our case are 10<br>
