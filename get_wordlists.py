import urllib

download_path='http://www.unc.edu/~ncaren/haphazard/'
files=['negative.txt','positive.txt']
for filename in files:
	urllib.urlretrieve(download_path+filename, filename)
