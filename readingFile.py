import configparser
config = configparser.ConfigParser()

#config.read('config.ini')
source_file = config.read( 'demofile.txt')
destination_file = config.read( 'demofile1.txt')

#f = open("demofile.txt", "r")
#print(f.read())