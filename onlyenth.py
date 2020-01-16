import psychrolib

psychrolib.SetUnitSystem(psychrolib.SI)

print("")

inval = input ("Please enter the dry-bulb temperature: ")
inv = float(inval)


print("")

inval3 = input ("Please enter the humidity ratio: ")
inv3 = float(inval3)


enth = psychrolib.GetMoistAirEnthalpy(inv, inv3)
ens = str(enth)

enth2 = psychrolib.GetSatAirEnthalpy(inv, inv3)
ensb = str(enth2)

enth3 = psychrolib.GetDryAirEnthalpy(inv)
ensc = str(enth3)



print("")

print ("The moist-air enthalpy is: " + ens)

print("")

print ("The saturated-air enthalpy is: " + ensb)

print("")

print ("The dry-air enthalpy is: " + ensc)


#Specific volume is defined as the total volume of dry air and water vapor mixture per kg of dry air and water vapor (SI-units). The specific volume can be expressed as: v = V / ma + mw (11)

