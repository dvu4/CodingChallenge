import re, string, glob, os

def median(stream):
    return (sorted(stream)[int(round((len(stream) - 1) / 2.0))] \
            + sorted(stream)[int(round((len(stream) - 1) // 2.0))]) / 2.0

newpath = r'..\\wc_output'
if not os.path.exists(newpath): os.makedirs(newpath)

files = glob.glob('..\\wc_input\*.txt')
with open ("..\\wc_output\\result.txt","w") as outfile:
    for file1 in files:
        for line in open(file1, 'r'):
            outfile.write(line)
outfile.close()

file = open("..\\wc_output\\result.txt","r+").read()

new_file = re.sub('[^a-zA-Z0-9\n\s]', '',file).lower()

num_words = 0
stream_line=[]

f = open("..\\wc_output\\med_result.txt","w")
for line in new_file.splitlines():
    num_words = len(line.split())
    stream_line.append(num_words)
    f.write(repr(median(stream_line)))
    f.write("\n")
f.close()
 
os.remove("..\\wc_output\\result.txt")
