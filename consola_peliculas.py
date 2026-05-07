import modulo_peliculas as mod


def mostrar_informacion_pelicula(pelicula):

    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    print("Nombre:", nombre)
    print("Género:", genero)
    print("Duración:", duracion, "minutos")
    print("Año:", anio)
    print("Clasificación:", clasificacion)

    horas = hora // 100
    minutos = hora % 100

    print("Día: " + dia + " Hora: " + str(horas) + ":" + str(minutos))
    print()


# OPCIÓN 1
def ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5):

    peli = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)

    print("\nLa película más larga es:\n")

    mostrar_informacion_pelicula(peli)


# OPCIÓN 2
def ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5):

    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)

    print("\nDuración promedio:", promedio)


# OPCIÓN 3
def ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5):

    anio = int(input("Ingrese el año: "))

    resultado = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)

    print("\nPelículas encontradas:", resultado)


# OPCIÓN 4
def ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5):

    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)

    print("\nCantidad de películas 18+:", cantidad)


# OPCIÓN 5
def ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5):

    print("\nReagendar una película")

    nombre = input("Nombre de la película: ")

    peli = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if peli is None:
        print("No se encontró la película")
        return

    nueva_hora = int(input("Nueva hora (ej: 1830): "))

    nuevo_dia = input("Nuevo día (Lunes, Martes, etc): ")

    control = input(
        "¿Activar control horario? (si/no): "
    ).lower() == "si"

    exito = mod.reagendar_pelicula(
        peli, nueva_hora, nuevo_dia,
        control, p1, p2, p3, p4, p5
    )

    if exito:
        print("Película reagendada correctamente")

    else:
        print("No se pudo reagendar")


# OPCIÓN 6
def ejecutar_decidir_invitar(p1, p2, p3, p4, p5):

    print("\nVerificar invitación")

    nombre = input("Nombre de la película: ")

    peli = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if peli is None:
        print("No se encontró la película")
        return

    edad = int(input("Edad del invitado: "))

    autorizacion = input(
        "¿Tiene autorización? (si/no): "
    ).lower() == "si"

    puede = mod.decidir_invitar(peli, edad, autorizacion)

    if puede:
        print("Sí se puede invitar")

    else:
        print("No se puede invitar")


# MENÚ
def mostrar_menu(p1, p2, p3, p4, p5):

    print("\n--- MENÚ ---")
    print("1. Consultar película más larga")
    print("2. Consultar duración promedio")
    print("3. Buscar estrenos")
    print("4. Contar películas 18+")
    print("5. Reagendar película")
    print("6. Verificar invitación")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)

    elif opcion == "2":

        ejecutar_consultar_duracion_promedio_peliculas(
            p1, p2, p3, p4, p5
        )

    elif opcion == "3":

        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)

    elif opcion == "4":

        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)

    elif opcion == "5":

        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)

    elif opcion == "6":

        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)

    elif opcion == "7":
        return False

    else:
        print("Opción inválida")

    return True


# PROGRAMA PRINCIPAL
def iniciar():

    p1 = mod.crear_pelicula(
        "Shrek", "Familiar", 90,
        2001, "Todos", 1700, "Viernes"
    )

    p2 = mod.crear_pelicula(
        "Get Out", "Terror", 104,
        2017, "18+", 2330, "Sábado"
    )

    p3 = mod.crear_pelicula(
        "Icarus", "Documental", 122,
        2017, "18+", 800, "Domingo"
    )

    p4 = mod.crear_pelicula(
        "Inception", "Acción", 148,
        2010, "13+", 1300, "Lunes"
    )

    p5 = mod.crear_pelicula(
        "Star Wars", "Ciencia ficción", 124,
        1980, "7+", 1415, "Miércoles"
    )

    continuar = True

    while continuar:

        print("\n=== AGENDA DE PELÍCULAS ===\n")

        mostrar_informacion_pelicula(p1)
        mostrar_informacion_pelicula(p2)
        mostrar_informacion_pelicula(p3)
        mostrar_informacion_pelicula(p4)
        mostrar_informacion_pelicula(p5)

        continuar = mostrar_menu(p1, p2, p3, p4, p5)


# Ejecutar programa
iniciar()