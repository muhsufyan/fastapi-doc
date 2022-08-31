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
# STATUS CODE
status code ke user/developer lainnya. lbh lanjut mengenai status kode yg dpt diberikan https://docs.python.org/3/library/http.html#http.HTTPStatus<br>
SELAIN ITU KITA JUGA LANGSUNG MEMPELAJARI CHANGE STATUS CODE DIBAGIAN ADVANCE
# CHANGE STATUS CODE (ADVANCE)
https://fastapi.tiangolo.com/advanced/response-change-status-code/
kasus ini kita ubah jika data yg di update tdk ada maka akan disuruh untuk create a new data melalui status http 201<br>
Maka gunakan Response parameter untuk mengubah status code & tempatkan di path operation function (sama sprti cookie & headers)
