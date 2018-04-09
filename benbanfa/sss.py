
gathering =float(raw_input("Please enter your\
 price query discount."))

if  2 < gathering <= 10:
	print "10% per cent off."
	print "In the long term, we provide you \
	with a discount, the new price after\
	discount is as follows.$",(gathering-gathering*0.1)
elif gathering > 10:
	print "20% per cent off."
	print "In the long term, we provide you \
	with a discount, the new price after\
	discount is as follows.$",(gathering-gathering*0.2)
else:
    print "la ji qiong gui!!!!!!"
