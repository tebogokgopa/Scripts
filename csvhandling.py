import csv
new_lines = []

def read_csv_file(csv_file_name):
    
    

with open('numbers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ';')
    for row in csv_reader:
        lines = list([row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[29],row[30]])
        new_lines.append(lines)
    print(new_lines)
    


with open('newNumbers.csv','w') as write_file:
    csv_writer = csv.writer(write_file)
    for row in newLines:
        csv_writer.writerow(row)
    
    write_file.close()

print("Done")
csv_file.close()
