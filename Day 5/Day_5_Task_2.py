#Writing and Reading a csv file

import csv

with open('participants.csv','w') as participants_file:
    file_writer = csv.writer(participants_file, delimiter=',')

    file_writer.writerow(['Himanshu Dubey', '10 years of experience'])
    file_writer.writerow(['John', '11 years of experience'])


with open('participants.csv','r') as participants_file:
    file_reader = csv.reader(participants_file, delimiter=',')

    for row in file_reader:
        print(row)
