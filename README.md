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
# FORM DATA
data input selain berupa json dpt pula form input, gunakan Form<br>
install dulu => pip install python-multipart.<br>
With <b>Form</b> you can declare the same metadata and validation as with <b>Body</b> (and <b>Query, Path, Cookie</b>). karena <b>Form</b> is a class that inherits directly from <b>Body</b>.<br>
Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.
But when the form includes files, it is encoded as multipart/form-data<br>
WARNING: You can declare multiple Form parameters in a path operation, but you can't also declare Body fields that you expect to receive as JSON, as the request will have the body encoded using application/x-www-form-urlencoded instead of application/json.

<BR>This is not a limitation of FastAPI, it's part of the HTTP protocol.
