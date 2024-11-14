dados = {"alunos":[
                   {"nome":"lucas","id":15},
                   {"nome":"cicero","id":29},
                  ], 
        "professores":[]}

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise AlunoNaoEncontrado

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def deleta_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            dados['alunos'].remove(dicionario)
            return 'ok'
    raise AlunoNaoEncontrado

def edita_nome_id(id_aluno,nome):
    dici_aluno = aluno_por_id (id_aluno)
    dici_aluno['nome'] = nome
    return "namama"


def adiciona_aluno(dict):
    dados['alunos'].append(dict)

def lista_alunos():
    return dados["alunos"]

def apaga_tudo():
    dados['alunos'] = []

