from fastapi import FastAPI
from app.routes import auth, domain

app = FastAPI(title="DomAIneer", description="AI powered App for domain management")

# Registering routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(domain.router, prefix="/domain", tags=["Domain Registration"])

@app.get("/")
def root():
    return {"message": "Welcome to DomAIneer"}