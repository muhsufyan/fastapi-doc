# can define Header parameters the same way you define Query, Path and Cookie parameters.
from fastapi import FastAPI, Header

app = FastAPI()

# Declare Header parameters
#  declare the header parameters using the same structure as with Path, Query and Cookie
@app.get("/items/")
# The first value is the default value, you can pass all the extra validation or annotation parameters
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}

# Automatic conversion
# biasanya header memakai tanda - tp di fastapi gunakan tanda _ maka otomatis diconvert jd - 
# tp jika ingin fitur otomatis convert ini hilang maka set
# parameter convert_underscores of Header to False
@app.get("/convert2underscore/items/")
async def read_items(
    # nonactive auto convert
    strange_header: str | None = Header(default=None, convert_underscores=False)
):
    return {"strange_header": strange_header}

# Duplicate headers
# artinya the same header with multiple values
# untuk mencegah itu gunakan list yg akan menampung semua nilai dari 1 key header yg sama tsb
@app.get("/duplicateheader/items/")
# header of X-Token that can appear more than once
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}
"""
now if 
X-Token: foo
X-Token: bar
maka headernya jd
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
"""