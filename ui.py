import PySimpleGUI as sg
sg.theme('LightGreen6')
sg.set_options(font=("Raleway", 13))

ly_basico = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('Caracter inferior', size=(20, 1), font=("Raleway",13), text_color='Black',background_color='White'), sg.In('', key='-char_inf-', font=("Raleway",13), text_color='Black',background_color='#F2F2F2')],
    [sg.Text('Caracter superior', size=(20, 1), font=("Raleway",13), text_color='Black',background_color='White'), sg.In('', key='-char_sup-', font=("Raleway",13), text_color='Black',background_color='#F2F2F2')],
    [sg.Text('ID', size=(20, 1), font=("Raleway",13), text_color='Black',background_color='White'), sg.In('', key='-id_basico-', font=("Raleway",13), text_color='Black',background_color='#F2F2F2')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Submit('Crear AFN', font=("Raleway",13), button_color = ('black','white'), key='-BASICO-')],
]

ly_unir = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [   
        sg.Text('Unir:', size=(10, 1)), sg.Combo([], key='-id_1_union-', size=(15, 1)),
        sg.Text('con:', size=(10, 1)), sg.Combo([], key='-id_2_union-', size=(15, 1)),
    ],
    [sg.Button('Unir', key='-UNION-', size=(40, 1))],
]

#                     - Pantalla de la concatenación de dos AFNs
ly_concatenar = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [
        sg.Text('Concatenar:', size=(10, 1)), sg.Combo([], key='-id_1_concatenar-', size=(15, 1)),
        sg.Text('con:', size=(10, 1)), sg.Combo([], key='-id_2_concatenar-', size=(15, 1)),
    ],
    [sg.Button('Concatenar', key='-CONCATENAR-', size=(40, 1))],
]

#                     - Pantalla para aplicar la cerradura positiva a un AFN
ly_positiva = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('Realizar Cerradura Positiva:', size=(20, 1)), sg.Combo([''], key='-id_positiva-', size=(8, 1))],
    [sg.Button('Cerradura Positiva', key='-POSITIVA-')]
]

#                     - Pantalla para aplicar la cerradura de kleen a un AFN
ly_kleen = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('Realizar operacion cerradura kleene:', size=(20, 1)), sg.Combo([''], key='-id_kleen-', size=(8, 1))],
    [sg.Button('Cerradura Kleene', key='-KLEEN-')]
]

ly_er_a_afn = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('Expresion regular:')],
    [sg.In('', key='-in_er-', size=(100, 1))],
    [sg.Text('Id para el AFN:')],
    [sg.In('', key='-id_afn_er-', size=(20, 1))],
    [sg.Button('Crear AFN', key='-ER A AFN-')],
]

ly_union_lexico = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [
        sg.Table(
            values=[],
            headings=['AFN sin seleccionar'],
            justification='center',
            alternating_row_color='grey',
            key='-UNION BASE LEXICO-',
            num_rows=5,
            auto_size_columns=False,
            def_col_width=30,
        ),
        sg.Column(
            [
                [sg.Button('Añadir seleccionado', key='-ANADIR UNION LEXICO-', size=(18, 1))],
                [sg.Button('Eliminar seleccionado', key='-ELIMINAR UNION LEXICO-', size=(18, 1))],
            ],
            element_justification='center'
        ),
        sg.Table(
            values=[[]],
            headings=['AFN seleccionado', 'Token'],
            justification='center',
            alternating_row_color='grey',
            background_color='White',
            key='-UNION RESULTADO LEXICO-',
            num_rows=5,
            auto_size_columns=False,
            def_col_width=15,
        ),
    ],
    [
        sg.Column(
            [
                [sg.Text('Valor del token')],
                [sg.In('', key='-token_union_lexico-')],
                [sg.Button('Agregar', key='-TOKEN UNION LEXICO-', size=(18, 1))],
            ],
            element_justification='center'
        ),
    ],
    [sg.Button('Unir todos los seleccionados', key='-UNION LEXICO-', size=(50, 1))],
]

encabezados = [f'{chr(i)}' for i in range(32, 127)]  
encabezados.append("Token")
ly_afn_a_afd = [
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    [sg.Text('', font=("Raleway",13), text_color='Black',background_color='White')],
    
    [
        sg.Text('Seleccionar automata'),
        sg.Combo([''], key='-id_convertir_a_afd-', size=(8, 1)),
    ],
    [
        sg.Table(
            values=[[]],
            headings=encabezados,
            auto_size_columns=False,
            def_col_width=5,
            expand_x=False,
            vertical_scroll_only=False,
            display_row_numbers=True,
            justification='center',
            key='-resultado_conversion_afn_afd-'
        ),
    ],
    [sg.Text('Nombre del archivo'), sg.In('', key='-nobre_archhivo_afn_afd-')],
    [sg.Button('Convetir', key='-CONVERTIR AFD A AFN-')],

]

ly_probar_analizador = [
    [sg.Text('PROBADOR DE UN ANALIZADOR LEXICO')],
    [sg.Text('Path del AFD'), sg.In('', key='-nombre_afd_txt-', size=(24, 1))],
    [sg.Text('Sigma:')],
    [sg.Multiline('', size=(160, 5), key='-cadena_sigma_al-')],
    [sg.Button('Analizar', key='-PROBAR ANALIZADOR LEXICO-')],
    [
        sg.Table(
            values=[[]],
            headings=['Token', 'Lexema'],
            auto_size_columns=False,
            def_col_width=40,
            key='-tabla_res_al-',
            justification='center',
        )
    ]
]

placeholder_sigma_ll1 = "E -> T Ep ;\n" \
                        "Ep -> mas T Ep | menos T Ep | epsilon ;\n" \
                        "T -> F Tp ;\n" \
                        "Tp -> por F Tp | entre F Tp | epsilon ;\n" \
                        "F -> parenI E parenD | num ;"

ly_a_ll1 =[    [sg.Text('', size=(15, 1), font=("Raleway", 13), text_color='Black', background_color='White')],
    [sg.Text('Gramatica', size=(71, 1), font=("Raleway", 13), text_color='Black', background_color='White')],
    [sg.Multiline(placeholder_sigma_ll1, size=(80, 10), key='-sigma_ll1-')],
    [        sg.Button('Analizar', key='-ANALIZAR LL(1)-', size=(20, 1)),        sg.Button('Desplegar tabla', key='-MOSTRAR TABLA LL(1)-', size=(20, 1))    ],
    [        sg.Table(            values=[],
            headings=['No terminal'],
            justification='center',
            alternating_row_color='white',
            key='-ll1_no_terminales-',
            num_rows=5,
            auto_size_columns=False,
            def_col_width=21,
        ),
        sg.Table(
            values=[],
            headings=['Terminal', 'Token'],
            justification='center',
            alternating_row_color='white',
            key='-ll1_terminales-',
            num_rows=5,
            auto_size_columns=False,
            def_col_width=21,
        ),
        sg.Column(
            [
                [sg.Text('Token')],
                [sg.In('', key='-token_ll1-')],
                [sg.Button('Cambiar Token', key='-TOKEN LL(1)-')],
                [sg.Button('Cambiar RAPIDO', key='-TOKEN AGREGAR RAPIDO-')],
            ],
        )
    ],
    [sg.Text('Path del archivo'), sg.In('./pruebas/afd_pe', key='-archivo_afd_ll1-')],
    [sg.Text('Sigma a evaluar')],
    [sg.In('', key='-sigma_eval_ll1-')],
    [sg.Button('Evaluar', key='-EVALUAR SIG LL1-')],
    [        sg.Table(            values=[],
            headings=['Stack', 'Cadena'],
            justification='center',
            alternating_row_color='grey',
            key='-ll1_pila-',
            num_rows=10,
            auto_size_columns=False,
            def_col_width=21,
        )
    ]
]
ly_sbgrp1 = [[
    sg.TabGroup([[
        sg.Tab(
            'Crear AFN',
            ly_basico,
            background_color='White',
            element_justification='center',
        ),
        sg.Tab(
            'Unir AFN',
            ly_unir,
            title_color='Black',
            background_color='White'
        ),
        sg.Tab(
            'Concatenar AFNs',
            ly_concatenar,
            title_color='Black',
            background_color='White'
        ),
        sg.Tab(
            'Cerradura Kleene',
            ly_kleen,
            title_color='Black',
            background_color='White'
        ),
        sg.Tab(
            'Cerradura Positiva',
            ly_positiva,
            title_color='Black',
            background_color='White'
        ),
        
        sg.Tab(
            'Mega AFN',
            ly_union_lexico,
            title_color='Black',
            background_color='White'
        ),
        sg.Tab(
            'AFN 2 AFD',
            ly_afn_a_afd,
            title_color='Black',
            background_color='White'
        ),
        sg.Tab(
            'Analizador lexico',
            ly_probar_analizador,
            title_color='Black',
            background_color='White',
            element_justification='center'
        ),
    ]],
        tab_location='topleft', title_color='Grey', tab_background_color='White', selected_title_color='Black',
        selected_background_color='White', border_width=5)]]

ly_sbgrp2 = [[
    sg.TabGroup([[
        sg.Tab(
            'LL1',
            ly_a_ll1,
            background_color='White',
        ),
    ]],
        tab_location='topleft', title_color='White', tab_background_color='White', selected_title_color='Black',
        selected_background_color='White', border_width=5)]]


ly_3er = [[]]
ly_pruebas = [[]]


layout = [[
    sg.TabGroup([[
        sg.Tab('1er Parcial',
               ly_sbgrp1,
               background_color='White',
               element_justification='center',

               ),
        sg.Tab('2ndo Parcial',
               ly_sbgrp2,
               background_color='White',
               element_justification='center',
               ),
        sg.Tab('3er Parcial',
               ly_3er,
               background_color='White',
               element_justification='center',
               ),
               
        sg.Tab('Pruebas',
               ly_3er,
               background_color='White',
               element_justification='center',
               )]
               
    ],
        tab_location='topleft', title_color='Grey', tab_background_color='White', selected_title_color='Black',
        selected_background_color='White', border_width=5)]]
