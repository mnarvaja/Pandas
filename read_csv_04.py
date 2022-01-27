from argparse import ArgumentParser
import xlrd

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="read FILE and print tab names", metavar="FILE")
parser.add_argument("-s", "--sheet", dest="sheet",
                    help="read FILE and print tab names", metavar="SHEET")
args = parser.parse_args()
# print(args.filename)
# print(args.sheet)

if args.filename != None:
    xls = xlrd.open_workbook(args.filename, on_demand=True)
    if args.sheet not in xls.sheet_names():
        print("%s not in the sheet names" % args.sheet)
        quit()
    # remeber: xlrd sheet_names is a function, not a property
    for file in xls.sheet_names():
        print(file)
