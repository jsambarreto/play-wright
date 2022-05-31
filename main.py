

from utils.server import select_query
from teste import executa_teste

query = 'select top 1 usr_ds_nickname, 123456 from portal3..usr_usuario where usr_ch_bloqueio = 0'
usuarios = select_query(query)
for usuario in usuarios:
    print (usuario["usuario"])
    executa_teste(usuario["usuario"], usuario["senha"])