from main import *
# working on solution 2
numOfIds = len(User.query.order_by(User.username).all())
bands = []
xx = 'asf'
xx1 = 'Elvis'
xx2 = 'Rolling Stones'
for i in range(numOfIds+1): # number of IDS
    #print(i)
    if i > 0:
        x = User.query.filter_by(id=i).first()
        #print("Username: " + x.username  +" Band: " + x.band1)
        #print(x.band1)
        user_band = [x.band1, x.band2, x.band3] # create a list and each index has 3 values 
        #print(user_band)
        bands.append(user_band)

shares = []

# THIS SOLUTION SEEMS FASTER
#for value in range(len(bands)):, optimized
for value in range(len(bands)):
    if xx in bands[value] or xx1 in bands[value] or xx2 in bands[value]: # check if the value got by the user is in the list 
        id_filter = User.query.filter_by(id=value+1).first() # get their id by doing value+1
        shares.append(id_filter.username)

print(shares)