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
# BODY UPDATE
untuk update
## Partial updates recap
* (Optionally) use PATCH instead of PUT.
* Retrieve the stored data.
* Put that data in a Pydantic model.
* Generate a dict without default values from the input model (using exclude_unset).
    * This way you can update only the values actually set by the user, instead of overriding values already stored with default values in your model.<br>


* Create a copy of the stored model, updating it's attributes with the received partial updates (using the update parameter).
* Convert the copied model to something that can be stored in your DB (for example, using the jsonable_encoder).
    *This is comparable to using the model's .dict() method again, but it makes sure (and converts) the values to data types that can be converted to JSON, for example, datetime to str.<br>


* Save the data to your DB.
* Return the updated model.