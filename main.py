import re
import sys


def find_certs(text):
    match = re.findall(r"-----BEGIN[\-\w\d\n\s=+/]*END CERTIFICATE-----", text)
    certs_num = len(match)
    print("Found {0} certificates!".format(certs_num))
    extract_certs(match, certs_num)


def extract_certs(match, certs_num):
    for i in range(certs_num):
        original_stdout = sys.stdout
        filename = "cert_"+str(i)
        with open(filename, 'w') as o:
            sys.stdout = o
            print(match[i])
            sys.stdout = original_stdout
            print("{0} was created.".format(filename))


if __name__ == '__main__':
    input_file = sys.argv[1]
    f = open(input_file, "r")
    find_certs(f.read())
