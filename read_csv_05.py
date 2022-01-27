from argparse import ArgumentParser
import xlrd
import pandas as pd

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="read FILE and print tab names", metavar="FILE")
parser.add_argument("-s", "--sheet", dest="sheet",
                    help="read FILE and print tab names", metavar="SHEET")
args = parser.parse_args()

data = pd.read_excel(args.filename, sheet_name = args.sheet)
df = pd.DataFrame(data, columns = ['Name','User ID', 'Date', 'TimeIn', 'TimeOut'])

for i in df.index:
    name_str = df['Name'][i]
    user_id  = df['User ID'][i]
    date_str = str(df['Date'][i])[0:10]
    time_in  = str(df['TimeIn'][i])[0:5]
    time_out = str(df['TimeOut'][i])[0:5]
    print("%s,%s,%s %s,,,2," % (name_str, user_id, date_str, time_in))
    print("%s,%s,%s %s,,,2," % (name_str, user_id, date_str, time_out))
