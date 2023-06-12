import configparser

config = configparser.ConfigParser()
config.read("config.txt")
password = config.get('mail','password')
