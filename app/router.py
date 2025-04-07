from fastapi import APIRouter
from .usuario_router import usuarioRouter
from .produto_router import produtoRouter


router = APIRouter()
router.include_router(usuarioRouter, prefix="/usuarios", tags=["usuarios"])
router.include_router(produtoRouter, prefix="/produtos", tags=["produtos"])  