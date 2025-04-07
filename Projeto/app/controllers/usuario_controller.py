from app import Usuario


class UsuarioController:

    @staticmethod
    async def listar_usuarios():
        usuarios = Usuario.getUsuarios()
        if usuarios:
            return {"usuarios": usuarios}
        else:
            return {"message": "Nenhum usuário encontrado."}

    @staticmethod
    async def buscar_usuario_por_id(id_usuario):
        usuario = Usuario.pegar_por_id(id_usuario)
        if usuario:
            return {"usuario": usuario.__dict__}
        else:
            return {"message": "Usuário não encontrado."}

    @staticmethod
    async def criar_usuario(nome, email, senha):
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario_id = usuario.inserir()
        if usuario_id:
            return {"message": "Usuário criado com sucesso.", "id_usuario": usuario_id}
        else:
            return {"message": "Erro ao criar usuário."}

    @staticmethod
    async def atualizar_usuario(usuario: Usuario):
        usuario_existente = Usuario.pegar_por_id(usuario.id_usuario)
        if not usuario_existente:
            return {"message": "Usuário não encontrado."}
        usuario_existente = usuario
        usuario_id = usuario_existente.atualizar()
        if usuario_id:
            return {"message": "Usuário atualizado com sucesso.", "id_usuario": usuario_id}
        else:
            return {"message": "Erro ao atualizar usuário."}

    @staticmethod
    async def deletar_usuario(id_usuario):
        usuario_id = Usuario.deletar(id_usuario)
        if usuario_id:
            return {"message": "Usuário deletado com sucesso.", "id_usuario": usuario_id}
        else:
            return {"message": "Erro ao deletar usuário."}