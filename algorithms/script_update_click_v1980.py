import csv
r = csv.reader(open('./points_data.csv')) # Here your csv file
lines = list(r)

if int(lines[1][5]):
  lines[1][5]=0
  writer = csv.writer(open('./points_data.csv', 'w'))
  writer.writerows(lines)
  self.SetNeedsUpdate(True)
