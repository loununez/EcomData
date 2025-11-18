from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import uuid
import time


def test_creacion_usuario_completa(driver):
    wait = WebDriverWait(driver, 10)

    # --- Login ---
    driver.get("http://127.0.0.1:5000/auth/")

    driver.find_element(By.NAME, "usuario").send_keys("admin@ecomdata.com")
    driver.find_element(By.NAME, "contrasena").send_keys("admin123")  
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_contains("/panel"))

    # Ir a usuarios
    driver.get("http://127.0.0.1:5000/usuarios/")

    # Clic en botón Agregar Usuario 
    boton_agregar = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "boton-agregar-usuario"))
    )
    boton_agregar.click()

    # Esperar redirección a la página de agregar usuario
    wait.until(EC.url_contains("/usuarios_agregar"))

    # Completar formulario 
    driver.find_element(By.NAME, "nombre").send_keys("Test Usuario Selenium1")
    
    email = f"selenium_user_{uuid.uuid4().hex[:6]}@example.com"
    driver.find_element(By.NAME, "email").send_keys(email)

    driver.find_element(By.NAME, "password").send_keys("test1234")

    select_rol = driver.find_element(By.NAME, "rol")
    select_rol.send_keys("Analista")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Luego de guardar debe volver a /usuarios/
    wait.until(EC.url_contains("/usuarios"))

    # Verificar que el usuario aparece 
    wait.until(EC.text_to_be_present_in_element(
        (By.TAG_NAME, "body"),
        email
    ))
    
  