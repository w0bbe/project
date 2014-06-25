import datetime
import urllib
import ephem



print "\n *** Track Sat 0.1 *** \n"

print "Downloading data"
#sock = urllib.urlopen("http://www.celestrak.com/NORAD/elements/stations.txt")
#htmlSource = sock.read()
#sock.close()

print "Writing to file \n"
#logfile = open('rawdata', 'w')
#logfile.write(htmlSource)
#logfile.close()

f = open('rawdata')
datarows = f.readlines()
datarows = [line.strip() for line in open('rawdata')]
f.close()


print "Information regarding : ", datarows[0]
print datarows[1]
print datarows[2]

tle_rec = ephem.readtle(datarows[0], datarows[1], datarows[2])
tle_rec.compute()

#Transform calc. latitude 
DMSsublatS = "%s"%tle_rec.sublat
DMSsublat = DMSsublatS.split(':')
Dlat = int(DMSsublat[0])
Mlat = int(DMSsublat[1])
Slat = int(float(DMSsublat[2]))
DMSsublatsum = Dlat + Mlat/60 + Slat/3600

#longitude
DMSsublongS = "%s" %tle_rec.sublong
DMSsublong = DMSsublongS.split(':')
Dlong = int(DMSsublong[0])
Mlong = int(DMSsublong[1])
Slong = int(float(DMSsublong[2]))
DMSsublongsum = float(Dlong) + float(Mlong/60) + float(Slong/3600)


print "Position: ", tle_rec.sublong, tle_rec.sublat

print "\nDMSsublatsum: ", DMSsublatsum, DMSsublongsum

print "\nAll done!"
