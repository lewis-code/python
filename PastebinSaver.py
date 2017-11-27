import requests
link = input("Input the paste bin URL, should have /raw/ EG: https://pastebin.com/raw/blahha\n")
filename = input("Input the file you'd like it to be saved to including the extension, EG: example.txt\n")

r = requests.get((link))

f = open((filename), 'w')
f.write((r.text))
f.close()
