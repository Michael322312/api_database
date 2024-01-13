from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    pass


@app.get("/users")
def get_all_users():
    pass


@app.post("/create_user")
def create_user(username: str, email: str):
    pass