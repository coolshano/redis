import redis
#import classHash

class ConnectDb():

    def credentials(self):
        try:
            r = redis.Redis(
            host='redis-18404.c256.us-east-1-2.ec2.redns.redis-cloud.com',
            port=18404,
            password='9WUg873qjXefEbT1eMiyZLJryuRLrWgS')
           
            r.hset(f"user:1001", "Shannon", "Smith")
            print("Data Inserted")
            
            

        except Exception as e:
            print(e)
            print("Connection failed!")
       
c = ConnectDb()
c.credentials()