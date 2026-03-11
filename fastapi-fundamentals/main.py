# Query Parameters
# Requirement:
# Create a GET endpoint /search that accepts two optional query parameters:

# name (string)
# age (integer)
# Return the received parameters as JSON.

# Example Request:
# /search?name=Deepak&age=30
# Expected Response:
# {
#   "name": "Deepak",
#   "age": 30
# }

from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
def search(name: Optional[str] = Query(default=None), age: Optional[str] = Query(default=None)):
    input_data = {"name": name, "age": age}
    return input_data
