import csv
import re


first_line = ['switch', 'mac', 'ip', 'vlan', 'interface']


def write_dhcp_snooping_to_csv(filenames, output):
    regex = re.compile(r'(?P<mac>\S+:\S+) +(?P<ip>\d+\.\d+\.\d+.\d+) +\S+ +\S+ +(?P<vlan>\d+) +(?P<int>\S+)')
    for filename in filenames:
        firs_row = filename[0:3]
        with open(filename, 'r') as file, open(output, 'a') as file_out:
            writer = csv.writer(file_out)
            writer.writerow(first_line)
            for line in file:
                match = regex.findall(line)
                if match:
                    for row in match:
                        row = list(row)
                        row.insert(0, firs_row)
                        writer.writerow(row)


def main():
    write_dhcp_snooping_to_csv(['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt'], 'result.csv')


if __name__ == "__main__":
    main()



