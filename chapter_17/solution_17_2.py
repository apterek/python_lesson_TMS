import re
import csv
import glob


def parse_sh_version(file_in_one_line):
    regex = r'\), Version (\S+),.+' \
            r'router uptime is (\d+ \S+ \d+ \S+ \d+ \S+).+' \
            r'System image file is "(\S+)"'
    match = re.search(regex, file_in_one_line, re.DOTALL)
    if match:
        return match.groups()


def write_inventory_to_csv(data_filename, csv_filename):
    for filename in data_filename:
        device_name = list(re.search(r'(r\d).', filename).groups())[0]
        with open(filename, 'r') as file_in, open(csv_filename, 'a') as file_out:
            row = list(parse_sh_version(file_in.read()))
            row.insert(0, device_name)
            writer = csv.writer(file_out)
            writer.writerow(headers)
            writer.writerow(row)


def main():
    sh_version_files = glob.glob("sh_version*")
    write_inventory_to_csv(sh_version_files, 'routers_inventory.csv')


if __name__ == '__main__':
    headers = ["hostname", "ios", "uptime",  "image"]
    main()
