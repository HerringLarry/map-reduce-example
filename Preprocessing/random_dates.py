import csv
import random
from datetime import datetime

def select_date(num):
    if num == 1:
        return "2015-12-1"
    elif num == 2:
        return "2015-12-2"
    elif num == 3:
        return "2015-12-3"
    elif num == 4:
        return "2015-12-4"
    elif num == 5:
        return "2015-12-5"
    elif num == 6:
        return "2015-12-6"
    elif num == 7:
        return "2015-12-7"
    elif num == 8:
        return "2015-12-8"
    elif num == 9:
        return "2015-12-9"
    elif num == 10:
        return "2015-12-10"

def return_random(num):
    random.seed(datetime.now())
    return random.randint(1,num)

def replace_dates(file_name, new_file_name):
    with open(file_name, 'r') as f:
        file_reader = csv.reader(f)
        with open(new_file_name, 'w') as w:
            file_writer = csv.writer(w)
            file_writer.writerow(file_reader.next())
            for line in file_reader:
                line[3] = select_date(return_random(10))
                file_writer.writerow(line)

def main():
    file_name = "From100G.csv"
    file_name_new = "FromNew.csv"
    replace_dates(file_name,file_name_new)

if __name__ == "__main__":
    main()


