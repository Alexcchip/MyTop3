# First solution for our matching issue 
# Issue with this: Slow

from main import *

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
        user_band = [x.band1, x.band2, x.band3]
        #print(user_band)
        bands.append(user_band)

#print(bands) 
shares = [] # find what it shares with 

for value in range(len(bands)):
    if xx == bands[value][0]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    if xx == bands[value][1]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    if xx == bands[value][2]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    
    # SET 2 (BAND2)
    if xx1 == bands[value][0]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    if xx1 == bands[value][1]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    if xx1 == bands[value][2]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)

    # SET 3 (BAND3)
    if xx2 == bands[value][0]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    if xx2 == bands[value][1]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
    if xx2 == bands[value][2]: # check for each value
        # filter by id
        id_filter = User.query.filter_by(id=value+1).first()
        shares.append(id_filter.username)
 
# the list with all users
#print(shares)

# remove duplicate users
final_list = [*set(shares)]
print(final_list) # Users who share the same values