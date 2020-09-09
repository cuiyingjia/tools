import os
import glob

path ='D:\\QMusic'
for infile in glob.glob(os.path.join(path, '*.flac')):
     os.remove(infile)