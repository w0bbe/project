import datetime
import urllib
import ephem



print "\n *** Track Sat 0.1 *** \n"

print "Downloading data"
sock = urllib.urlopen("http://www.celestrak.com/NORAD/elements/stations.txt")
htmlSource = sock.read()
sock.close()

print "Writing to file \n"
logfile = open('rawdata', 'w')
logfile.write(htmlSource)
logfile.close()

f = open('rawdata')
datarows = f.readlines()
datarows = [line.strip() for line in open('rawdata')]
f.close()


print "Information regarding : ", datarows[0]
print datarows[1]
print datarows[2]

tle_rec = ephem.readtle(datarows[0], datarows[1], datarows[2])
tle_rec.compute()

print "Position: ", tle_rec.sublong, tle_rec.sublat


print "\nAll done!"
