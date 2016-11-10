author = "AI research team"
import xlrd
import numpy as np

def get_cell_range(sheet, start_col, start_row, end_col, end_row):
    return [sheet.row_slice(row, start_colx=start_col, end_colx=end_col+1) for row in range(start_row, end_row+1)]

def readExcel(filename):
    wb = xlrd.open_workbook(filename)
    data = wb.sheet_by_index(0)
    data = [data.cell(i, 0).value for i in range(data.nrows)]
    return data

def normalisasi(data):
    datanorm = []
    for row in data:
            rate = np.mean([float(row) for row in data])
            stdev = np.std([float(row) for row in data])
            datanorm.append((float(row)-rate)/stdev )
    return datanorm

def generateToSeries(filename, series):
    dataPrice = readExcel(filename)
    normalizedData = normalisasi(dataPrice)
    atribut = []
    target = []
    for i in range(len(normalizedData)-series):
        atribut.append(normalizedData[i : i+series])
        target.append(normalizedData[i+series])
    return atribut, target

# print(generateToSeries('DataTrainSMA.xlsx', 3))