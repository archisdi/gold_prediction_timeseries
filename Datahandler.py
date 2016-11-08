author = "AI research team"
import xlrd

def get_cell_range(sheet, start_col, start_row, end_col, end_row):
    return [sheet.row_slice(row, start_colx=start_col, end_colx=end_col+1) for row in range(start_row, end_row+1)]

def readExcel(filename):
    wb = xlrd.open_workbook(filename)
    data = wb.sheet_by_index(0)
    data = [data.cell(i, 0).value for i in range(data.nrows)]
    return data

def generateToSeries(filename, series):
    dataPrice = readExcel(filename)

    atribut = []
    target = []

    for i in range(len(dataPrice)-series):
        atribut.append(dataPrice[i : i+series])
        target.append(dataPrice[i+series])
    return atribut, target

# print(generateToSeries('DataTrainSMA.xlsx', 3))