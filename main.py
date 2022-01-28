import imp
import psycopg2
from .config import config

# config é um dicioário com as configurações a serem desempacotadas como nos
# argumentos da conexão.

# Cria uma conexão utilizando as conficurações preconstruídas
conn = psycopg2.connect(**config)

# Cria um cursor a partir da conexão
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS times;
''')

# Cria a tabela "times"
cur.execute('''
    CREATE TABLE IF NOT EXISTS times(
        id              BIGSERIAL       PRIMARY KEY,
        nome_do_time    VARCHAR         NOT NULL,
        divisao         VARCHAR(128)    NOT NULL
    );
''')

# Pupulando a tabela "times"
cur.execute('''
    INSERT INTO times
        (nome_do_time, divisao)
    VALUES
        ('Zé do Leite FC', '1ª divisão'),
        ('Esporte Clube Estoura Dedo', '1ª divisão'),
        ('Atlético da esquina FC', '2ª divisão')
    RETURNING *;
''')

# Capturando a saída da última execução do método "execute"
registros = cur.fetchall()
print('>>>>>>>', registros)

# Pegando todas as informações da tabela "times"
cur.execute('''
    SELECT * FROM times;
''')

# Capturando a saída da última execução do método "execute"
registros = cur.fetchall()
print('>>>>>>>', registros)

# Comando usado para persistir as mudanças realizadas pelos scripts
conn.commit()

# Após tudo, é necessário fechar a conexão para evitar instabilidades
cur.close()
conn.close()
