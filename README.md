# fastapi-doc
## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
pip install "fastapi[all]" <br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn main:app --reload<br>
* dimana main adlah file main.py & app adlah FastAPI()<br>

# request body
untuk menangkap data request dr body maka gunakan pydantic, sehingga harus menggunakan BaseModel dari pydantic.
jika tdk memakai pydantic maka gunakan Body parameters dibagian Body - Multiple Parameters
