import urllib

print "Downloading data"
sock = urllib.urlopen("http://www.celestrak.com/NORAD/elements/stations.txt")
htmlSource = sock.read()
sock.close()

print "Writing to file"
logfile = open('rawdata', 'w')
logfile.write(htmlSource)
logfile.close()

print "All done!"
