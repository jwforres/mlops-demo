pip install selenium==4.9.1
python -c '
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Remote(
    desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
    command_executor="http://selenium.demo.svc.cluster.local:4444/wd/hub"
)
driver.get("https://llm-chat-demo-ui-stage.apps.rosa.jforrest.ruek.p3.openshiftapps.com/")
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//strong[text()=\"Response\"]"))
    )
finally:
    driver.quit()
'