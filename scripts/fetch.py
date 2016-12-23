import os
import urllib
import hashlib
import zipfile

def md5_of_file(filename):
    with open(filename, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

url = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"
expected_md5 = "c4d9eecfca2ab87c1945afe126590906"
file_path = "data/raw/ml-1m.zip"

if not os.path.isfile(file_path) or md5_of_file(file_path) != expected_md5:
    urllib.urlretrieve(url, file_path)
    print ("Downloaded from {0} at {1}.".format(url, file_path))

else:
    print ("File already downloaded at {0}.".format(file_path))


data_path = "data/raw"
with zipfile.ZipFile(file_path) as f:
    f.extractall(data_path)

print ("Extracted data.")
