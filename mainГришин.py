import csv
from collections import defaultdict
from datetime import datetime


class FileRecord:
    def __init__(self, name, size, file_type, creation_date, modification_date, access_level):
        self.name = name
        self.size = int(size) 
        self.file_type = file_type

        self.creation_date = datetime.strptime(creation_date, '%d.%m.%Y')
        self.modification_date = datetime.strptime(modification_date, '%d.%m.%Y')
        self.access_level = access_level

def read_file_records(filename):
    records = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 6:
                record = FileRecord(*row)
                records.append(record)
    return records

def count_files_by_type(records):
    count = defaultdict(int)
    for record in records:
        count[record.file_type] += 1
    return count

def largest_files(records, top_n=10):
    sorted_files = sorted(records, key=lambda x: (x.size, x.name), reverse=True)
    return sorted_files[:top_n]

def restricted_presentations_2012(records):
    presentations = [record for record in records if record.file_type == 'презентация' and record.access_level == 'ограниченный' and record.modification_date.year == 2012]
    return sorted(presentations, key=lambda x: x.name)

def large_videos_2011(records):
    videos = [record for record in records if record.file_type == 'видео' and record.size > 100 * 1024 and record.creation_date.year == 2011 and record.creation_date.month > 6]
    return sorted(videos, key=lambda x: x.size, reverse=True)

def main():
    records = read_file_records('files.csv')
    

    file_counts = count_files_by_type(records)
    print("Количество файлов каждого типа:")
    for file_type, count in file_counts.items():
        print(f"{file_type}: {count}")


    largest_files_list = largest_files(records)
    print("\n10 самых больших файлов:")
    for file in largest_files_list:
        print(f"{file.name}: {file.size} Кбайт")


    restricted_presentations_list = restricted_presentations_2012(records)
    print("\nПрезентации ограниченного доступа, измененные в 2012 году:")
    for file in restricted_presentations_list:
        print(file.name)


    large_videos_list = large_videos_2011(records)
    print("\nВидео размером больше 100 Мбайт, созданные во второй половине 2011 года:")
    for file in large_videos_list:
        print(f"{file.name}: {file.size} Кбайт")

if __name__ == "__main__":
    main()
