#utilitarios
def feedback_opcion_invalida():
    print("Debe ingresar una opcion válida")
    print()

def pedir_opcion():
    opcion = input("Opción deseada: ")
    print("")
    return opcion

def es_numero_valido(input):
    esValido = True
    try:
        int(input)
    except ValueError:
        esValido = False
    return esValido

##DNI
dnis = []

def indice_no_esta_en_la_lista(indice, lista):
    return indice > len(lista) or indice < 1

def registrar_dni():
    dni = input("Ingrese el DNI: ")
    if es_numero_valido(dni):
        dnis.append(dni)
    else:
        print("Debe ingresar un DNI válido")
    print()

def imprimir_lista_dnis(lista_dnis):
    i = 1
    for dni in lista_dnis:
        print(f"{i} DNI {dni}")
        i += 1

#conjuntos
def generar_conjuntos():
    for dni in dnis:
        print(set(dni))
        print()

def operar_conjuntos(operacion):
    copia_dnis = list(dnis)
    resultado = None
    seguir = True
    while(seguir):
        print("Seleccionar conjuntos: ")
        imprimir_lista_dnis(copia_dnis)
        opcion = input("Conjunto: ")
        if es_numero_valido(opcion):
            indice = int(opcion)
            if indice_no_esta_en_la_lista(indice, copia_dnis):
                feedback_opcion_invalida()
            else:
                conjunto = copia_dnis[indice - 1]
                if resultado is not None:
                    match operacion:
                        case 1:
                            resultado = resultado | set(conjunto)
                        case 2:
                            resultado = resultado & set(conjunto)
                        case 3:
                            resultado = resultado - set(conjunto)
                        case 4:
                            resultado = resultado ^ set(conjunto)
                    print(f"resultado: {resultado}")
                else:
                    resultado = set(conjunto)
                copia_dnis.remove(copia_dnis[indice - 1])
        else:
            feedback_opcion_invalida()

        if len(copia_dnis) == 0:
            seguir = False
        else:
            mas_operaciones = ""
            while(mas_operaciones != "S" and mas_operaciones != "N"):
                mas_operaciones = input("Seguir (S/N)?: ")
                mas_operaciones = mas_operaciones.capitalize()
                if mas_operaciones == "S":
                    seguir = True
                elif mas_operaciones == "N":
                    seguir = False

#ciclos
def operar_digitos(operacion):
    print("Seleccione un DNI:")
    imprimir_lista_dnis(dnis)
    opcion_seleccionada = input("DNI: ")
    if es_numero_valido(opcion_seleccionada):
        indice = int(opcion_seleccionada)
        if indice_no_esta_en_la_lista(indice, dnis):
            feedback_opcion_invalida()
        else:
            match operacion:
                case 1:
                    dni = dnis[indice - 1]
                    ocurrencia_digitos = dict()
                    for digito in dni:
                        if ocurrencia_digitos.get(digito) is None:
                            ocurrencia_digitos[digito] = 1
                        else:
                            ocurrencia_digitos[digito] = ocurrencia_digitos[digito] + 1
                    print(ocurrencia_digitos)
                case 2:
                    dni = dnis[indice - 1]
                    acumulado = 0
                    for digito in dni:
                        acumulado = acumulado + int(digito)
                    print(acumulado)

def condiciones_logicas():
    def grupo_sin_ceros():
        for dni in dnis:
            if '0' in set(dni):
                return False
        return True

    def digito_compartido():
        if len(dnis) >= 2:
            interseccion = set(dnis[0]) & set(dnis[1])
            for i in range(2, len(dnis)):
                interseccion = interseccion & dnis[i]
            return interseccion
        return set()

    def diversidad_numerica_alta():
            for dni in dnis:
                if len(set(dni)) > 6:
                    return True
            return False

    compartidos = digito_compartido()
    if grupo_sin_ceros():
        print("Grupo sin ceros")
    if len(compartidos) > 0:
        print(f"Dígitos compartidos: {compartidos}")
    if diversidad_numerica_alta():
        print("Diversidad numérica alta")

##años
anios_de_nacimiento = []

def ingresa_anio():
    anio = input("Ingrese el año de nacimiento: ")
    if len(anio) == 4 and es_numero_valido(anio):
        anios_de_nacimiento.append(anio)
    else:
        print("Debe ingresar un año válido")

def operar_con_anios():
    def es_anio_bisiesto(anio):
        bisiesto = False
        if anio >= 0:    
            if anio % 4 == 0:
                bisiesto = True
                if anio % 100 == 0:
                    bisiesto = False
                    if anio % 400 == 0:
                        bisiesto = True
        return bisiesto

    def anios_pares():
        pares = 0
        impares = 0
        for anio in anios_de_nacimiento:
            if anio % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
        if pares > 0:
            print(f"{pares} personas nacieron en año par")
        if impares > 0:
            print(f"{pares} personas nacieron en año impar")

    def gen_z():
        es_gen_z = True
        for anio in anios_de_nacimiento:
            if int(anio) < 2000:
                es_gen_z = False
                break
        if es_gen_z:
            print("Grupo Z")
    
    def anio_especial():
        for anio in anios_de_nacimiento:
            if es_anio_bisiesto(int(anio)):
                print("Tenemos un año especial")


#menus
def menu_dni():
    def menu_dni_conjuntos():
        texto_menu = """1.- Imprimir conjuntos
2.- Unión de conjuntos
3.- Intersección de conjuntos
4.- Diferencia de conjuntos
5.- Diferencia simetrica de conjuntos
6.- Salir
"""
        opcion = ""
        while(opcion != "6"):
            print(texto_menu)
            opcion = pedir_opcion()
            match opcion:
                case "1":
                    generar_conjuntos()
                case "2":
                    operar_conjuntos(1)
                case "3":
                    operar_conjuntos(2)
                case "4":
                    operar_conjuntos(3)
                case "5":
                    operar_conjuntos(4)

    def menu_dni_digitos():
        texto_menu = """1.- Conteo de frecuencia
2.- Suma de digitos
3.- Condiciones lógicas
4.- Salir
"""
        opcion = ""
        while(opcion != "4"):
            print(texto_menu)
            opcion = pedir_opcion()
            match opcion:
                case "1":
                    operar_digitos(1)
                case "2":
                    operar_digitos(2)
                case "3":
                    condiciones_logicas()
    
    opcion = ""
    while(opcion != "0"):
        print("1.- Ingresar DNI")
        #si hay + de 2 DNIs
        if len(dnis) > 1:
            print("2.- Operaciones con conjuntos")
        else:
            print("Operaciones de conjuntos (ingrese al menos 2 DNIs)")
        #si hay al menos 1 DNI
        if len(dnis) > 0:
            print("3.- Operaciones con digitos")
        else:
            print("Operaciones con digitos (ingrese al menos 1 DNI)") 
        print("0.- Salir")
        opcion = pedir_opcion()
        match opcion:
            case "1":
                registrar_dni()
            case "2":
                if len(dnis) > 1:
                    menu_dni_conjuntos()
            case "3":
                if len(dnis) > 0:
                    menu_dni_digitos()

def menu_anio():
    opcion = ""
    while(opcion != "0"):
        print("1.- Ingresar año de nacimiento")
        if len(anios_de_nacimiento) == 0:
            print("Ingrese al menos un año de nacimiento para operar")
        else:
            print("2.- Operar")

        opcion = pedir_opcion()

opcion = ""
while(opcion != "3"):
    print("1.- Operaciones con DNI")
    print("2.- Operaciones con año de nacimiento")
    print("3.- Salir")
    opcion = pedir_opcion()
    if opcion == "1":
        menu_dni()
    elif opcion == "2":
        menu_anio()
    