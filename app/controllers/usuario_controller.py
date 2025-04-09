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
        if not isinstance(id_usuario, int):
            return {"error": "ID do usuário deve ser um número inteiro."}
        usuario = Usuario.pegar_por_id(id_usuario)
        if usuario:
            return {"usuario": usuario.__dict__}
        else:
            return {"message": "Usuário não encontrado."}

    @staticmethod
    async def criar_usuario(nome, email, senha):
        if not nome or not email or not senha:
            return {"error": "Todos os campos são obrigatórios."}
        if not isinstance(nome, str) or len(nome) < 3:
            return {"error": "Nome deve ser uma string com pelo menos 3 caracteres."}
        if not isinstance(email, str) or "@" not in email:
            return {"error": "Email inválido."}
        if not isinstance(senha, str) or len(senha) < 6:
            return {"error": "Senha deve ter pelo menos 6 caracteres."}
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario_id = usuario.inserir()
        if usuario_id:
            return {"message": "Usuário criado com sucesso.", "id_usuario": usuario_id}
        else:
            return {"message": "Erro ao criar usuário."}

    @staticmethod
    async def atualizar_usuario(usuario: Usuario):
        if not usuario.nome or not usuario.email or not usuario.senha:
            return {"error": "Todos os campos são obrigatórios."}
        if not isinstance(usuario.nome, str) or len(usuario.nome) < 3:
            return {"error": "Nome deve ser uma string com pelo menos 3 caracteres."}
        if not isinstance(usuario.email, str) or "@" not in usuario.email:
            return {"error": "Email inválido."}
        if not isinstance(usuario.senha, str) or len(usuario.senha) < 6:
            return {"error": "Senha deve ter pelo menos 6 caracteres."}
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
        if not isinstance(id_usuario, int) or id_usuario <= 0:
            return {"error": "ID do usuário deve ser um número inteiro positivo."}
        usuario_id = Usuario.deletar(id_usuario)
        if usuario_id:
            return {"message": "Usuário deletado com sucesso.", "id_usuario": usuario_id}
        else:
            return {"message": "Erro ao deletar usuário."}