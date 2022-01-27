import pandas as pd

filename = '/home/pi/Code/Pandas/Import_Yard.xls'

data = pd.read_excel(filename, sheet_name = 'Sheet1')
df = pd.DataFrame(data, columns = ['Name','User ID', 'Date', 'TimeIn', 'TimeOut'])

for i in df.index:
    print('{0}{1:10d} {2} {3} {4}'.format(df['Name'][i].ljust(20,'.'), 
                            df['User ID'][i], 
                            str(df['Date'][i])[0:10], 
                            str(df['TimeIn'][i])[0:5], 
                            str(df['TimeOut'][i])[0:5]))
