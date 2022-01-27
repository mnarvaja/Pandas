import pandas as pd

filename = '/home/pi/Code/Pandas/Import_Yard.xls'

data = pd.read_excel(filename, sheet_name = 'Sheet1')
df = pd.DataFrame(data, columns = ['Name','User ID', 'Date', 'TimeIn', 'TimeOut'])

for i in df.index:
    name_str = df['Name'][i]
    user_id  = df['User ID'][i]
    date_str = str(df['Date'][i])[0:10]
    time_in  = str(df['TimeIn'][i])[0:5]
    time_out = str(df['TimeOut'][i])[0:5]
    print("%s,%s,%s %s,,,2," % (name_str, user_id, date_str, time_in))
    print("%s,%s,%s %s,,,2," % (name_str, user_id, date_str, time_out))
