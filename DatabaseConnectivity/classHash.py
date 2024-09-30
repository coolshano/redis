from redis.cluster import RedisCluster
#from DatabaseConnectivity import DBconnection
#import DBconnection

class Hashing:
    def __init__(self):
        pass

    def resturantDetails(self):
        #D = DBconnection.c.credentials
        d = 'user-session:123', mapping={
            'name': 'John',
            "surname": 'Smith',
            "company": 'Redis',
            "age": 29}


h = Hashing()
h.resturantDetails()

       



