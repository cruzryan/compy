import PySimpleGUI as sg
# import BUClases as clases
from clases import *
import time

TIEMPO_A_DORMIR = 3

main_afn = AFN()
main_tabla_union = list()
tabla_resultado_union_lexico = list(list())

#                                           Definicion de mis pantallas del tab AFN's

#                     - Pantalla de la creacion de un AFN basico
ly_basico = [
    [sg.Text('CREACIÓN DE UN AUTOMATA BÁSICO')],
]

#                     - Pantalla de la union de dos AFNs
ly_unir = [
    [sg.Text('UNIÓN DE DOS AUTOMATAS', size=(60, 1))],

]

#                     - Pantalla de la concatenación de dos AFNs
ly_concatenar = [
    [sg.Text('CONCATENACIÓN DE DOS AUTOMATAS', size=(60, 1))],
]

#                     - Pantalla para aplicar la cerradura positiva a un AFN
ly_positiva = [
    [sg.Text('OPERACIÓN CERRADURA POSITIVA/TRANSITIVA', size=(60, 1))],
]

#                     - Pantalla para aplicar la cerradura de kleen a un AFN
ly_kleen = [
    [sg.Text('OPERACIÓN CERRADURA DE KLEEN', size=(60, 1))],
]

ly_post = [
    [sg.Text('EVALUADOR DE EXPRESION Y CONVERSIÓN A POSTFIJA')],
]

ly_er_a_afn = [
    [sg.Text('CONERSION DE EXPRESION REGULAR A AFN')],
]

#                     - Pantalla para realizar la union para un analizador lexico
ly_union_lexico = [
    [sg.Text('CREACIÓN DE UN ANALAIZADOR LEXICO DE UN AFD', size=(60, 1))],

]

ly_afn_a_afd = [
    [sg.Text('CONVERSION DE UN AUTOMATA AFN A AFD', size=(60, 1))],

]

ly_analizar_cadena = [
    [sg.Text('TODO LLENAR CON INFO PARA ANALIZAR CADENA')]
]

ly_probar_analizador = [
    [sg.Text('PROBADOR DE UN ANALIZADOR LEXICO')],
]

#                                           Definicion de mis pantallas del tab Analizador sintáctico
#                     - Pantalla para...

# ly_a_ll1 = [
#     [sg.Text('ANALIZADOR LL(1)', size=(15, 1))],
#     [sg.Text('Gramatica', size=(15, 1))],
#     [sg.Multiline('', size=(160, 10), key='-sigma_ll1-')],
#     [
#         sg.Button('Crear tabla', key='-A LL(1)-', size=(20, 1)),
#         sg.Button('Mostrar tabla', key='-MOSTRAR TABLA LL(1)-', size=(20, 1))
#     ],
#     [
#         sg.Table(
#             values=[],
#             headings=['No terminal'],
#             justification='center',
#             alternating_row_color='grey',
#             key='-ll1_no_terminales-',
#             num_rows=5,
#             auto_size_columns=False,
#             def_col_width=21,
#         ),
#         sg.Table(
#             values=[],
#             headings=['Terminal'],
#             justification='center',
#             alternating_row_color='grey',
#             key='-ll1_terminales-',
#             num_rows=5,
#             auto_size_columns=False,
#             def_col_width=21,
#         ),
#     ],
# ]

#                                           Definicion de mi pantalla del subgrupo del tab de AFN's
# ly_sbgrp1 = [[
#     sg.TabGroup([[
#         sg.Tab(
#             'Creación de AFN básico',
#             ly_basico,
#             background_color='Red',
#             element_justification='center'
#         ),
#         sg.Tab(
#             'Unir',
#             ly_unir,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Concatenar',
#             ly_concatenar,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Cerradura +',
#             ly_positiva,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Cerradura *',
#             ly_kleen,
#             title_color='Black',
#             background_color='RoyalBlue1'
#         ),
#         sg.Tab(
#             'Evaluador y Posfijo',
#             ly_post,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'ER -> AFN',
#             ly_er_a_afn,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Unión para analizador léxico',
#             ly_union_lexico,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Convertir AFN a AFD',
#             ly_afn_a_afd,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Analizar una cadena',
#             ly_analizar_cadena,
#             title_color='Black',
#             background_color='Pink'
#         ),
#         sg.Tab(
#             'Probar analizador léxico',
#             ly_probar_analizador,
#             title_color='Black',
#             background_color='Pink',
#             element_justification='center'
#         ),
#     ]],
#         tab_location='topleft', title_color='Grey', tab_background_color='White', selected_title_color='Black',
#         selected_background_color='White', border_width=5)]]
#
# #                                           Definicion de mi pantalla del subgrupo del tab de Analizador sintacatico
# ly_sbgrp2 = [[
#     sg.TabGroup([[
#         sg.Tab(
#             'Analizador LL(1)',
#             ly_a_ll1,
#             background_color='Green',
#         ),
#     ]],
#         tab_location='topleft', title_color='Grey', tab_background_color='White', selected_title_color='Black',
#         selected_background_color='White', border_width=5)]]

#                                           Definicion de mi pantalla general
# layout = [[
#     sg.TabGroup([[
#         sg.Tab('AFN\'s', ly_sbgrp1, background_color='Green', element_justification='center'),
#         sg.Tab('Analizador sintáctico', ly_sbgrp2, title_color='Black', background_color='Pink')]
#     ],
#         tab_location='topleft', title_color='Grey', tab_background_color='White', selected_title_color='Black',
#         selected_background_color='White', border_width=5)]]

# Define Window
window = sg.Window("Compiladores", layout, size=(1500, 500))


# Read  values entered by user
# def analisis_ll1(valores):
#     sigma = valores['-sigma_ll1-']
#     # print("Analisis LL(1) de:")
#     # print(sigma)
#
#     dr_gg = DescensoRecGramGram(sigma)
#     # print(dr_gg.analizar_gramatica())
#
#     if not dr_gg.analizar_gramatica():
#         sg.popup("Gramatica no LL(1)", title='Error', text_color='Red')
#         return
#     sg.popup("Gramatica aceptada", title='Exito')
#
#     dr_gg.calcular_tabla_ll1()
#
#     window['-ll1_no_terminales-'].update(values=dr_gg.v_n)
#     window['-ll1_terminales-'].update(values=dr_gg.v_t)
#
#     with open("res_ll1.txt", "w") as tabla_ll1_en_txt:
#         for terminal in dr_gg.v_t:
#             print(terminal, end='#', file=tabla_ll1_en_txt)
#         print(file=tabla_ll1_en_txt)
#
#         for fila in dr_gg.tabla_ll1:
#             for valor in fila:
#                 print(valor, end=';', file=tabla_ll1_en_txt)
#             print(file=tabla_ll1_en_txt)


# def mostrar_tabla_ll1():
#     try:
#         with open("res_ll1.txt", "r") as archivo_t_ll1:
#             encabezados = archivo_t_ll1.readline()
#             lista_encabezados = encabezados.split('#')
#             lista_encabezados.pop()
#             # print(len(lista_encabezados))
#
#             tabla_ll1 = list()
#
#             total_lineas = archivo_t_ll1.readlines()
#             for linea in total_lineas:
#                 arr_linea = linea.split(sep=';')
#                 arr_linea.pop()
#                 # print(len(arr_linea))
#                 tabla_ll1.append(arr_linea)
#
#             diseno = [
#                 [sg.Text("Tabla LL(1)")],
#                 [
#                   sg.Table(
#                       values=tabla_ll1,
#                       headings=lista_encabezados,
#                       auto_size_columns=False,
#                       def_col_width=10,
#                       expand_x=False,
#                       vertical_scroll_only=False,
#                       display_row_numbers=True,
#                       row_height=20,
#                       justification='center',
#                       key='-tabla_ll1_ventana-',
#                   ),
#                 ],
#             ]
#
#             ventana = sg.Window("Tabla LL(1)", diseno, finalize=True)
#
#             tabla = ventana['-tabla_ll1_ventana-'].Widget
#             tabla.heading('Row', text='Regla')
#
#             while True:
#                 evento, info = ventana.read()
#                 if evento == "Exit" or evento == sg.WIN_CLOSED:
#                     break
#
#             ventana.close()
#
#     except FileNotFoundError:
#         sg.popup("Favor de analizar primero una gramatica", title='Error', text_color='Red')


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WINDOW_CLOSED:
        break
    # elif event == "-A LL(1)-":
    #     analisis_ll1(values)
    # elif event == "-MOSTRAR TABLA LL(1)-":
    #     mostrar_tabla_ll1()

window.close()
