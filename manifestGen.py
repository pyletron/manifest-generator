import os
import time
import json

print("Pyletron Manifest Generator")
print("By ItsIceCreeperPE Dev")
print("https://github.com/pyletron/manifest-generator")
name = input('What is the application name?\nApplication Name: ')
os.system('cls')
console = input('Do you want your application to have an open console window\nDefault : No\nOptions: Y/N\nSelection: ')
os.system('cls')
onedir = input('Do you want your application to be a single executable or a folder.\nNote: Single executable may take a little more time to launch\nOptions: Y/N\nSelection: ')
os.system('cls')
icon = input('Input the directory to your icon file\nMUST BE .ico FILE\nFile Path: ')
os.system('cls')
version = input('What is your application version?\nApplication Version: ')
os.system('cls')
if console=="Y" or console=="y":
	console=True
elif console=="N" or console=="n":
	console=False
else:
	quit()
if onedir=="Y" or onedir=="y":
	onedir=True
elif onedir=="N" or onedir=="n":
	onedir=False
else:
	quit()

manifestDictionary = {
	"name" : name,
	"console" : console,
	"onedir" : onedir,
	"icon" : icon,
	"version" : version
}

jsonFile = json.dumps(manifestDictionary, indent=4)

with open('manifest.json', 'w') as outfile:
	outfile.write(jsonFile)

print("File Generated!")
print("File located in same directory as this file.")
print("Closing in 5 seconds")
time.sleep(5)