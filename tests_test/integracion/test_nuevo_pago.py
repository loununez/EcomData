from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import uuid


def test_creacion_pago(driver):
    wait = WebDriverWait(driver, 10)

    # --- 1. Login ---
    driver.get("http://127.0.0.1:5000/auth/")

    driver.find_element(By.NAME, "usuario").send_keys("admin@ecomdata.com")
    driver.find_element(By.NAME, "contrasena").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_contains("/panel"))

    # --- 2. Ir a Pagos ---
    driver.get("http://127.0.0.1:5000/pagos/")
    
    
    # --- 3. Ir a Nuevo Pago ---
    boton_nuevo_pago = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "boton-procesar-pago"))
    )
    boton_nuevo_pago.click()
    
    
    # 🔍 DEBUG: VER HTML REAL DE LA PANTALLA
    print("\n======= HTML DESPUÉS DE HACER CLIC EN NUEVO PAGO =======\n")
    print(driver.page_source)
    print("\n==========================================================\n")

    # --- 4. Completar formulario para crear un nuevo pago ---
    
    # Seleccionar venta (primer elemento del select)
    select_venta = Select(wait.until(
    EC.presence_of_element_located((By.ID, "ventaId"))
    ))
    select_venta.select_by_index(1)

    # Obtener el monto real autocompletado por el JS
    selected_option = select_venta.options[1]
    monto_real = selected_option.get_attribute("data-total")
    
    # Esperar a que el input se auto-complete
    monto_input = wait.until(EC.presence_of_element_located((By.ID, "monto")))
    time.sleep(0.5)  # breve pausa para dejar que el JS actualice
    assert monto_input.get_attribute("value") == monto_real
    

    # Método de pago
    metodo = Select(driver.find_element(By.ID, "metodoPago"))
    metodo.select_by_visible_text("Efectivo")

    # Enviar formulario
    boton_guardar = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    boton_guardar.click()

    # --- 5. Volver a la lista de pagos ---
    wait.until(EC.url_contains("/pagos"))


    time.sleep(1)  # deja cargar tabla


    # --- 6. Verificar que el pago aparece ---
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert monto_real in body_text