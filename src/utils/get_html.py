from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_html(browser):
  WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#rl_ist0 > div > div.rl_tile-group > div.rlfl__tls.rl_tls")))
  element = browser.find_element(By.CSS_SELECTOR, "#rl_ist0 > div > div.rl_tile-group > div.rlfl__tls.rl_tls")
  html = element.get_attribute("innerHTML")
  return html
