# fastapi-doc

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

# Simple OAuth2 with Password and Bearer
## passwordnya secret, username dpt dilihat pd fake_users_db
saya tidak tahu bagaimana cara menggunakan untuk test OAuth2
penjelasan lbh lanjut mengenai get username & password for OAuth2 https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password<br>
body untuk OAuth2PasswordRequestForm adlh :
* The username.
* The password.
* An optional scope field as a big string, composed of strings separated by spaces.
* An optional grant_type
* An optional client_id (we don't need it for our example).
* An optional client_secret (we don't need it for our example).