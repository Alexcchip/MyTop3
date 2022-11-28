from main import *

numOfIds = len(User.query.order_by(User.username).all())
bands = dict()
for i in range(numOfIds+1):
    if i > 0:
        x = User.query.filter_by(id=i).first()
        bandList = [x.band1,x.band2,x.band3]
        bands[x.username] = bandList
print(bands)