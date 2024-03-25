import csv

def dollars_to_hryvnias(dollars):
    return round(dollars * conversion_rate)

conversion_rate = 28

with open('test_file.csv', mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

for row in data[1:]:
    for i in range(1, len(row)):
        dollars = int(row[i])
        hryvnias = dollars_to_hryvnias(dollars)
        row[i] = hryvnias

with open('converted_test_file.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

