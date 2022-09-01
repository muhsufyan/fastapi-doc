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

# CORS (Cross-Origin Resource Sharing)
the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a different "origin" than the frontend.<br>
* allow_origins => A list of origins that should be permitted to make cross-origin requests. E.g. ['https://example.org', 'https://www.example.org']. You can use ['*'] to allow any origin.
* allow_origin_regex => A regex string to match against origins that should be permitted to make cross-origin requests. e.g. 'https://.*\.example\.org'.
* allow_methods => A list of HTTP methods that should be allowed for cross-origin requests. Defaults to ['GET']. You can use ['*'] to allow all standard methods.
* allow_headers => A list of HTTP request headers that should be supported for cross-origin requests. Defaults to []. You can use ['*'] to allow all headers. The Accept, Accept-Language, Content-Language and Content-Type headers are always allowed for CORS requests.
* allow_credentials => Indicate that cookies should be supported for cross-origin requests. Defaults to False. Also, allow_origins cannot be set to ['*'] for credentials to be allowed, origins must be specified.
* expose_headers => Indicate any response headers that should be made accessible to the browser. Defaults to [].
* max_age => Sets a maximum time in seconds for browsers to cache CORS responses. Defaults to 600.

## lbh baik baca lagi bagian cors