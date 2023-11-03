# Dado un arbol con los nombres de los superhéroes y villanos de la saga Maverl Cinematic Universe (MCU), desarrollar un algortmo que contemple lo siguiente:

# a. ademas del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente; DONE!
# b. listar los villanos ordenados alfabéticamente DONE!
# c. mostrar todos los superhéroes que empiezan con C. DONE!
# d. determinar cuántos superhéroes hay en el árbol. DONE!
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre; DONE! 
# f. listar los superhéroes ordenados de manera descentente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguientes tareas:
# I. determinar cuántos nodos tiene cada árbol; DONE!
# II. realizar un barrido ordenado alfabéticamente de cada árbol. DONE! 

from arbol_binario import BinaryTree

arbol = BinaryTree()
arbol_villano = BinaryTree()
arbol_heroes = BinaryTree()

personajes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

for personaje in personajes:
    arbol.insert_node(personaje['name'], personaje['heroe'])

def ejercicio_b():
    print('b')
    arbol.inorden_sov(False)

def ejercicio_c():
    print('c')
    arbol.inorden_letra('c')

def ejercicio_d():
    print('d')
    print(arbol.contar_en_general()) # Entiendo que superheroe es categoria general, dividida en heroes y villanos. No obstante, si se quisiera únicamente los héroes también está definida la funcion: contar_heroes, la cual toma como unico parametro el arbol y arroja un contador de héroes.

def ejercicio_e():
    print('e')
    superheroe = input('Ingrese superheroe que desea modificar: ')
    pos = arbol.search(superheroe)
    if pos:
        es_heroe = pos.other_values
        arbol.delete_node(superheroe)
        nombre_correcto = input('Ingrese ahora el nombre correctamente: ')
        arbol.insert_node(nombre_correcto, es_heroe)
    else:
        print(superheroe, ': no se encuentra.')
    arbol.inorden()

def ejercicio_f(): # Si bien en el otro consideré a superheroes como la categoría más abarcativa, en este ejercicio para no hacer simplemente un postorden, los dividí en heroes y superhéroes. 
    arbol.postorden_listadoD(False)

def ejercicio_g():
    arbol.hacer_bosque(arbol_heroes, arbol_villano)
    print('cantidad de nodos arbol heroes: ')
    print(arbol_heroes.contar_en_general())
    print('cantidad de nodos arbol villanos: ')
    print(arbol_villano.contar_en_general())
    print()
    print('barrido heroes:')
    arbol_heroes.inorden()
    print()
    print('barrido villanos:')
    arbol_villano.inorden()

ejercicio_g()