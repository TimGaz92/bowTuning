#python based trig app for tuning bowsight 
print("--------------------------------------------------------")
print("Welcome to Tim's Bow Tuning Guide");
print("this calculator takes in same basic variables\n"
	"to determine how much you should adjust you bows sight pins")
print("--------------------------------------------------------")

distance = input("how far is your target? (meters)")
offBy = input("how far off are your shots (Centimeters, negative for low shots)")


angleA = 90
distanceConvert = float(distance) * 100
#[offBy squared] + [distanceConvert squared] = [sideCsquared]
offBySquared = float(offBy) ** 2 #still seeing offby as strng
distanceConvertSquared = float(distanceConvert) **2
sideCsquared = offBySquared + distanceConvertSquared
sideC = sideCsquared **.5
# #sideC = [squreroot sideCsquared]
# print(sideCsquared)
# print(sideC)

##use law of cosines to get the angles
CosineStpOne = distanceConvertSquared + sideCsquared
cosineStpTwo = CosineStpOne - offBySquared
divider = distanceConvert * sideC
dividerTwo = float(divider) * 2 
cosineStpThree = cosineStpTwo / dividerTwo
print("-----------------------------------------")
print ("you are off by")
print(cosineStpThree) 
print("degrees")
print("-----------------------------------------")

##find the ammount to corrrect the sight by
dropRate = float(offBy) / float(distanceConvert)
print("adjust your sight by")
print(dropRate)
print("centimeters")
print("-----------------------------------------")

# print( distance)
# print (distanceConvert)
# print (distanceConvertSquared)
# print( offBy)