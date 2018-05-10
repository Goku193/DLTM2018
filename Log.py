import re
import sys
wartosci = []

print "Podaj formule: "
form = raw_input()
print "Formula: " + str(form)


sprawdz = bool(re.search('[^NKACE]+',form))
if sprawdz is True:
	print 'Zla formula'
#	sys.exit()

zmienne = re.findall('[a-z]', form)
print zmienne
zmien = sorted(list(set(zmienne)))
print 'Wykrylem ' + str(len(zmien)) + ' zmienne.'
print 'Sa to: ' + str(zmien) + '. Podaj kolejno wartosci (0,1) zatwierdzajac enterem.'

for p in zmien:
	wart = raw_input()
	if wart == '1':
		wartosci.append(True)
	if wart == '0':
		wartosci.append(False)
	print p + ': ' + wart
print wartosci
