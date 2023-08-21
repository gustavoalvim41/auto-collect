from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser(url):
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  browser = webdriver.Chrome(options=options)
  browser.get(url)
  element_a = browser.find_element(By.CSS_SELECTOR, "#Odp5De > div > div > div.ixix9e > div.VT5Tde > div.kuydt > div.iNTie > g-more-link > a")
  element_a.click()
  return browser
