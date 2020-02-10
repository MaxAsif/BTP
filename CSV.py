
class CSV:
    file = ''
    def __init__(self,f):
        self.file = f    
    
    def generate_csv(self):
        input_file = open("raw_data/"+self.file, 'r')
        filename = self.file
        filename = filename.replace(".","_")
        output_file = open("csv/"+filename+".csv", 'w')
        input_file.readline() # skip first line 
        input_file.readline()
        input_file.readline()
        input_file.readline()
        input_file.readline()
        lst = ['Trial','chan','Time','Voltage']
        output_file.write(','.join([lst[0], lst[1], lst[2], lst[3]]) + '\n')
        for line in input_file:
            lst = line.strip().split(' ')
            output_file.write(','.join([lst[0], lst[1], lst[2], lst[3]]) + '\n')
        input_file.close()
        output_file.close()