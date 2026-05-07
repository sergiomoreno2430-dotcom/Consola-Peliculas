"""
Agenda de películas.
Módulo de lógica.
"""


def crear_pelicula(nombre, genero, duracion, anio, clasificacion, hora, dia):

    return {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }


def encontrar_pelicula(nombre_pelicula, p1, p2, p3, p4, p5):

    peliculas = [p1, p2, p3, p4, p5]

    for peli in peliculas:
        if peli["nombre"].lower() == nombre_pelicula.lower():
            return peli

    return None


def encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5):

    peliculas = [p1, p2, p3, p4, p5]
    mas_larga = peliculas[0]

    for peli in peliculas:
        if peli["duracion"] > mas_larga["duracion"]:
            mas_larga = peli

    return mas_larga


def duracion_promedio_peliculas(p1, p2, p3, p4, p5):

    peliculas = [p1, p2, p3, p4, p5]

    total = 0

    for peli in peliculas:
        total += peli["duracion"]

    promedio = total // 5

    horas = promedio // 60
    minutos = promedio % 60

    return f"{horas:02}:{minutos:02}"


def encontrar_estrenos(p1, p2, p3, p4, p5, anio):

    peliculas = [p1, p2, p3, p4, p5]
    resultado = []

    for peli in peliculas:
        if peli["anio"] > anio:
            resultado.append(peli["nombre"])

    if len(resultado) == 0:
        return "Ninguna"

    return ", ".join(resultado)


def cuantas_peliculas_18_mas(p1, p2, p3, p4, p5):

    peliculas = [p1, p2, p3, p4, p5]

    contador = 0

    for peli in peliculas:
        if peli["clasificacion"] == "18+":
            contador += 1

    return contador


def reagendar_pelicula(peli, nueva_hora, nuevo_dia,
                        control_horario, p1, p2, p3, p4, p5):

    peliculas = [p1, p2, p3, p4, p5]

    dias_validos = [
        "Lunes", "Martes", "Miércoles",
        "Jueves", "Viernes", "Sábado", "Domingo"
    ]

    if nuevo_dia not in dias_validos:
        return False

    for otra in peliculas:

        if (
            otra != peli
            and otra["dia"] == nuevo_dia
            and otra["hora"] == nueva_hora
        ):
            return False

    if control_horario:

        if nueva_hora < 600 or nueva_hora > 2359:
            return False

    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia

    return True


def decidir_invitar(peli, edad, autorizacion):

    clas = peli["clasificacion"]
    genero = peli["genero"]

    # Mayores de edad
    if edad >= 18:
        return True

    # Menores de 15 no pueden ver terror
    if edad < 15 and "terror" in genero.lower():
        return False

    # Menores de 10 solo familiar
    if edad <= 10 and "familiar" not in genero.lower():
        return False

    # Documentales siempre permitidos
    if "documental" in genero.lower():
        return True

    # Clasificación Todos
    if clas == "Todos":
        return True

    # Clasificación 7+
    elif clas == "7+":

        if edad >= 7:
            return True

        return autorizacion

    # Clasificación 13+
    elif clas == "13+":

        if edad >= 13:
            return True

        return autorizacion

    # Clasificación 16+
    elif clas == "16+":

        if edad >= 16:
            return True

        return autorizacion

    # Clasificación 18+
    elif clas == "18+":
        return autorizacion

    return False