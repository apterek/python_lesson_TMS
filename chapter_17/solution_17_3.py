import re


def parse_sh_cdp_neighbors(file_in_one_row):
    res_dict = {}
    new_dict = {}
    regex = r'(R\S) +(\S+ \d+\/\d+) +\S+ + \S+ \S+ \S+ +\S+ + (\S+ \d+\/\d+)'
    name = list(re.search(r'(\S+)>', file_in_one_row).groups())[0]
    result = [match.groups() for match in re.finditer(regex, file_in_one_row)]
    for line_list in result:
        new_dict[line_list[1]] = {line_list[0]: line_list[2]}
    res_dict[name] = new_dict
    return res_dict


def main():
    with open('sh_cdp_n_sw1.txt') as file:
        print(parse_sh_cdp_neighbors(file.read()))


if __name__ == "__main__":
    main()
