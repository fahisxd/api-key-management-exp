from fastapi import FastAPI
#testing
app = FastAPI()

@app.get("/keys")
async def list_keys():
    return {"keys": []}


@app.post("/keys")
async def create_key():
    return {"status": "created"}


@app.put("/keys/{key_id}")
async def update_key(key_id: int):
    return {"updated": key_id}


@app.delete("/keys/{key_id}")
async def delete_key(key_id: int):
    return {"deleted": key_id}