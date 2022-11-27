from main import *

numOfIds = len(User.query.order_by(User.username).all())

for i in range(numOfIds+1):
    x = User.query.filter_by(id=i).first()
    print(x)