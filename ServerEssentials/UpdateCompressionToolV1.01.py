# SNU Server Essentials 2019 beta
'''
Update compression tool
Description: This tool compresses SNU updates significantly. It can turn 100 Terabytes of updates into just 80 Gigabytes within the SNU 3 branch
How it works:
The way SNU is updated, a file change counts as an update. When you copy all files over and over, this amounts to a massive amount of memory.
Users who install SNU for their own servers should use a lighter tool to extract only the updates that they want.
'''
in1 = input("Reading updates... [PRESS ENTER] KEY TO FINISH]")
extractVerLisBranch3_0_0 = [] # 18 UPDATES IN THIS BRANCH
extractVerLisBranch3_0_0.append("V3.0.0.0")
extractVerLisBranch3_0_0.append("V3.0.0.1")
extractVerLisBranch3_0_0.append("V3.0.0.2")
extractVerLisBranch3_0_0.append("V3.0.0.3")
extractVerLisBranch3_0_0.append("V3.0.0.4")
extractVerLisBranch3_0_0.append("V3.0.0.5")
extractVerLisBranch3_0_0.append("V3.0.0.6")
extractVerLisBranch3_0_0.append("V3.0.0.7")
extractVerLisBranch3_0_0.append("V3.0.0.8")
extractVerLisBranch3_0_0.append("V3.0.0.9")
extractVerLisBranch3_0_0.append("V3.0.0.10")
extractVerLisBranch3_0_0.append("V3.0.0.11")
extractVerLisBranch3_0_0.append("V3.0.0.12")
extractVerLisBranch3_0_0.append("V3.0.0.13")
extractVerLisBranch3_0_0.append("V3.0.0.14")
extractVerLisBranch3_0_0.append("V3.0.0.15")
extractVerLisBranch3_0_0.append("V3.0.0.16")
extractVerLisBranch3_0_0.append("V3.0.0.17")
extractVerLisBranch3_0_1 = [] # 15 UPDATES IN THIS BRANCH
extractVerLisBranch3_0_1.append("V3.0.1.0")
extractVerLisBranch3_0_1.append("V3.0.1.1")
extractVerLisBranch3_0_1.append("V3.0.1.2")
extractVerLisBranch3_0_1.append("V3.0.1.3")
extractVerLisBranch3_0_1.append("V3.0.1.4")
extractVerLisBranch3_0_1.append("V3.0.1.5")
extractVerLisBranch3_0_1.append("V3.0.1.6")
extractVerLisBranch3_0_1.append("V3.0.1.7")
extractVerLisBranch3_0_1.append("V3.0.1.8")
extractVerLisBranch3_0_1.append("V3.0.1.9")
extractVerLisBranch3_0_1.append("V3.0.1.10")
extractVerLisBranch3_0_1.append("V3.0.1.11")
extractVerLisBranch3_0_1.append("V3.0.1.12")
extractVerLisBranch3_0_1.append("V3.0.1.13")
extractVerLisBranch3_0_1.append("V3.0.1.14")
extractVerLisBranch3_0_2 = [] # 10 UPDATES IN THIS BRANCH
extractVerLisBranch3_0_2.append("V3.0.2.0")
extractVerLisBranch3_0_2.append("V3.0.2.1")
extractVerLisBranch3_0_2.append("V3.0.2.2")
extractVerLisBranch3_0_2.append("V3.0.2.3")
extractVerLisBranch3_0_2.append("V3.0.2.4")
extractVerLisBranch3_0_2.append("V3.0.2.5")
extractVerLisBranch3_0_2.append("V3.0.2.6")
extractVerLisBranch3_0_2.append("V3.0.2.7")
extractVerLisBranch3_0_2.append("V3.0.2.8")
extractVerLisBranch3_0_2.append("V3.0.2.9")
extractVerLisBranch3_0_3 = [] # 22 UPDATES IN THIS BRANCH
extractVerLisBranch3_0_3.append("V3.0.3.0")
extractVerLisBranch3_0_3.append("V3.0.3.1")
extractVerLisBranch3_0_3.append("V3.0.3.2")
extractVerLisBranch3_0_3.append("V3.0.3.3")
extractVerLisBranch3_0_3.append("V3.0.3.4")
extractVerLisBranch3_0_3.append("V3.0.3.5")
extractVerLisBranch3_0_3.append("V3.0.3.6")
extractVerLisBranch3_0_3.append("V3.0.3.7")
extractVerLisBranch3_0_3.append("V3.0.3.8")
extractVerLisBranch3_0_3.append("V3.0.3.9")
extractVerLisBranch3_0_3.append("V3.0.3.10")
extractVerLisBranch3_0_3.append("V3.0.3.11")
extractVerLisBranch3_0_3.append("V3.0.3.12")
extractVerLisBranch3_0_3.append("V3.0.3.13")
extractVerLisBranch3_0_3.append("V3.0.3.14")
extractVerLisBranch3_0_3.append("V3.0.3.15")
extractVerLisBranch3_0_3.append("V3.0.3.16")
extractVerLisBranch3_0_3.append("V3.0.3.17")
extractVerLisBranch3_0_3.append("V3.0.3.18")
extractVerLisBranch3_0_3.append("V3.0.3.19")
extractVerLisBranch3_0_3.append("V3.0.3.20")
extractVerLisBranch3_0_3.append("V3.0.3.21")
extractVerLisBranch3_0_4 = [] # 981 UPDATES IN THIS BRANCH
extractVerLisBranch3_0_4.append("V3.0.4.0")
extractVerLisBranch3_0_4.append("V3.0.4.1")
extractVerLisBranch3_0_4.append("V3.0.4.2")
extractVerLisBranch3_0_4.append("V3.0.4.3")
extractVerLisBranch3_0_4.append("V3.0.4.4")
extractVerLisBranch3_0_4.append("V3.0.4.5")
extractVerLisBranch3_0_4.append("V3.0.4.6")
extractVerLisBranch3_0_4.append("V3.0.4.7")
extractVerLisBranch3_0_4.append("V3.0.4.8")
extractVerLisBranch3_0_4.append("V3.0.4.9")
extractVerLisBranch3_0_4.append("V3.0.4.10")
extractVerLisBranch3_0_4.append("V3.0.4.11")
extractVerLisBranch3_0_4.append("V3.0.4.12")
extractVerLisBranch3_0_4.append("V3.0.4.13")
extractVerLisBranch3_0_4.append("V3.0.4.14")
extractVerLisBranch3_0_4.append("V3.0.4.15")
extractVerLisBranch3_0_4.append("V3.0.4.16")
extractVerLisBranch3_0_4.append("V3.0.4.17")
extractVerLisBranch3_0_4.append("V3.0.4.18")
extractVerLisBranch3_0_4.append("V3.0.4.19")
extractVerLisBranch3_0_4.append("V3.0.4.20")
extractVerLisBranch3_0_4.append("V3.0.4.21")
extractVerLisBranch3_0_4.append("V3.0.4.22")
extractVerLisBranch3_0_4.append("V3.0.4.23")
extractVerLisBranch3_0_4.append("V3.0.4.24")
extractVerLisBranch3_0_4.append("V3.0.4.25")
extractVerLisBranch3_0_4.append("V3.0.4.26")
extractVerLisBranch3_0_4.append("V3.0.4.27")
extractVerLisBranch3_0_4.append("V3.0.4.28")
extractVerLisBranch3_0_4.append("V3.0.4.29")
extractVerLisBranch3_0_4.append("V3.0.4.30")
extractVerLisBranch3_0_4.append("V3.0.4.31")
extractVerLisBranch3_0_4.append("V3.0.4.32")
extractVerLisBranch3_0_4.append("V3.0.4.33")
extractVerLisBranch3_0_4.append("V3.0.4.34")
extractVerLisBranch3_0_4.append("V3.0.4.35")
extractVerLisBranch3_0_4.append("V3.0.4.36")
extractVerLisBranch3_0_4.append("V3.0.4.37")
extractVerLisBranch3_0_4.append("V3.0.4.38")
extractVerLisBranch3_0_4.append("V3.0.4.39")
extractVerLisBranch3_0_4.append("V3.0.4.40")
extractVerLisBranch3_0_4.append("V3.0.4.41")
extractVerLisBranch3_0_4.append("V3.0.4.42")
extractVerLisBranch3_0_4.append("V3.0.4.43")
extractVerLisBranch3_0_4.append("V3.0.4.44")
extractVerLisBranch3_0_4.append("V3.0.4.45")
extractVerLisBranch3_0_4.append("V3.0.4.46")
extractVerLisBranch3_0_4.append("V3.0.4.47")
extractVerLisBranch3_0_4.append("V3.0.4.48")
extractVerLisBranch3_0_4.append("V3.0.4.49")
extractVerLisBranch3_0_4.append("V3.0.4.50")
extractVerLisBranch3_0_4.append("V3.0.4.51")
extractVerLisBranch3_0_4.append("V3.0.4.52")
extractVerLisBranch3_0_4.append("V3.0.4.53")
extractVerLisBranch3_0_4.append("V3.0.4.54")
extractVerLisBranch3_0_4.append("V3.0.4.55")
extractVerLisBranch3_0_4.append("V3.0.4.56")
extractVerLisBranch3_0_4.append("V3.0.4.57")
extractVerLisBranch3_0_4.append("V3.0.4.58")
extractVerLisBranch3_0_4.append("V3.0.4.59")
extractVerLisBranch3_0_4.append("V3.0.4.60")
extractVerLisBranch3_0_4.append("V3.0.4.61")
extractVerLisBranch3_0_4.append("V3.0.4.62")
extractVerLisBranch3_0_4.append("V3.0.4.63")
extractVerLisBranch3_0_4.append("V3.0.4.64")
extractVerLisBranch3_0_4.append("V3.0.4.65")
extractVerLisBranch3_0_4.append("V3.0.4.66")
extractVerLisBranch3_0_4.append("V3.0.4.67")
extractVerLisBranch3_0_4.append("V3.0.4.68")
extractVerLisBranch3_0_4.append("V3.0.4.69")
extractVerLisBranch3_0_4.append("V3.0.4.70")
extractVerLisBranch3_0_4.append("V3.0.4.71")
extractVerLisBranch3_0_4.append("V3.0.4.72")
extractVerLisBranch3_0_4.append("V3.0.4.73")
extractVerLisBranch3_0_4.append("V3.0.4.74")
extractVerLisBranch3_0_4.append("V3.0.4.75")
extractVerLisBranch3_0_4.append("V3.0.4.76")
extractVerLisBranch3_0_4.append("V3.0.4.77")
extractVerLisBranch3_0_4.append("V3.0.4.78")
extractVerLisBranch3_0_4.append("V3.0.4.79")
extractVerLisBranch3_0_4.append("V3.0.4.80")
extractVerLisBranch3_0_4.append("V3.0.4.81")
extractVerLisBranch3_0_4.append("V3.0.4.82")
extractVerLisBranch3_0_4.append("V3.0.4.83")
extractVerLisBranch3_0_4.append("V3.0.4.84")
extractVerLisBranch3_0_4.append("V3.0.4.85")
extractVerLisBranch3_0_4.append("V3.0.4.86")
extractVerLisBranch3_0_4.append("V3.0.4.87")
extractVerLisBranch3_0_4.append("V3.0.4.88")
extractVerLisBranch3_0_4.append("V3.0.4.89")
extractVerLisBranch3_0_4.append("V3.0.4.90")
extractVerLisBranch3_0_4.append("V3.0.4.91")
extractVerLisBranch3_0_4.append("V3.0.4.92")
extractVerLisBranch3_0_4.append("V3.0.4.93")
extractVerLisBranch3_0_4.append("V3.0.4.94")
extractVerLisBranch3_0_4.append("V3.0.4.95")
extractVerLisBranch3_0_4.append("V3.0.4.96")
extractVerLisBranch3_0_4.append("V3.0.4.97")
extractVerLisBranch3_0_4.append("V3.0.4.98")
extractVerLisBranch3_0_4.append("V3.0.4.99")
extractVerLisBranch3_0_4.append("V3.0.4.100")
extractVerLisBranch3_0_4.append("V3.0.4.101")
extractVerLisBranch3_0_4.append("V3.0.4.102")
extractVerLisBranch3_0_4.append("V3.0.4.103")
extractVerLisBranch3_0_4.append("V3.0.4.104")
extractVerLisBranch3_0_4.append("V3.0.4.105")
extractVerLisBranch3_0_4.append("V3.0.4.106")
extractVerLisBranch3_0_4.append("V3.0.4.107")
extractVerLisBranch3_0_4.append("V3.0.4.108")
extractVerLisBranch3_0_4.append("V3.0.4.109")
extractVerLisBranch3_0_4.append("V3.0.4.110")
extractVerLisBranch3_0_4.append("V3.0.4.111")
extractVerLisBranch3_0_4.append("V3.0.4.112")
extractVerLisBranch3_0_4.append("V3.0.4.113")
extractVerLisBranch3_0_4.append("V3.0.4.114")
extractVerLisBranch3_0_4.append("V3.0.4.115")
extractVerLisBranch3_0_4.append("V3.0.4.116")
extractVerLisBranch3_0_4.append("V3.0.4.117")
extractVerLisBranch3_0_4.append("V3.0.4.118")
extractVerLisBranch3_0_4.append("V3.0.4.119")
extractVerLisBranch3_0_4.append("V3.0.4.120")
extractVerLisBranch3_0_4.append("V3.0.4.121")
extractVerLisBranch3_0_4.append("V3.0.4.122")
extractVerLisBranch3_0_4.append("V3.0.4.123")
extractVerLisBranch3_0_4.append("V3.0.4.124")
extractVerLisBranch3_0_4.append("V3.0.4.125")
extractVerLisBranch3_0_4.append("V3.0.4.126")
extractVerLisBranch3_0_4.append("V3.0.4.127")
extractVerLisBranch3_0_4.append("V3.0.4.128")
extractVerLisBranch3_0_4.append("V3.0.4.129")
extractVerLisBranch3_0_4.append("V3.0.4.130")
extractVerLisBranch3_0_4.append("V3.0.4.131")
extractVerLisBranch3_0_4.append("V3.0.4.132")
extractVerLisBranch3_0_4.append("V3.0.4.133")
extractVerLisBranch3_0_5 = [] # [COMING SOON] UPDATES IN THIS BRANCH
extractVerLisBranch3_0_5.append("V3.0.5.0")
extractVerLisBranch3_0_5.append("V3.0.5.1")
extractVerLisBranch3_0_5.append("V3.0.5.2")
extractVerLisBranch3_0_5.append("V3.0.5.3")
extractVerLisBranch3_0_5.append("V3.0.5.4")
extractVerLisBranch3_0_5.append("V3.0.5.5")
extractVerLisBranch3_0_5.append("V3.0.5.6")
extractVerLisBranch3_0_5.append("V3.0.5.7")
extractVerLisBranch3_0_5.append("V3.0.5.8")
extractVerLisBranch3_0_5.append("V3.0.5.9")
extractVerLisBranch3_0_5.append("V3.0.5.10")
extractVerLisBranch3_0_6 = [] # [COMING SOON] UPDATES IN THIS BRANCH
extractVerLisBranch3_0_6.append("V3.0.6.0")
extractVerLisBranch3_0_6.append("V3.0.6.1")
print ("SNU Update compression tool")
print ("What version branch do you want to compress/extract?")
print ("3.0.0 [ID: 30] 3.0.1 [ID: 31] 3.0.2 [ID: 32] 3.0.3 [ID: 33] 3.0.4 [ID: 34] 3.0.5 [ID: 35] 3.0.6 [ID: 36]")
branch1 = str(input("ID choice:"))
if (branch1 == "30"):
	print ("You have selected the SNU 3.0.0.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_0)))
	# Action line: Extract Ver, compress Ver
if (branch1 == "31"):
	print ("You have selected the SNU 3.0.1.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_1)))
	# Action line: Extract Ver, compress Ver
if (branch1 == "32"):
	print ("You have selected the SNU 3.0.2.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_2)))
	# Action line: Extract Ver, compress Ver
if (branch1 == "33"):
	print ("You have selected the SNU 3.0.3.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_3)))
	# Action line: Extract Ver, compress Ver
if (branch1 == "34"):
	print ("You have selected the SNU 3.0.4.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_4)))
	# Action line: Extract Ver, compress Ver
if (branch1 == "35"):
	print ("You have selected the SNU 3.0.5.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_6)))
	# Action line: Extract Ver, compress Ver
if (branch1 == "36"):
	print ("You have selected the SNU 3.0.6.x branch")
	vcountEnt = input("Press [ENTER] key to view all versions")
	print('[%s]' % ', '.join(map(str, extractVerLisBranch3_0_6)))
	# Action line: Extract Ver, compress Ver
print ("Extraction complete!")
entQ = input("Press [ENTER] key to close the update compression tool")