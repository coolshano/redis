#What is Redis
Redis (Remote Dictionary Server) is an open-source, in-memory data structure store, used as a database, cache, message broker, and queue. It is known for its speed, efficiency, and support for various data structures. Redis can handle large amounts of data while providing fast access times, making it ideal for performance-critical applications.

#This example will cover inserting data and retreving data using samples with Python

#The following data types will be covered.

1/ Hash

In Redis, a hash is a data structure that stores a collection of field-value pairs, similar to a dictionary or a map in programming languages. Each hash is identified by a key, and within the hash, you can store and retrieve multiple fields and their corresponding values.

Inserting data
HSET hashKey field value

HSET user:1000 name "John"
HSET user:1000 age "30"

Retreving data
HGET hashKey field

HGET user:1000 name


2/ List 

To be updated

3/ Set

To be updated
