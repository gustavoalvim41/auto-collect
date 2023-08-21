base_url = "https://www.google.com/search"

def format_search(commerce, city):
  search_query = f"{commerce}+em+{city}"
  url = f"{base_url}?q={search_query}"
  return url
