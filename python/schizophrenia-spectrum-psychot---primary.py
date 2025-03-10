# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"Eu32300","system":"readv2"},{"code":"Eu32A00","system":"readv2"},{"code":"286..11","system":"readv2"},{"code":"Eu23200","system":"readv2"},{"code":"Eu23212","system":"readv2"},{"code":"Eu23.00","system":"readv2"},{"code":"Eu21.14","system":"readv2"},{"code":"Eu23300","system":"readv2"},{"code":"Eu23000","system":"readv2"},{"code":"Eu32313","system":"readv2"},{"code":"E130.11","system":"readv2"},{"code":"Eu33311","system":"readv2"},{"code":"285..11","system":"readv2"},{"code":"Eu33313","system":"readv2"},{"code":"Eu23100","system":"readv2"},{"code":"Eu20y13","system":"readv2"},{"code":"Eu33315","system":"readv2"},{"code":"Eu32311","system":"readv2"},{"code":"Eu33300","system":"readv2"},{"code":"Eu2y.00","system":"readv2"},{"code":"E13z.11","system":"readv2"},{"code":"Eu23y00","system":"readv2"},{"code":"Eu23z00","system":"readv2"},{"code":"Eu32900","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('schizophrenia-spectrum-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["schizophrenia-spectrum-psychot---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["schizophrenia-spectrum-psychot---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["schizophrenia-spectrum-psychot---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
