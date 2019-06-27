from PIL import Image

# the RGB values of the colors I want to use
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

navyBlue = (0, 0, 128)
lightSteelBlue = (176, 196, 222)
dodgerBlue = (30, 144, 255)
lightCyan = (224, 255, 255)
########################################
im = Image.open("obamababy3.jpg")
im.show()
colors = im.getdata()
newobama = []
for tuples in colors:
	total = (tuples[0] + tuples[1] + tuples[2])
	if total < 182:
		newobama.append(darkBlue)
	elif total >= 182 and total < 364:
		newobama.append(red)
	elif total >= 364 and total < 546:
		newobama.append(lightBlue)
	elif total >= 546:
		newobama.append(yellow)

# newcap = im.putdata(newobama)
im.show(im.putdata(newobama))
