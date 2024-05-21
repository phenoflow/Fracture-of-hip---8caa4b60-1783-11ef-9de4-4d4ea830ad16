# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"14G7.00","system":"readv2"},{"code":"S30..11","system":"readv2"},{"code":"34351.0","system":"readv2"},{"code":"38489.0","system":"readv2"},{"code":"34078.0","system":"readv2"},{"code":"24587.0","system":"readv2"},{"code":"73981.0","system":"readv2"},{"code":"39984.0","system":"readv2"},{"code":"73234.0","system":"readv2"},{"code":"5301.0","system":"readv2"},{"code":"67394.0","system":"readv2"},{"code":"96644.0","system":"readv2"},{"code":"60885.0","system":"readv2"},{"code":"8243.0","system":"readv2"},{"code":"28965.0","system":"readv2"},{"code":"51216.0","system":"readv2"},{"code":"38878.0","system":"readv2"},{"code":"38054.0","system":"readv2"},{"code":"52194.0","system":"readv2"},{"code":"68668.0","system":"readv2"},{"code":"51861.0","system":"readv2"},{"code":"73210.0","system":"readv2"},{"code":"36599.0","system":"readv2"},{"code":"45779.0","system":"readv2"},{"code":"51999.0","system":"readv2"},{"code":"58642.0","system":"readv2"},{"code":"61733.0","system":"readv2"},{"code":"8648.0","system":"readv2"},{"code":"101567.0","system":"readv2"},{"code":"67633.0","system":"readv2"},{"code":"33957.0","system":"readv2"},{"code":"45141.0","system":"readv2"},{"code":"17019.0","system":"readv2"},{"code":"68229.0","system":"readv2"},{"code":"89434.0","system":"readv2"},{"code":"24276.0","system":"readv2"},{"code":"29145.0","system":"readv2"},{"code":"18273.0","system":"readv2"},{"code":"23803.0","system":"readv2"},{"code":"96518.0","system":"readv2"},{"code":"50727.0","system":"readv2"},{"code":"62966.0","system":"readv2"},{"code":"36391.0","system":"readv2"},{"code":"71282.0","system":"readv2"},{"code":"44735.0","system":"readv2"},{"code":"39396.0","system":"readv2"},{"code":"97971.0","system":"readv2"},{"code":"58720.0","system":"readv2"},{"code":"72138.0","system":"readv2"},{"code":"49209.0","system":"readv2"},{"code":"40267.0","system":"readv2"},{"code":"2225.0","system":"readv2"},{"code":"69919.0","system":"readv2"},{"code":"70479.0","system":"readv2"},{"code":"19387.0","system":"readv2"},{"code":"48337.0","system":"readv2"},{"code":"19117.0","system":"readv2"},{"code":"93374.0","system":"readv2"},{"code":"1994.0","system":"readv2"},{"code":"65690.0","system":"readv2"},{"code":"10570.0","system":"readv2"},{"code":"100771.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fracture-of-hip-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hip---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hip---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hip---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
