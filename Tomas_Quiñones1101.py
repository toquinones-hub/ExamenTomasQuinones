def cupos_genero(genero, peliculas, cartelera):
    genero=genero.strip().lower()
    genero_pelicula = 0
    for codigo_pelicula, peliculas in codigo_pelicula.items():
        if genero_pelicula[1]:

            for codigo_peliculas_cartelera, cartelera in cartelera.items():
                if codigo_pelicula == codigo_peliculas_cartelera:
                    cantidad_pelicula += cartelera[1]
                    break 

def eliminar_pelicula(buscar_codigo, peliculas, cartelera):

    if buscar_codigo==peliculas and buscar_codigo==cartelera:
        del peliculas[buscar_codigo]
        del cartelera[buscar_codigo]
        return True    
    else:
        return False

def busqueda_precio(p_min, p_max, peliculas, cartelera):

    peliculas_rango_precio = []

    for codigo_cartelera, arreglo_cartelera in arreglo_cartelera.items():
        precio=cartelera[0]

        if precio >= p_min and precio <= p_max and cartelera[1] > 0:
            for codigo_pelicula, peliculas in peliculas.items():
                if codigo_pelicula == codigo_cartelera:
                    peliculas_rango_precio.append(f"{peliculas[0]}--{codigo_pelicula}")
                    break

    if len(peliculas_rango_precio) > 0:
        peliculas_rango_precio.sort()
        for peliculas in peliculas_rango_precio:
            print(peliculas)
    else:
        print("Debe ingresar valores enteros")

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):

    nueva_peli = { codigo: [titulo, genero, duracion, clasificacion, idioma, es_3d]}
    nueva_cartelera = {codigo: [precio, cupos]}
    peliculas+= nueva_peli
    cartelera+= nueva_cartelera

def actualizar_precio(codigo, precionuevo):
    for i in cartelera:
        codigo= codigo.upper()
        if codigo == [cartelera]:

            cartelera+=precionuevo



peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}  # 0123      0               1               2     3       4       5

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}       #       0   1

while True:
    print("""========== MENÚ PRINCIPAL ==========
1. Cupos por género
2. Búsqueda de películas por rango de precio
3. Actualizar precio de película
4. Agregar película
5. Eliminar película
6. Salir
=====================================""")
    opcion = input("Seleccione una opcion: ")
    if opcion=="1":
        genero=input("Ingrese el nombre del genero: ").lower()
        cupos_genero(genero, peliculas, cartelera)
    elif opcion=="2":
        try:
            p_min=int(input("Ingrese rango minimo: "))
            p_max=int(input("Ingrese rango maximo: "))
            if p_min < 0 or p_min> p_max:
                print("Ingrese un valor valido")
            else:
                busqueda_precio(p_min, p_max, peliculas, cartelera)
        except ValueError:
            print("Debe ingresar valores enteros")

    elif opcion=="3":
        codigo=input("Ingrese codigo de la pelicula")
        precionuevo=input("Ingrese nuevo precio de la pelicula: ")
        actualizar_precio(codigo, precionuevo)
    elif opcion=="4":
        Pelicula3D=False
        codigo=input("Ingrese el codigo de la pelicula: ").strip().upper()
        if codigo == peliculas:
                print("Este codigo ya existe!")
        else:
                titulo=input("Ingrese titulo de la pelicula: ").strip()
                if titulo==" ":
                    print("No puede ingresar un texto vacio!")
                else:
                    genero=input("Ingrese genero de la pelicula: ").strip()
                    if genero==" ":
                        print("No puede ingresar un texto vacio!")
                    else:
                        try:
                            duracion=int(input("Ingrese la duracion de la pelicula: "))
                            if duracion>0:
                                clasificacion=input("Ingrese clasificacion de edad (A, B, C): ").upper()
                                if clasificacion == "A" or clasificacion == "B" or clasificacion == "C":
                                    idioma=input("Ingrese el idioma de la pelicula: ").strip
                                    if idioma==" ":
                                        print("No puede ingresar un texto vacio!")
                                    else:
                                        es_3d=input("La pelicula es 3D?:").lower()
                                        if es_3d=="s":
                                            Pelicula3D==True
                                            try:
                                                precio=int(input("Ingrese el precio de la pelicula: "))
                                                if precio > 0:
                                                    cupos=int(input("Ingrese la cantidad de cupos: "))
                                                    try:
                                                        if cupos>0:
                                                            agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
                                                        else:
                                                            print("Debe ingresar un numero entero mayor a 0!")
                                                    except ValueError:
                                                        print("Debe ingresar un numero entero mayor a 0!")
                                                else:
                                                    print("Debe ingresar un numero entero mayor a 0!")
                                            except ValueError:
                                                print("Debe ingresar un numero entero mayor a 0!")
                                        elif es_3d=="n":
                                            Pelicula3D==False
                                            try:
                                                precio=int(input("Ingrese el precio de la pelicula: "))
                                                if precio > 0:
                                                    cupos=input("Ingrese la cantidad de cupos: ")
                                                    try:
                                                        if cupos>0:
                                                            agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
                                                        else:
                                                            print("Debe ingresar un numero entero mayor a 0!")
                                                    except ValueError:
                                                        print("Debe ingresar un numero entero mayor a 0!")
                                                else:
                                                    print("Debe ingresar un numero entero mayor a 0!")
                                            except ValueError:
                                                print("Debe ingresar un numero entero mayor a 0!")
                                else:
                                    print("Ingrese una clasificacion valida!")
                            else:
                                print("Debe ingresar un numero entero mayor a 0!")
                        except ValueError:
                            print("Debe ingresar un numero entero mayor a 0!")
        agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
    elif opcion=="5":
        buscar_codigo=input("Ingrese el codigo de la pelicula: ")
        eliminado=eliminar_pelicula(buscar_codigo, peliculas, cartelera)
        if eliminado== True:
            print("Película eliminada")
        else:
            print("El código no existe")
    elif opcion=="6":
        print("Programa finalizado.")
        break