import csv
 
class ReadAndWriteData:
    def __init__(self, filename):
        self.filename = filename
    def read_data(self):
        data = csv.reader(self.filename)
        return data
 
if __name__ == "__main__":
    excel_filepath = 'C:/Users/Z00530863/Music/ReadnData.xlsx'
    data_handler = ReadAndWriteData(excel_filepath)
    data = data_handler.read_data()
    print(data)