joulemeterStatements = 4 #number of statements from joulemeter
otherNanoStatements = 18 #number of statements from everything else

#declare the dictionary to store all input data
my_dict={
    'Cur' : -1,'Vlt' : -1,'Thr' : -1,'Pwr' : -1,
    'Spd' : -1,'Lng' : -1,'Lat' : -1,'Alt' : -1,'Tem' : -1,
    'GyX' : -1,'GyY' : -1,'GyZ' : -1,'AcX' : -1,'AcY' : -1,'AcZ' : -1,'MaX' : -1,'MaY' : -1,'MaZ' : -1,
    'Pit' : -1,'Rol' : -1,'Hea' : -1,'Rpm' : -1,
    }

while (True):
  for x in range (0, joulemeterStatements): #read joulemeter statements
    joulemeterInput = joulemeter.readline().decode('ascii') #read one statement
    joulemeterInputPrefix = joulemeterInput[0:3] #parse the statement for the first three characters (KEY)
    my_dict[joulemeterInputPrefix] = float(joulemeterInput[5:-2]) #assign VALUE to KEY in dictionary

  for x in range (0, otherNanoStatements): #read otherNano statements
    otherNanoInput = otherNano.readline().decode('ascii') #read one statement
    otherNanoPrefix = otherNanoInput[0:3] #parse the statement for the first three characters (KEY)
    my_dict[otherNanoPrefix] = float(otherNanoInput[5:-2]) #assign VALUE TO KEY in dictionary

