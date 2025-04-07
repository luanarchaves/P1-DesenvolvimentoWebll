from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str

# class UsuarioRequestSchema(BaseModel):
#     id: int  # ID opcional, pois pode ser gerado automaticamente
#     nome: str
#     email: str
#     senha: str

class UsuarioResponseSchema(BaseModel):
    id: int
    nome: str
    email: str
    senha: str


class UsuarioListResponseSchema(BaseModel):
    usuarios: list[UsuarioResponseSchema]

    class Config:
        orm_mode = True  # Permite que o Pydantic converta modelos ORM em dicionários