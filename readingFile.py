import configparser



parser = configparser.ConfigParser()
sourcefile=parser.read('file1.ini')
destinationfile=parser.read('file2.ini')
#config.read('config.ini')
#source_file = config.read( 'demofile.txt')
#destination_file = config.read( 'demofile1.txt')

#f = open("demofile.txt", "r")
#print(f.read())