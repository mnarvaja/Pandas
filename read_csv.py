import pandas as pd

# filename = '/home/pi/Code/Pandas/Import_Yard.xlsx'
filename = '/home/pi/Code/Pandas/Import_Yard.xls'

# df = pd.read_excel(filename, sheet_name = 1, index_col = 0)
df = pd.read_excel(filename)

print(df)

