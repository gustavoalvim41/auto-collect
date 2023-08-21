from utils.format_search import format_search
from utils.open_browser import open_browser
from utils.get_html import get_html
from utils.format_result import format_result
from utils.create_spreadsheet import create_spreadsheet

def main():
  commerce = input("\nDigite o tipo de comércio desejado (Ex: Loja de Roupas): ")
  city = input("Digite o nome da cidade (Ex: Florianópolis): ")
  if commerce and city:
    url = format_search(commerce, city)
    if url:
      browser = open_browser(url)
      html = get_html(browser)
      results = format_result(html)
      create_spreadsheet(results)
      browser.quit()
    else:
      print("\nA url não existe, o script será encerrando.")
  else:
    print("\nNenhum campo pode ser vazio, o script será encerrando.")

if __name__ == "__main__":
  main()
