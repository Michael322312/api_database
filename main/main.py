from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str

users = [
    User(id=1, username='Michael', email="michaels123@gmail.com"),
    User(id=2, username="User", email="user23476@gmail.com")
]


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    else:
        return "User not found"


@app.get("/users")
def get_all_users():
    return users


@app.post("/create_user")
def create_user(username: str, email: str):
    user = User(id=users[-1].id, username=username,email=email)
    users.append(user)
    return user