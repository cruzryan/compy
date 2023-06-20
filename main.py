import copy
import pickle

from ui import *
import utils_comp
import time
import fk as fk

TIEMPO_A_DORMIR = 3

main_afn = utils_comp.AFN()
main_tabla_union = list()
tabla_resultado_union_lexico = list(list())
terminales_tokens_ll1 = list()
terminales_tokens_lr0 = list()
terminales_tokens_lr1 = list()

window = sg.Window("2ndo Parcial", layout, size=(1600, 700), )

def crear_popup(tipo, valores=None):
    if tipo == 'basico':
        mensaje = "Se ha creado un automata con:\n" \
                  "Caracter inferior: {}\n" \
                  "Caracter superior: {}\n" \
                  "ID: {}" \
            .format(valores['-char_inf-'], valores['-char_sup-'], valores['-id_basico-'])
        sg.popup(mensaje, title='Exito')
    elif tipo == 'Error':
        mensaje = 'verificar las entradas'
        sg.popup(mensaje, title='Error', text_color='Red')


def actualizar_campos():  
    ordernados = []
    for afn in main_afn.conjunto_AFNs:
        ordernados.append(afn.id_AFN)
    ordernados.sort()

    window['-id_positiva-'].update(values=ordernados)

    window['-id_kleen-'].update(values=ordernados)

    window['-id_1_union-'].update(values=ordernados)
    window['-id_2_union-'].update(values=ordernados)

    window['-id_1_concatenar-'].update(values=ordernados)
    window['-id_2_concatenar-'].update(values=ordernados)

    window['-id_convertir_a_afd-'].update(values=ordernados)

    global main_tabla_union
    main_tabla_union = ordernados.copy()
    tabla_resultado_union_lexico.clear()
    window['-UNION BASE LEXICO-'].update(values=main_tabla_union)
    window['-UNION RESULTADO LEXICO-'].update(values=[])


def crear_basico(valores):
    if valores['-id_basico-'] == '' or valores['-char_inf-'] == '' or valores['-char_sup-'] == '':
        crear_popup('Error')
        return
    if ord(valores['-char_inf-']) > ord(valores['-char_sup-']):
        sg.popup("Ingrese de ingresar un rango adecuado de valores", title='Error', text_color='Red')
        return
    if not valores['-id_basico-'].isnumeric():
        sg.popup("Ingrese un valor  numerico para el id", title='Error', text_color='Red')
        return
    if int(valores['-id_basico-']) in [afn.id_AFN for afn in main_afn.conjunto_AFNs]:
        sg.popup("Ingrese otro id que no exista", title='Error', text_color='Red')
        return
    temp_afn = utils_comp.AFN()
    main_afn.conjunto_AFNs.append(
        temp_afn.crear_afn_basico(values['-char_inf-'], values['-char_sup-'], int(values['-id_basico-'])))

    global main_tabla_union
    main_tabla_union.append(int(values['-id_basico-']))
    actualizar_campos()

    crear_popup('basico', values)
    window['-id_basico-'].update('')
    window['-char_sup-'].update('')
    window['-char_inf-'].update('')

    return True


def crear_positiva(valores):
    if valores['-id_positiva-'] == '':
        sg.popup("seleccionar un automata", title='Error', text_color='Red')
        return
    id_afn = int(valores['-id_positiva-'])
    for afn in main_afn.conjunto_AFNs:
        if afn.id_AFN == id_afn:
            afn.cerradura_positiva()
            actualizar_campos()
            sg.popup("Se ha aplicado la cerradura positiva al automata: {}".format(afn.id_AFN), title='Exito')
            return


def crear_kleen(valores):
    if valores['-id_kleen-'] == '':
        sg.popup("seleccionar un automata", title='Error', text_color='Red')
        return
    id_afn = int(valores['-id_kleen-'])
    for afn in main_afn.conjunto_AFNs:
        if afn.id_AFN == id_afn:
            afn.cerradura_kleen()
            actualizar_campos()
            sg.popup("Se ha aplicado la cerradura de kleen al automata: {}".format(afn.id_AFN), title='Exito')
            return


def agregar_union_lexico(valores):
    try:
        lugar = valores['-UNION BASE LEXICO-'][0]
        global main_tabla_union
        global tabla_resultado_union_lexico
        tabla_resultado_union_lexico.append([main_tabla_union.pop(lugar), 0])
        window['-UNION BASE LEXICO-'].update(values=main_tabla_union)
        window['-UNION RESULTADO LEXICO-'].update(values=tabla_resultado_union_lexico)
    except IndexError:
        sg.popup("No se ha seleccionado ningún elemento", title='Error', text_color='Red')


def eliminar_union_lexico(valores):
    try:
        lugar = valores['-UNION RESULTADO LEXICO-'][0]
        global main_tabla_union
        global tabla_resultado_union_lexico
        main_tabla_union.append(tabla_resultado_union_lexico.pop(lugar)[0])
        window['-UNION BASE LEXICO-'].update(values=main_tabla_union)
        window['-UNION RESULTADO LEXICO-'].update(values=tabla_resultado_union_lexico)
    except IndexError:
        sg.popup("No se ha seleccionado ningún elemento", title='Error', text_color='Red')


def token_union_lexico(valores):
    try:

        lugar = valores['-UNION RESULTADO LEXICO-'][0]
        token = values['-token_union_lexico-']
        global tabla_resultado_union_lexico
        tabla_resultado_union_lexico[lugar][1] = token
        window['-UNION RESULTADO LEXICO-'].update(values=tabla_resultado_union_lexico)
    except IndexError:
        sg.popup("seleccionar la casilla para agregar el token", title='Error', text_color='Red')


def unir_afns(valores):
    if valores['-id_1_union-'] == '' or valores['-id_2_union-'] == '':
        sg.popup("seleccionar los automatas a unir", title='Error', text_color='Red')
        return
    if valores['-id_1_union-'] == valores['-id_2_union-']:
        sg.popup("Selecciona dos automatas distintos", title='Error', text_color='Red')
        return
    id_1 = int(valores['-id_1_union-'])
    id_2 = int(valores['-id_2_union-'])
    for afn_1 in main_afn.conjunto_AFNs:
        if afn_1.id_AFN == id_1:
            for afn_2 in main_afn.conjunto_AFNs:
                if afn_2.id_AFN == id_2:
                    afn_1.unir_afn(afn_2)
                    main_afn.conjunto_AFNs.remove(afn_2)
                    actualizar_campos()
                    sg.popup("Se han unido exitosamente los automatas: {} y {}"
                             .format(afn_1.id_AFN, afn_2.id_AFN),
                             title='Exito')
                    # actualizar_todo() TODO implementar
                    return


def concatenar_afns(valores):
    if valores['-id_1_concatenar-'] == '' or valores['-id_2_concatenar-'] == '':
        sg.popup("seleccionar los automatas a concatenar", title='Error', text_color='Red')
        return
    if valores['-id_1_concatenar-'] == valores['-id_2_concatenar-']:
        sg.popup("Selecciona dos automatas distintos", title='Error', text_color='Red')
        return
    id_1 = int(valores['-id_1_concatenar-'])
    id_2 = int(valores['-id_2_concatenar-'])
    for afn_1 in main_afn.conjunto_AFNs:
        if afn_1.id_AFN == id_1:
            for afn_2 in main_afn.conjunto_AFNs:
                if afn_2.id_AFN == id_2:
                    afn_1.concatenar_afn(afn_2)
                    main_afn.conjunto_AFNs.remove(afn_2)
                    actualizar_campos()

                    sg.popup("Se han concatenado exitosamente los automatas: {} y {}"
                             .format(afn_1.id_AFN, afn_2.id_AFN),
                             title='Exito')
                    # actualizar_todo() TODO implementar
                    return


def crear_union_lexico():
    if len(tabla_resultado_union_lexico) < 1:
        sg.popup("Elija mas de un elemento para la union", title='Error', text_color='Red')
        return

    temp_afn = None
    list_res_afn = list()
    ids = list()
    tokens = list()
    for i in range(len(tabla_resultado_union_lexico)):
        ids.append(tabla_resultado_union_lexico[i][0])
        tokens.append(tabla_resultado_union_lexico[i][1])
    # copia_main = copy.deepcopy(main_afn.conjunto_AFNs)
    copia_main = main_afn.conjunto_AFNs.copy()
    sacados = 0
    for i in range(len(main_afn.conjunto_AFNs)):
        if copia_main[i].id_AFN == ids[0]:
            temp_afn = main_afn.conjunto_AFNs.pop(i - sacados)
            sacados += 1
        elif copia_main[i].id_AFN in ids:
            list_res_afn.append(main_afn.conjunto_AFNs.pop(i - sacados))
            sacados += 1
    main_afn.conjunto_AFNs.append(temp_afn.union_especial(list_res_afn, tokens))
    sg.popup("Se han unido exitosamente los automatas: {} y se ha colocado en el AFN con el id: {}"
             .format(ids, ids[0]),
             title='Exito')
    actualizar_campos()


def convertir_afd_a_afn(valores):
    if valores['-id_convertir_a_afd-'] == '':
        sg.popup("seleccionar un automata", title='Error', text_color='Red')
        return
    id_afn = int(valores['-id_convertir_a_afd-'])
    for afn in main_afn.conjunto_AFNs:
        if afn.id_AFN == id_afn:
            tabla = afn.convertir_a_afd(valores['-nobre_archhivo_afn_afd-'])
            window['-resultado_conversion_afn_afd-'].update(tabla)
            window['-id_convertir_a_afd-'].update('')
            actualizar_campos()
            sg.popup("El automata {} se ha convertido exitosamente".format(afn.id_AFN), title='Exito')
            return


def probar_analizador_lexico(valores):
    if valores['-nombre_afd_txt-'] == '':
        sg.popup("ingresar el nombre del archivo", title='Error', text_color='Red')
        return
    if valores['-cadena_sigma_al-'] == '':
        sg.popup("ingresar una cadena a evaluar", title='Error', text_color='Red')
        return
    sigma = valores['-cadena_sigma_al-']
    nom_txt = valores['-nombre_afd_txt-']

    try:
        open(f"{nom_txt}.txt", "r")
    except FileNotFoundError:
        sg.popup(f"El archivo {nom_txt}.txt no existe", title='Error', text_color='Red')
        return

    anal_lexico = utils_comp.AnalizadorLexico(sigma, nom_txt)

    tabla_lexemas = list()

    # while anal_lexico.token != '«' and anal_lexico.token != 'ø' and anal_lexico.token is None:

    token = anal_lexico.yylex()

    while token != '0':
        # time.sleep(TIEMPO_A_DORMIR)
        holder_lexema = list()

        token_temp = anal_lexico.token
        yytext_temp = anal_lexico.yytext
        holder_lexema.append(token_temp)
        holder_lexema.append(yytext_temp)

        tabla_lexemas.append(holder_lexema)

        token = anal_lexico.yylex()

    window['-tabla_res_al-'].update(values=tabla_lexemas)


def evaluar_postfijo(valores):
    sigma = valores['-val_post-']

    evaluador_p = utils_comp.DescensoRecursivoCalc(sigma)
    if evaluador_p.ini_eval():
        window['-res_post-'].update(value=evaluador_p.resultado)
        window['-ex_post-'].update(value=evaluador_p.e_post_fija)
    else:
        sg.popup("Expresión sintácticamente incorrecta", title='Error', text_color='Red')


def convertir_de_er(valores):
    if valores['-nombre_afd_er_txt-'] == '':
        sg.popup("ingresar el nombre del archivo", title='Error', text_color='Red')
        return
    if valores['-in_er-'] == '':
        sg.popup("ingresar una cadena a evaluar", title='Error', text_color='Red')
        return
    try:
        id_er = int(valores['-id_afn_er-'])
        if id_er in [afn.id_AFN for afn in main_afn.conjunto_AFNs]:
            sg.popup("Ingrese otro id que no exista", title='Error', text_color='Red')
            return
        expresion_r = valores['-in_er-']

        convertidor = utils_comp.ERaAFN(expresion_r)
        if not convertidor.ini_conversion():
            sg.popup("Verfique la expresion regular", title='Error', text_color='Red')
            return
        convertidor.afd_result.id_AFN = id_er
        main_afn.conjunto_AFNs.append(convertidor.afd_result)

        sg.popup("Se ha convertida la expresion regular correctamente", title='Exito')
        actualizar_campos()
    except ValueError:
        sg.popup("ingresar un valor entero para el id", title='Error', text_color='Red')


def analisis_ll1(valores):
    print("Analizando Gramatica!")
    sigma = valores['-sigma_ll1-']

    terminales_tokens_ll1.clear()
    dr_gg = utils_comp.DescensoRecGramGram(sigma)

    if not dr_gg.analizar_gramatica():
        sg.popup("Gramatica no LL(1)", title='Error', text_color='Red')
        return
    sg.popup("Aceptada", title='Status de Gramatica')

    dr_gg.calcular_tabla_ll1()

    # tokens_ll1 = [-1 for i in range(0, len(dr_gg.v_t))]
    # res_termi_tokens = list()

    for index, simbolo in enumerate(dr_gg.v_t):
        terminales_tokens_ll1.append([simbolo, '-1'])

    window['-ll1_no_terminales-'].update(values=dr_gg.v_n)
    window['-ll1_terminales-'].update(values=terminales_tokens_ll1)

    # with open("res_ll1.txt", "w") as tabla_ll1_en_txt:
    #
    #     print('Regla:', end='#', file=tabla_ll1_en_txt)
    #     for terminal in dr_gg.v_t:
    #         print(terminal, end='#', file=tabla_ll1_en_txt)
    #     print('$', end='#', file=tabla_ll1_en_txt)
    #     print(file=tabla_ll1_en_txt)
    #
    #     reglas = copy.copy(dr_gg.v_n)
    #     reglas.append('$')
    #
    #     for index, fila in enumerate(dr_gg.tabla_ll1):
    #         print(reglas[index], end=';', file=tabla_ll1_en_txt)
    #         for valor in fila:
    #             print(valor, end=';', file=tabla_ll1_en_txt)
    #         print(file=tabla_ll1_en_txt)

    with open("res_ll1.pickle", "wb") as f_res:
        pickle.dump(dr_gg, f_res)


def mostrar_tabla_ll1():
    try:
        # with open("res_ll1.txt", "r") as archivo_t_ll1:
        with open("res_ll1.pickle", "rb") as archivo_t_ll1:
            # encabezados_ll1 = archivo_t_ll1.readline()
            # lista_encabezados = encabezados_ll1.split('#')
            # lista_encabezados.pop()
            # # print(len(lista_encabezados))
            #
            # tabla_ll1 = list()
            #
            # total_lineas = archivo_t_ll1.readlines()
            # for linea in total_lineas:
            #     arr_linea = linea.split(sep=';')
            #     arr_linea.pop()
            #     # print(len(arr_linea))
            #     tabla_ll1.append(arr_linea)
            r_ll1 = pickle.load(archivo_t_ll1)
            lista_encabezados = copy.copy(r_ll1.v_t)
            lista_encabezados.insert(0, 'Regla')
            lista_encabezados.append('$')

            diseno = [
                [sg.Text("Tabla LL(1)")],
                [
                    sg.Table(
                        values=r_ll1.tabla_ll1,
                        headings=lista_encabezados,
                        auto_size_columns=False,
                        def_col_width=10,
                        expand_x=False,
                        vertical_scroll_only=False,
                        # display_row_numbers=True,
                        row_height=20,
                        justification='center',
                        key='-tabla_ll1_ventana-',
                    ),
                ],
            ]

            ventana = sg.Window("Tabla LL(1)", diseno, finalize=True)

            # tabla = ventana['-tabla_ll1_ventana-'].Widget
            # tabla.heading('Row', text='Regla')

            while True:
                evento, info = ventana.read()
                if evento == "Exit" or evento == sg.WIN_CLOSED:
                    break

            ventana.close()

    except FileNotFoundError:
        sg.popup("  analizar primero una gramatica", title='Error', text_color='Red')


# EVALUANDO SIGMAAA

def evaluar_sigma_ll1(valores):

    print("Evaluando Sigma!")
    if valores['-archivo_afd_ll1-'] == '':
        sg.popup("ingresar el nombre del archivo", title='Error', text_color='Red')
        return
    if valores['-sigma_eval_ll1-'] == '':
        sg.popup("ingresar una cadena a evaluar", title='Error', text_color='Red')
        return

    if len(terminales_tokens_ll1) == 0:
        sg.popup("asignar todos los tokens", title='Error', text_color='Red')
        return
    for s, t in terminales_tokens_ll1:
        if t == '-1':
            sg.popup("asignar todos los tokens", title='Error', text_color='Red')
            return

    nom_txt = valores['-archivo_afd_ll1-']
    sigma = valores['-sigma_eval_ll1-']

    try:
        open(f"{nom_txt}.txt", "r")
    except FileNotFoundError:
        sg.popup(f"El archivo {nom_txt}.txt no existe", title='Error', text_color='Red')
        return

    with open("res_ll1.pickle", "rb") as archivo_t_ll1:
        r_ll1 = pickle.load(archivo_t_ll1)
        if not r_ll1.evaluar_con_ll1(sigma, nom_txt):
            sg.popup("Cadena sintacticamente incorrecta", title='Error', text_color='Red')
            window['-ll1_pila-'].update(values=r_ll1.tabla_txt_eval_ll1)
            return
        sg.popup("Gramatica sintacticamente correcta", title='Exito')
        window['-ll1_pila-'].update(values=r_ll1.tabla_txt_eval_ll1)
    
    fk.shg()

    # a_ll1 = clases.AnalizadorLL1(sigma, nom_txt, terminales_tokens_ll1)
    # a_ll1.obtener_tokens()


def asignar_token_ll1(valores):

    print("VALORES: ", valores)
    tokens_vt = valores['-token_ll1-']

    print("TOKENS: ", tokens_vt)
    r_ll1 = None
    if tokens_vt == '':
        sg.popup("ingresar un token", title='Error', text_color='Red')
        return
    try:
        with open("res_ll1.pickle", "rb") as archivo_t_ll1:
            r_ll1 = pickle.load(archivo_t_ll1)

            lugar = valores['-ll1_terminales-'][0]
            print("LUGAR: ", lugar)
            terminales_tokens_ll1[lugar][1] = tokens_vt

            # DICT = { [token] : [simbolo] }
            r_ll1.tokens_vt[terminales_tokens_ll1[lugar][1]] = terminales_tokens_ll1[lugar][0]

            window['-ll1_terminales-'].update(values=terminales_tokens_ll1)

        with open("res_ll1.pickle", "wb") as archivo_t_ll1:
            pickle.dump(r_ll1, archivo_t_ll1)
    except IndexError:
        sg.popup("seleccionar la casilla para agregar el token", title='Error', text_color='Red')


def asignar_tokens_ll1_rapido(valores):
    
    r_ll1 = None
    with open("res_ll1.pickle", "rb") as archivo_t_ll1:
        r_ll1 = pickle.load(archivo_t_ll1)
        # Loop from 0 to 7
        for i in range(1, 8):
            lugar = i-1
            print("LUGAR: ", lugar)
            terminales_tokens_ll1[lugar][1] = (i)*10
            r_ll1.tokens_vt[terminales_tokens_ll1[lugar][1]] = terminales_tokens_ll1[lugar][0]
            window['-ll1_terminales-'].update(values=terminales_tokens_ll1)

    with open("res_ll1.pickle", "wb") as archivo_t_ll1:
        pickle.dump(r_ll1, archivo_t_ll1)

    print("VALORES RAPIDO: ")
    print(valores)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WINDOW_CLOSED:
        break
    elif event == "-BASICO-":
        crear_basico(values)
    elif event == "-UNION-":
        unir_afns(values)
    elif event == '-CONCATENAR-':
        concatenar_afns(values)
    elif event == "-POSITIVA-":
        crear_positiva(values)
    elif event == "-KLEEN-":
        crear_kleen(values)
    elif event == "-ANADIR UNION LEXICO-":
        agregar_union_lexico(values)
    elif event == "-ELIMINAR UNION LEXICO-":
        eliminar_union_lexico(values)
    elif event == "-TOKEN UNION LEXICO-":
        token_union_lexico(values)
    elif event == "-UNION LEXICO-":
        crear_union_lexico()
    elif event == "-CONVERTIR AFD A AFN-":
        convertir_afd_a_afn(values)
    elif event == '-PROBAR ANALIZADOR LEXICO-':
        probar_analizador_lexico(values)
    elif event == '-POSTFIJO-':
        evaluar_postfijo(values)
    elif event == '-ER A AFN-':
        convertir_de_er(values)
    elif event == "-ANALIZAR LL(1)-":
        analisis_ll1(values)
    elif event == "-MOSTRAR TABLA LL(1)-":
        mostrar_tabla_ll1()
    elif event == "-EVALUAR SIG LL1-":
        evaluar_sigma_ll1(values)
    elif event == "-TOKEN LL(1)-":
        asignar_token_ll1(values)
    elif event == "-TOKEN AGREGAR RAPIDO-":
        asignar_tokens_ll1_rapido(values)


window.close()
