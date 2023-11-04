# Implementar un algoritmo que permita generar un arbol con los datos de la siguiente tabla y resuleva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron; DONE!
# b. se debe permitir cargar una breve descripcion sobre cada criatura; DONE!
# c. mostrar toda la informacion de la criatura Talos; DONE! 
# d. determinar los 3 heroes o dioses que derrotaron mayor cantidad de criaturas; DONE!
# e. listar las criaturas derrotadas por Heracles; DONE! 
# f. listar las criaturas que no han sido derrotadas; DONE! 
# g. ademas cada nodo debe tener un campo "capturada" que almacerana el nombre del heroe o dios que la capturo; DONE! 
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabali de Enimanto indicando que Heracles las atrapo; DONE! 
# i. se debe permitir busquedas por coincidencia; DONE! 
# j. eliminar al Basilisco y a las Sirenas; DONE! 
# k. modificar el nodo que contiene a las Aves del Estinfalo, agregando que Heracles derroto a varias; DONE! 
# l. modificar el nombre de la criatura Ladon por Dragon Ladon; DONE!
# m. realizar un listado por nivel del arbol; DONE!
# n. muestre las criaturas capturadas por Heracles; DONE!

from arbol_binario import BinaryTree


arbol = BinaryTree()


datos = [
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tifón', 'derrotado': 'Zeus'},
    {'name': 'Equidna', 'derrotado': 'Argos Panoptes'},
    {'name': 'Dino', 'derrotado': None},
    {'name': 'Pefredo', 'derrotado': None},
    {'name': 'Enio', 'derrotado': None},
    {'name': 'Escila', 'derrotado': None},
    {'name': 'Caribdis', 'derrotado': None},
    {'name': 'Euríale', 'derrotado': None},
    {'name': 'Esteno', 'derrotado': None},
    {'name': 'Medusa', 'derrotado': 'Perseo'},
    {'name': 'Ladon', 'derrotado': 'Heracles'},
    {'name': 'Aguila de Caucaso', 'derrotado': None},
    {'name': 'Quimera', 'derrotado': 'Belerofonte'},
    {'name': 'Hidra de Lerna', 'derrotado': 'Heracles'},
    {'name': 'Leon de Nemea', 'derrotado': 'Heracles'},
    {'name': 'Esfinge', 'derrotado': 'Edipo'},
    {'name': 'Dragon de Colquida', 'derrotado': None},
    {'name': 'Cerbero', 'derrotado': None},
    {'name': 'Cerda de Cromion', 'derrotado': 'Teseo'},
    {'name': 'Ortro', 'derrotado': 'Heracles'},
    {'name': 'Toro de Creta', 'derrotado': 'Teseo'},
    {'name': 'Jabali de Calidon', 'derrotado': 'Atalanta'},
    {'name': 'Carcinos', 'derrotado': None},
    {'name': 'Gerion', 'derrotado': 'Heracles'},
    {'name': 'Cloto', 'derrotado': None},
    {'name': 'Laquelis', 'derrotado': None},
    {'name': 'Atropos', 'derrotado': None},
    {'name': 'Minotauro de Creta', 'derrotado': 'Teseo'},
    {'name': 'Harpias', 'derrotado': None},
    {'name': 'Argos Panoptes', 'derrotado': 'Hermes'},
    {'name': 'Aves de Esinfalo', 'derrotado': None},
    {'name': 'Talos', 'derrotado': 'Medea'},
    {'name': 'Sirenas', 'derrotado': None},
    {'name': 'Piton', 'derrotado': 'Apolo'},
    {'name': 'Cierva Cerinea', 'derrotado': None},
    {'name': 'Basilisco', 'derrotado': None},
    {'name': 'Jabali de Enimanto', 'derrotado': None},
]

for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})

def ejercicio_a():
    arbol.inorden_datos()

def ejercicio_b():
    arbol.inorden_add_newfield('Descripcion')

def ejercicio_c():
    ejercicio_b()
    arbol.inorden_criatura('Talos')

def ejercicio_d():
    ranking = {}
    arbol.inorden_ranking(ranking)

    top_tres = sorted(ranking, key=ranking.get, reverse=True)[:3]

    for clave in top_tres:
        print({clave}, {ranking[clave]})

def ejericio_e():
    arbol.inorden_derrotadas_por('Heracles')

def ejercicio_f():
    arbol.inorden_soy_invencible()

def ejercicio_g():
    arbol.inorden_add_field()

def ejercicio_h():
    arbol.inorden_heracles_ataca()
    ejercicio_a()

def ejercicio_i():
    arbol.search_by_coincidence('Jabali')

def ejercicio_j():
    arbol.delete_node('Sirenas')
    arbol.delete_node('Basilisco')

def ejercicio_k():
    ejercicio_b()
    arbol.inorden_aves_en_peligro()
    ejercicio_a()

def ejercicio_l():
    buscado = arbol.search('Ladon')
    if buscado is not None:
        aux = buscado.other_values
        arbol.delete_node('Ladon')
        arbol.insert_node('Dragon Ladon', aux)

def ejercicio_m():
    arbol.by_level()

def ejercicio_n():
    arbol.inorden_derrotado_por_heracles()
    
# arbol.inorden_add_field()


# dic_ranking = {}
# arbol.inorden_ranking(dic_ranking)

# print(dic_ranking)


# def order_por(item):
#     print(item)
#     return item[1]

# ordenados = list(dic_ranking.items())
# ordenados.sort(key=order_por, reverse=True)
# print(ordenados[:3])


# pos = arbol.search()
# if pos is not None:
#     pos.other_values['capturado'] = 'Heracles'