import streamlit as st 
import pandas as pd 
import pyautogui as py
import time
from aux_pyautogui_fun import reduzir


## OBSERVE O MÊS DE MAIO, SEMANA 1, AO INVES DE PEGAR AS IMAGENS COM OS NOMES DO MÊS, PEGUEI APENAS O BOTÃO DE SELEÇÃO DA PAGINA (ao lado de adcionar pagína),
# DEIXANDO APENAS 1 FOTO FIXA (evitando erros), E DIRECIONANDO AO DIRETORIO APENAS COM O COMANDO SETA PARA BAIXO E 'ENTER' NO LOCAL SELECIONADO.


# ATUALIZADO DIA 06/05
# UTILIZANDO FUNÇÃO JÁ QUE PARTE DO TRABALHO E REPETITIVO

st.set_page_config(
                   page_title='CEM_DRIVER',
                   layout='wide')

py2 = st.file_uploader('Select seu arquivo',type='csv')
''
if py2 is not None:
    
    st.subheader('MÊS DE :red[ABRIL]')
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        but_M4S1 = st.button('M4S1', type='primary')

    with col2:
        but_M4S2 = st.button('M4S2',type='primary')

    with col3:
        but_M4S3 = st.button('M4S3',type='primary')

    with col4:
        but_M4S4 = st.button('M4S4', type='primary')

    ### MÊS 4 SEMANA 1 -> NOVO
    ###################################################
    if but_M4S1:
         
            reduzir()

            proc_nome = py.locateCenterOnScreen('proc_nome.png')
            py.click(proc_nome.x, proc_nome.y)

            py.press('down')

            py.PAUSE = 0.5

            df = pd.read_csv(py2,header=None, sep=(',')).drop(0).drop(columns=0)
            df = df.rename(columns={1:'Nome', 2:'Horas', 3:'Motivo'})
            # Transforma número para string.    
            #df['Horas'] = df['Horas'].astype(str)

            for lin in df.index:
                name = df.loc[lin,'Nome']
                py.write(name)
                py.press('down')

            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            
            for lin in df.index:
                horas = df.loc[lin,'Horas']
                py.write(horas)
                py.press('down')


            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            py.press('tab')

            for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                py.write(motivo)
                py.press('down')
    

    #####################################################
    if but_M4S2:

            reduzir()


            mes = py.locateCenterOnScreen('select_mês.png')
            py.click(mes.x, mes.y)
            py.press('down')
            py.press('enter')

            proc_nome = py.locateCenterOnScreen('proc_nome.png')
            py.click(proc_nome.x, proc_nome.y)

            py.press('down')

            py.PAUSE = 0.5

            df = pd.read_csv(py2,header=None, sep=(',')).drop(0).drop(columns=0)
            df = df.rename(columns={1:'Nome', 2:'Horas', 3:'Motivo'})
            # Transforma número para string.    
            #df['Horas'] = df['Horas'].astype(str)

            for lin in df.index:
                name = df.loc[lin,'Nome']
                py.write(name)
                py.press('down')

            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            
            for lin in df.index:
                horas = df.loc[lin,'Horas']
                py.write(horas)
                py.press('down')


            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            py.press('tab')

            for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                py.write(motivo)
                py.press('down')

###################################################################################################################
    if but_M4S3:
        
            reduzir()


            mes = py.locateCenterOnScreen('select_mês.png')
            py.click(mes.x, mes.y)
            py.press('down')
            py.press('down')
            py.press('enter')

            proc_nome = py.locateCenterOnScreen('proc_nome.png')
            py.click(proc_nome.x, proc_nome.y)

            py.press('down')

            py.PAUSE = 0.5

            df = pd.read_csv(py2,header=None, sep=(',')).drop(0).drop(columns=0)
            df = df.rename(columns={1:'Nome', 2:'Horas', 3:'Motivo'})
            # Transforma número para string.    
            #df['Horas'] = df['Horas'].astype(str)

            for lin in df.index:
                name = df.loc[lin,'Nome']
                py.write(name)
                py.press('down')

            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            
            for lin in df.index:
                horas = df.loc[lin,'Horas']
                py.write(horas)
                py.press('down')


            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            py.press('tab')

            for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                py.write(motivo)
                py.press('down')

######################################################################

    if but_M4S4:
            
            reduzir()


            mes = py.locateCenterOnScreen('select_mês.png')
            py.click(mes.x, mes.y)
            py.press('down')
            py.press('down')
            py.press('down')
            py.press('enter')

            proc_nome = py.locateCenterOnScreen('proc_nome.png')
            py.click(proc_nome.x, proc_nome.y)

            py.press('down')

            py.PAUSE = 0.5

            df = pd.read_csv(py2,header=None, sep=(',')).drop(0).drop(columns=0)
            df = df.rename(columns={1:'Nome', 2:'Horas', 3:'Motivo'})
            # Transforma número para string.    
            #df['Horas'] = df['Horas'].astype(str)

            for lin in df.index:
                name = df.loc[lin,'Nome']
                py.write(name)
                py.press('down')

            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            
            for lin in df.index:
                horas = df.loc[lin,'Horas']
                py.write(horas)
                py.press('down')


            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            py.press('tab')

            for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                py.write(motivo)
                py.press('down')

## M  Ê  S    D  E    M  A  I  O
    st.subheader('MÊS DE :blue[MAIO]')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        but_M5S1 = st.button('M5-S1', type='primary')

    with col2:
        but_M5S2 = st.button('M5-S2', type='primary')


    ##### M Ê S      D  E      M  A  I  O

    if but_M5S1:
            
            reduzir()


            mes = py.locateCenterOnScreen('select_mês.png')
            py.click(mes.x, mes.y)
            py.press('down')
            py.press('down')
            py.press('down')
            py.press('down')
            py.press('enter')

            proc_nome = py.locateCenterOnScreen('proc_nome.png')
            py.click(proc_nome.x, proc_nome.y)

            py.press('down')

            py.PAUSE = 0.5

            df = pd.read_csv(py2,header=None, sep=(',')).drop(0).drop(columns=0)
            df = df.rename(columns={1:'Nome', 2:'Horas', 3:'Motivo'})
            # Transforma número para string.    
            #df['Horas'] = df['Horas'].astype(str)

            for lin in df.index:
                name = df.loc[lin,'Nome']
                py.write(name)
                py.press('down')

            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            
            for lin in df.index:
                horas = df.loc[lin,'Horas']
                py.write(horas)
                py.press('down')


            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            py.press('tab')

            for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                py.write(motivo)
                py.press('down')

#########################################################################################################
    if but_M5S2:
            
            reduzir()


            mes = py.locateCenterOnScreen('select_mês.png')
            py.click(mes.x, mes.y)
            py.press('down')
            py.press('down')
            py.press('down')
            py.press('down')
            py.press('down')
            py.press('enter')

            proc_nome = py.locateCenterOnScreen('proc_nome.png')
            py.click(proc_nome.x, proc_nome.y)

            py.press('down')

            py.PAUSE = 0.5

            df = pd.read_csv(py2,header=None, sep=(',')).drop(0).drop(columns=0)
            df = df.rename(columns={1:'Nome', 2:'Horas', 3:'Motivo'})
            # Transforma número para string.    
            #df['Horas'] = df['Horas'].astype(str)

            for lin in df.index:
                name = df.loc[lin,'Nome']
                py.write(name)
                py.press('down')

            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            
            for lin in df.index:
                horas = df.loc[lin,'Horas']
                py.write(horas)
                py.press('down')


            py.click(proc_nome.x, proc_nome.y)
            py.press('down')
            py.press('tab')
            py.press('tab')

            for lin in df.index:
                motivo = df.loc[lin,'Motivo']
                py.write(motivo)
                py.press('down')