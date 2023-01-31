import csv

def main():
    infile = open('customers.csv', 'r')
    outfile = open('customer_country.csv', 'w+')

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        customer_name = row[1]
        customer_country = row[4]
        customer_list = [customer_name, customer_country]
        writer.writerow(customer_list)

if __name__ == "__main__":
    main()
