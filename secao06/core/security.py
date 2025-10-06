from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_senha(senha: str, hashed_password: str) -> bool:
    return CRIPTO.verify(senha, hashed_password)

def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)