import sys
import csv

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    sampling = sys.argv[3]

    data = []
    with open(infile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        axis = next(reader)
        data.append(axis)

        counter = 0
        for row in reader:
            counter+=1
            if counter == int(sampling):
                data.append(row)
                counter = 0

    with open(outfile, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for row in data:
            writer.writerow(row)