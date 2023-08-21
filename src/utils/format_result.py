from bs4 import BeautifulSoup

def format_result(html):
  soup = BeautifulSoup(html, "html.parser")
  details = []
  for item in soup.select(".rllt__details"):
    name = item.find("span", class_="OSrXXb").get_text().strip()
    address_with_number = item.find_all("div")[2].get_text().strip()
    parts = address_with_number.split("·")
    if len(parts) >= 2:
      address = parts[0].strip()
      contact = parts[1].strip()
    else:
      address = address_with_number
      contact = "Não Informado" 
    details.append({
      "nome": name,
      "endereço": address,
      "contato": contact
    })
  return details
