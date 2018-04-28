import redis, json


if __name__ == '__main__':
	r_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
	r_conn = redis.Redis(connection_pool=r_pool)
	
	with open('data.txt') as filedata:
		
		data = json.load(filedata)
		
		key = data['key']
		value = json.dumps(data)

		print (r_conn.set(key,value))
		