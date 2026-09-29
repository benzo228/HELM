import os
from fastapi import FastAPI

app = FastAPI(title="FastAPI on minikube")

APP_ENV = os.getenv("APP_ENV", "dev")
GREETING = os.getenv("GREETING", "Hello")
DB_PASSWORD = os.getenv("DB_PASSWORD", "not-set")


@app.get("/")
def root():
    return {
        "message": f"{GREETING} from FastAPI!",
        "env": APP_ENV,
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/secret-check")
def secret_check():
    # покажем, что секрет реально доехал (не делай так в проде!)
    return {"db_password_length": len(DB_PASSWORD)}