import pandas as pd

def create_spreadsheet(date):
  df = pd.DataFrame(date)
  excel_filename = "result.xlsx"
  df.to_excel(excel_filename, index=False)
  print(f"\nPlanilha {excel_filename} foi criada com sucesso!")
