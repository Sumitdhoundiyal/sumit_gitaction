from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return " hi Sumit dhoundiyal your code is working fine,you are now ready to give demo to pavan and amit and demonstrate what you have done so far"
