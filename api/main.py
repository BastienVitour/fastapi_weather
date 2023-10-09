from fastapi import FastAPI
from weather import weather

app = FastAPI()

# Include the user endpoints
app.include_router(weather.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
