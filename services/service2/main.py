from fastapi import FastAPI
import logging

app = FastAPI()

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Request received at root endpoint")
    return {"message": "Hello from Service2"}