"""""
Point d'entrée pincipla de l'apiavec FastAPI

ce fichier configure et l'anc l'application

"""""

# imports

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products


# Creer l'app

app = FastAPI(
    title = "API gestionnaire de Produits",
    descritpion = "API REST pour gerer un catalogue de produits",
    version = "1.0.0"
)

@app.get("/")
def root() :
    """
    Route racine de l'API
    """

    return {
        "message": "Bienvenue sur l'API",
        "documentaiton": "docs",
        "version":"1.0.0"
    }

@app.get("/health")
def health_check() :
    """
    endpoint pour verifier que l'API fonctionne
    """

    return {
        'status': "ok",
        "message" : "L'API fonctionne"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)