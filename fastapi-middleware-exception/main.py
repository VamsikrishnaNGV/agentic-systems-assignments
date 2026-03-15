# Middleware and Exception Handling in FastAPI
# You are building a FastAPI application that logs every incoming request.

# First, create a simple API endpoint /hello that returns the following JSON response:

# {
#   "message": "Hello, Welcome to FastAPI!"
# }
# Next, create a middleware that:

# Logs the HTTP method (GET, POST, etc.)
# Logs the URL path of the request
# Prints a message before the request is processed
# Prints a message after the response is returned
# Finally, implement a simple exception handler for 404 Not Found errors. This handler should return a custom JSON message when a user tries to access a route that is not defined in the application (for example, /unknown).

# Example response for an undefined route:

# {
#   "message": "The requested resource was not found"
# }

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.get("/hello")
def demo_endpoint():
    return {"message": "Hello, Welcome to FastAPI!"}


@app.middleware("http")
async def process_time(request: Request, call_next):
    print("Before request is processed")
    print(f"HTTP Method: {request.method}")
    print(f"URL Path: {request.url.path}")

    response = await call_next(request)

    print("After the request is processed")

    return response


@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404, content={"message": "The requested resource was not found"}
        )
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
