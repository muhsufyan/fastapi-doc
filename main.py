# agar dpt berjln dibelakang layar (background) gunakan BackgroundTasks
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

# this func run as the background task. the task function will write to a file (simulating sending an email).
def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # Add the background task with .add_task on BackgroundTasks
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
"""
pd kode diatas,
.add_task() receives as arguments:

* A task function to be run in the background (write_notification). write_notification adlh fungsi yg kita buat
* Any sequence of arguments that should be passed to the task function in order (email).
* Any keyword arguments that should be passed to the task function (message="some notification").
"""
# DI
from fastapi import Depends
#  can declare a parameter of type BackgroundTasks at multiple levels: in a path operation function, in a dependency (dependable), in a sub-dependency, etc.
def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)

# declare a parameter of type BackgroundTasks at path operation function
def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/DI/send-notification/{email}")
async def send_notification(
    # declare a parameter of type BackgroundTasks at dependencies
    email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
):
    message = f"message to {email}\n"
    # declare a parameter of type BackgroundTasks at sub-dependencies
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}