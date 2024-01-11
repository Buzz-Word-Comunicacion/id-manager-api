#Importación de librerías
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import sys

from .db import insert_scrap_data


def obtenerDriver():
    #Definición del driver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    return driver

def abrirTribulal(driver,cedulaCR):
    try:
        #Abrir el sitio del tribunal supremo de Costa Rica
        driver.get('https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx')

        #Colocar el número de cédula y dar click en la busqueda
        cedula_input = driver.find_element(By.ID,'txtcedula')
        cedula_input.send_keys(cedulaCR)
        consultar_boton = driver.find_element(By.ID, 'btnConsultaCedula')
        consultar_boton.click()
        time.sleep(1)
        return 1
    except:
        interrupcion = {"error": "Fallo al cargar el sitio del tribunal"}
        json_data = json.dumps(interrupcion)
        return 0
    
def abrirDetalle(driver):
    try:
        #Click para ver el detalle de la cédula
        detalles_boton = driver.find_element(By.ID, 'LinkButton11')
        detalles_boton.click()
        time.sleep(1)
        return 1
    except:
        interrupcion = {"error": "Fallo al cargar el detalle de la cedula"}
        json_data = json.dumps(interrupcion)
        return 0
    
def obtenerDetalle(driver):
    try:
        #Obtener los datos del detalle
        label_cedula = driver.find_element(By.ID, 'lblcedula')
        Cedula =label_cedula.text

        label_nombre= driver.find_element(By.ID, 'lblnombre')
        Nombre = label_nombre.text

        label_primerapellido = driver.find_element(By.ID, 'lblprimer_apellido')
        PrimerApellido = label_primerapellido.text

        label_segundoapellido = driver.find_element(By.ID, 'lblsegundo_apellido')
        SegundoApellido = label_segundoapellido.text

        label_conocidocomo = driver.find_element(By.ID, 'lblconocido_como')
        ConocidoComo = label_conocidocomo.text

        label_fechanacimiento = driver.find_element(By.ID, 'lblfecha_nacimiento')
        FechaNacimiento = label_fechanacimiento.text

        label_lugarnacimiento = driver.find_element(By.ID, 'lbllugar_nacimiento')
        LugarNacimiento = label_lugarnacimiento.text

        label_nacionalidad = driver.find_element(By.ID, 'lblnacionalidad')
        Nacionalidad = label_nacionalidad.text

        label_padre = driver.find_element(By.ID, 'lblnombre_padre')
        NombrePadre = label_padre.text

        label_idpadre = driver.find_element(By.ID, 'lblid_padre')
        IdPadre = label_idpadre.text

        label_madre = driver.find_element(By.ID, 'lblnombre_madre')
        NombreMadre = label_madre.text

        label_idmadre = driver.find_element(By.ID, 'lblid_madre')
        IdMadre = label_idmadre.text

        label_empadronado = driver.find_element(By.ID, 'lblempadronado')
        Empadronado = label_empadronado.text

        label_fallecido = driver.find_element(By.ID, 'lblfallecido')
        Fallecido = label_fallecido.text

        label_marginal = driver.find_element(By.ID, 'lblLeyendaMarginal')
        Marginal = label_marginal.text
        
        datos = {
            "cedula": Cedula,
            "nombre": Nombre,
            "primerApellido": PrimerApellido,
            "segundoApellido": SegundoApellido,
            "conocidoComo": ConocidoComo,
            "fechaNacimiento": FechaNacimiento,
            "lugarNacimiento": LugarNacimiento,
            "nacionalidad": Nacionalidad,
            "nombrePadre": NombrePadre,
            "idPadre": IdPadre,
            "nombreMadre": NombreMadre,
            "idMadre": IdMadre,
            "empadronado": Empadronado,
            "fallecido": Fallecido,
            "marginal": Marginal  
        }
        insert_scrap_data(datos)
        return datos

    except:
        interrupcion = {"error": "Fallo al obtener los datos del detalle"}
        json_data = json.dumps(interrupcion)
        return 0
    
def scrapingCR(cedulaCR):
    driver = obtenerDriver()
    abrirTribulal(driver,cedulaCR)
    abrirDetalle(driver)
    return obtenerDetalle(driver)