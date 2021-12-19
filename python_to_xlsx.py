import xlsxwriter
from requests import get
from re import findall

headers = {'User-Agent': 'Mozilla/5.0'}
output = {}
row_x = 1
row_y = 1
column = 1

for y in range(0, 12):
    bruh = [[], []]
    for m in range(1, 13):
        m = str(m).zfill(2)

        for d in range(1, 29):
            d = str(d).zfill(2)

            for i in findall("(\d+\ \:\ \d+)", str(get(f"https://www.championat.com/stat/basketball/#{2010 + y}-{m}-{d}", headers=headers).content)):
                bruh[0].append(i.split(" : ")[0])
                bruh[1].append(i.split(" : ")[1])
                print(f'Year: {2010+y}  Month: {m}  Day: {d}')

    output[2010+y] = bruh
 
workbook = xlsxwriter.Workbook('Output.xlsx')
worksheet = workbook.add_worksheet()

for i in output.keys():
    print(i)
    worksheet.write(row_x, column+2, str(i))
    for x in output[i][0]:
        worksheet.write(row_x, column, x)
        row_x += 1

    for y in output[i][1]:
        worksheet.write(row_y, column+1, y)
        row_y += 1

workbook.close()
        



