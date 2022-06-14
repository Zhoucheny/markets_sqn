import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21], [12, 22], [31, 32]],
                  columns=['a', 'b'])

df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
data = pd.read_excel('pandas_to_excel.xlsx', index_col=0) 
print(data)
