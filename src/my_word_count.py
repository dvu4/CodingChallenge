import re, glob, os

newpath = r'..\\wc_output'
if not os.path.exists(newpath): os.makedirs(newpath)

files = sorted(glob.glob('..\\wc_input\*.txt'))
with open ("..\\wc_output\\result.txt","w") as outfile:
    for f in files:
        with open(f,"r") as infile:
            outfile.write(infile.read())
        outfile.write("\n")            
outfile.close()

file = open("..\\wc_output\\result.txt","r+").read()
new_file = re.sub('[^a-zA-Z0-9\n\s]', '',file).lower()


word_dict={}

for word in new_file.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
    
f = open("..\\wc_output\\wc_output.txt","w")

for key in sorted(word_dict):
        f.write(key)
        f.write(' ')
        f.write(repr(word_dict[key]))
        f.write("\n")
f.close()

os.remove("..\\wc_output\\result.txt")
