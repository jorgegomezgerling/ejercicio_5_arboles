# Dado un archivo con todos los JEDI, de los que se cuenta con: nombre, especie, anio de nacimiento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro los ultimos tres campos pueden tener mas de un valor. Esribir las funciones necesarias para resolver las siguientes consignas:
# a. crear tres arboles de acceso a los datos: por nombre, ranking y especie; Done! (No entiendo bien como funciona, puesto que falté a clases pero veo que funciona)
# b. realizar un barrido inorden del arbol por nombre y ranking; DONE! 
# c. realizar un barrido por nivel de los arboles por ranking y especie; DONE! 
# d. mostrar toda la información de Yoda y Luke Skywalker; DONE!
# e. mostrar todos los Jedi con ranking "Jedi Master"; DONE! 
# f. listar todos los Jedi que utilizaron sable de luz color verde; DONE! 
# g. listar todos los Jedi cuyos maestros están en el archivo; DONE! 
# h. mostrar todos los Jedi de especie "Togruta" o "Cerean"; DONE!  
# i. listar los Jedi que comienzan con la letra A y los que contiene un "-" en su nombre; 

from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open('jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)

def ejercicio_b():
    print('barrido por nombre:')
    name_tree.inorden()
    print()
    print('barrido por ranking:')
    ranking_tree.inorden()

def ejercicio_c():
    print('barrido arbol ranking por nivel: ')
    ranking_tree.by_level()
    print()
    print('barrido arbol especie por nivel: ')
    specie_tree.by_level()

#personaje = input('Ingrese a quien quiere buscar: ')
def ejercicio_d(personaje):
    pos = name_tree.search(personaje)
    if pos:
        print(get_value_from_file('jedis.txt', pos.other_values))
    else:
        print('no esta en la lista')

def ejercicio_e():
    ranking_tree.inorden_rank('jedis.txt', 'jedi master')

def ejercicio_f():
    name_tree.inorden_file_lightsaber('jedis.txt', 'green')

def ejercicio_g():
    print('jedis con maestro: ')
    name_tree.inorden_maestro('jedis.txt')

def ejercicio_h():
    print('provenientes de togruta o cerean: ')
    name_tree.inorden_proveniente('jedis.txt')

def ejercicio_i():
    print('Jedis que comienzan con la letra "A"')
    name_tree.inorden_start_with_jedi('A')
    print()
    print('Jedis que contienen caracter particular: ')
    name_tree.inorden_caracter('-')

ejercicio_i()


#name_tree.inorden()
#ranking_tree.postorden()
# print()
# ranking_tree.inorden_file('jedis.txt')
# print(get_value_from_file('jedis.txt', ))
# print()
# ranking_tree.by_level()
# print()
# specie_tree.by_level()

#print()

# name_tree.inorden_file_lightsaber('jedis.txt', 'green')

#name_tree.inorden_start_with_jedi('A')