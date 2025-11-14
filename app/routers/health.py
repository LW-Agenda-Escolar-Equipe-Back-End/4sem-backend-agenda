from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def health_check():
    """Verificar status da API."""
    return {"status": "healthy", "version": "1.0.1"}
