# fastapi-doc
## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
pip install "fastapi[all]" <br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn main:app --reload<br>
* dimana main adlah file main.py & app adlah FastAPI()<br>

# path param
ex the param is foo => http://127.0.0.1:8000/items/foo<br>
path param select data from list => /models/{model_name}<br>
path param for file => /files/{file_path}<br>
