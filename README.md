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

# SUB DEPENDENCIES
## Using the same dependency multiple times
jika dependency dideklarasikan beberapa kali didlm path operation, misalnya beberapa dependensi memiliki sub-dependensi yang sama, FastAPI akan tahu untuk memanggil sub-dependensi itu hanya sekali per request.<br>
Dan itu akan menyimpan nilai yang dikembalikan dalam "cache"<br>
In an advanced scenario where you know you need the dependency to be called at every step (possibly multiple times) in the same request instead of using the "cached" value, you can set the parameter use_cache=False when using Depends<br>
async def needy_dependency(fresh_value: str = Depends(get_value, use_cache=False)):
    return {"fresh_value": fresh_value}