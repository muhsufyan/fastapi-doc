from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a user model (data model)
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

# Get the user
def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

# Create a get_current_user dependency. get_current_user will receive a token as a str from the sub-dependency oauth2_scheme
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Get the user
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
# Inject the current user(get_current_user)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user