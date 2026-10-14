# =========================================================
# actividad1_logica.py
# Generador de tablas de verdad y verificador de equivalencias
# Aplicado a un sistema de control de acceso TI
# =========================================================

from itertools import product

# =========================================================
# FUNCION PARA CLASIFICAR UNA PROPOSICION
# =========================================================

def clasificar(resultados):
    if all(resultados):
        return "TAUTOLOGIA"
    elif not any(resultados):
        return "CONTRADICCION"
    else:
        return "CONTINGENCIA"


# =========================================================
# FUNCION GENERADORA DE TABLAS DE VERDAD
# =========================================================

def tabla_verdad(nombre, funcion, variables):

    print("\n" + "=" * 60)
    print(f"TABLA DE VERDAD: {nombre}")
    print("=" * 60)

    encabezado = " | ".join(variables) + " | Resultado"
    print(encabezado)
    print("-" * len(encabezado))

    resultados = []

    for valores in product([False, True], repeat=len(variables)):

        resultado = funcion(*valores)
        resultados.append(resultado)

        fila = []

        for v in valores:
            fila.append("V" if v else "F")

        fila.append("V" if resultado else "F")

        print(" | ".join(fila))

    print("-" * len(encabezado))

    tipo = clasificar(resultados)
    print("Clasificación:", tipo)


# =========================================================
# FUNCION VERIFICADORA DE EQUIVALENCIAS
# =========================================================

def verificar_equivalencia(nombre1, f1, nombre2, f2, variables):

    print("\n" + "=" * 60)
    print("VERIFICACION DE EQUIVALENCIA")
    print("=" * 60)

    print(f"{nombre1}   ?=   {nombre2}")

    equivalentes = True

    encabezado = " | ".join(variables)
    encabezado += f" | {nombre1} | {nombre2}"

    print(encabezado)
    print("-" * len(encabezado))

    for valores in product([False, True], repeat=len(variables)):

        r1 = f1(*valores)
        r2 = f2(*valores)

        if r1 != r2:
            equivalentes = False

        fila = []

        for v in valores:
            fila.append("V" if v else "F")

        fila.append("V" if r1 else "F")
        fila.append("V" if r2 else "F")

        print(" | ".join(fila))

    print("-" * len(encabezado))

    if equivalentes:
        print(f"RESULTADO: {nombre1} ≡ {nombre2}")
    else:
        print(f"RESULTADO: {nombre1} ≢ {nombre2}")


# =========================================================
# REQUERIMIENTO 1
# GENERADOR DE TABLAS DE VERDAD
# =========================================================

# a) ¬p
tabla_verdad(
    "¬p",
    lambda p: not p,
    ["p"]
)

# b) p ∧ q
tabla_verdad(
    "p ∧ q",
    lambda p, q: p and q,
    ["p", "q"]
)

# c) p ∨ q
tabla_verdad(
    "p ∨ q",
    lambda p, q: p or q,
    ["p", "q"]
)

# d) p → q
tabla_verdad(
    "p → q",
    lambda p, q: (not p) or q,
    ["p", "q"]
)

# e) p ↔ q
tabla_verdad(
    "p ↔ q",
    lambda p, q: p == q,
    ["p", "q"]
)

# f) ¬p ∨ q
tabla_verdad(
    "¬p ∨ q",
    lambda p, q: (not p) or q,
    ["p", "q"]
)

# g) p ∨ ¬p
tabla_verdad(
    "p ∨ ¬p",
    lambda p: p or (not p),
    ["p"]
)

# h) p ∧ ¬p
tabla_verdad(
    "p ∧ ¬p",
    lambda p: p and (not p),
    ["p"]
)

# i) (p ∧ q) → r
tabla_verdad(
    "(p ∧ q) → r",
    lambda p, q, r: (not (p and q)) or r,
    ["p", "q", "r"]
)


# =========================================================
# REQUERIMIENTO 2
# VERIFICADOR DE EQUIVALENCIAS
# =========================================================

# a) ¬(p ∧ q) ≡ ¬p ∨ ¬q
verificar_equivalencia(
    "¬(p ∧ q)",
    lambda p, q: not (p and q),

    "¬p ∨ ¬q",
    lambda p, q: (not p) or (not q),

    ["p", "q"]
)

# b) ¬(p ∨ q) ≡ ¬p ∧ ¬q
verificar_equivalencia(
    "¬(p ∨ q)",
    lambda p, q: not (p or q),

    "¬p ∧ ¬q",
    lambda p, q: (not p) and (not q),

    ["p", "q"]
)

# c) p → q ≡ ¬p ∨ q
verificar_equivalencia(
    "p → q",
    lambda p, q: (not p) or q,

    "¬p ∨ q",
    lambda p, q: (not p) or q,

    ["p", "q"]
)

# d) p → q ≡ ¬q → ¬p
verificar_equivalencia(
    "p → q",
    lambda p, q: (not p) or q,

    "¬q → ¬p",
    lambda p, q: q or (not p),

    ["p", "q"]
)

# e) ¬¬p ≡ p
verificar_equivalencia(
    "¬¬p",
    lambda p: not (not p),

    "p",
    lambda p: p,

    ["p"]
)

# f) p ∧ (p ∨ q) ≡ p
verificar_equivalencia(
    "p ∧ (p ∨ q)",
    lambda p, q: p and (p or q),

    "p",
    lambda p, q: p,

    ["p", "q"]
)


# =========================================================
# REQUERIMIENTO 3
# APLICACION TI: SISTEMA DE CONTROL DE ACCESO
# =========================================================

# Variables:
# u = usuario_activo
# c = clave_correcta
# a = es_administrador
# h = en_horario

# Expresion principal:
# Acceso_permitido = (u ∧ c) ∧ (a ∨ h)

tabla_verdad(
    "Acceso_permitido",
    lambda u, c, a, h: (u and c) and (a or h),
    ["u", "c", "a", "h"]
)

# Verificacion de equivalencia con De Morgan

verificar_equivalencia(
    "(u ∧ c) ∧ (a ∨ h)",
    lambda u, c, a, h: (u and c) and (a or h),

    "¬(¬u ∨ ¬c ∨ (¬a ∧ ¬h))",
    lambda u, c, a, h: not ((not u) or (not c) or ((not a) and (not h))),

    ["u", "c", "a", "h"]
)

# =========================================================
# ANALISIS DEL SISTEMA DE ACCESO
# =========================================================

# Cantidad de combinaciones que permiten acceso:
#
# Para que exista acceso:
# u = Verdadero
# c = Verdadero
# y además:
# a = Verdadero  O  h = Verdadero
#
# Posibilidades válidas:
#
# 1) a = V , h = V
# 2) a = V , h = F
# 3) a = F , h = V
#
# Total:
# 3 combinaciones permiten acceso de las 16 posibles.


# Ley utilizada:
#
# Se utilizó la PRIMERA LEY DE DE MORGAN:
#
# ¬(p ∧ q) ≡ ¬p ∨ ¬q
#
# aplicada sobre partes internas de la expresión lógica.


# =========================================================
# REQUERIMIENTO 4
# ANALISIS ESCRITO
# =========================================================

# Pregunta 1:
# ¿En qué único caso el condicional p → q es FALSO?
#
# El condicional p → q es falso únicamente cuando:
# p = Verdadero y q = Falso.
#
# Esto ocurre porque se promete que si p ocurre,
# entonces q también debe ocurrir, pero no se cumple.


# Pregunta 2:
# Explique qué significa ¬(p ∧ q) ≡ ¬p ∨ ¬q
# y dé un ejemplo propio.
#
# Significa que negar una conjunción es equivalente
# a negar al menos una de las proposiciones.
#
# Ejemplo:
#
# p = "El usuario tiene internet"
# q = "El servidor está activo"
#
# ¬(p ∧ q):
# "No es cierto que el usuario tenga internet
# y el servidor esté activo"
#
# Es equivalente a:
#
# ¬p ∨ ¬q:
# "El usuario no tiene internet
# o el servidor no está activo"


# Pregunta 3:
# ¿Cuál expresión es tautología y cuál es contradicción?
#
# Tautología:
# p ∨ ¬p
#
# porque siempre es verdadera.
#
# Contradicción:
# p ∧ ¬p
#
# porque siempre es falsa.


# Pregunta 4:
# En el sistema de acceso,
# ¿qué combinación mínima de valores verdaderos permite acceso?
#
# La combinación mínima es:
#
# u = Verdadero
# c = Verdadero
# h = Verdadero
# a = Falso
#
# porque basta con estar en horario permitido
# aunque no sea administrador.
#
# También funciona:
#
# u = Verdadero
# c = Verdadero
# a = Verdadero
# h = Falso
#
# ya que basta una de las dos condiciones:
# administrador o estar en horario.