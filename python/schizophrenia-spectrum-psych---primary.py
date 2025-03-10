# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"E13yz00","system":"readv2"},{"code":"E14..00","system":"readv2"},{"code":"Eu02z12","system":"readv2"},{"code":"E130.00","system":"readv2"},{"code":"Eu0z.12","system":"readv2"},{"code":"E13..11","system":"readv2"},{"code":"Eu2z.00","system":"readv2"},{"code":"146H.00","system":"readv2"},{"code":"Eu2z.11","system":"readv2"},{"code":"Eu2y.11","system":"readv2"},{"code":"E1z..00","system":"readv2"},{"code":"E13z.00","system":"readv2"},{"code":"E1y..00","system":"readv2"},{"code":"Eu23z12","system":"readv2"},{"code":"E13..00","system":"readv2"},{"code":"E13y.00","system":"readv2"},{"code":"E1...00","system":"readv2"},{"code":"Eu84314","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('schizophrenia-spectrum-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["schizophrenia-spectrum-psych---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["schizophrenia-spectrum-psych---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["schizophrenia-spectrum-psych---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
