import sqlite3

#criando banco de dados 
conection = sqlite3.connect('database.db')

#criando cursor 
cursor = conection.cursor()

#criando tabelas
cursor.execute (

"""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dre TEXT NOT NULL,
        password TEXT NOT NULL
        )
"""
)

cursor.execute (

    """
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY,
        code TEXT NOT NULL,
        name TEXT NOT NULL
        )
    """
)

#criando tabelas relacionais
cursor.execute (
    """
    CREATE TABLE IF NOT EXISTS inscricoes(
        id INTEGER PRIMARY KEY,
        idAluno INTEGER NOT NULL,
        idDisciplina INTEGER NOT NULL,

        FOREIGN KEY (idAluno) REFERENCES alunos(id),
        FOREIGN KEY (idDisciplina) REFERENCES disciplinas(id)
        )    
    """
)

#inserindo dados
cursor.execute (
    
    """
    INSERT INTO alunos (name, dre, password)
    VALUES ("Marina Daumas", "1788752092", "senha"), ("Fulano", "17645699", "senha1");
    """
    )

#consultando dados
rows = cursor.execute(
    
    """
    SELECT name, dre, senha FROM alunos;
    """
).fetchall()

#atualizar dados

#deletar dados

#fechar banco de dados
conection.close()
