from base64 import encode
import collections

from utils.conector import conecta, desconecta

data=[]
#Sample select query
#query = 'select usr_ds_nickname, 123456, pes_nu_cpf_cgc from usr_usuario'
def select_query(query):
    cursor=conecta()
    cursor.execute(query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["usuario"] = row[0]
        d["senha"] = row[1]
        objects_list.append(d)

    #j = json.dumps(objects_list)
    desconecta(cursor)
    return objects_list