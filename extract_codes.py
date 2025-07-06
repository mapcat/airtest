import csv

iata_codes = set()

with open('airports.csv', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=';')
    next(reader)  # Skip header
    for row in reader:
        if row[1]:  # Ensure IATA code exists
            iata_codes.add(row[1].strip())

sorted_codes = sorted(iata_codes)

with open('airports-master.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    for code in sorted_codes:
        writer.writerow([code])
