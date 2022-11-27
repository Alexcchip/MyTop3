from main import *

numOfIds = len(User.query.order_by(User.username).all())

for i in range(numOfIds+1):
    #print(i)
    if i > 0:
        x = User.query.filter_by(id=i).first()
        print("Username: " + x.username  +" Band: " + x.band1)
        #print(x.band1)

