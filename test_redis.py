import redis

# Kết nối đến Redis (mặc định localhost:6379)
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set dữ liệu vào Redis
client.set('my_key', 'Hello, Redis!')

# Get dữ liệu từ Redis
value = client.get('my_key')

# Hiển thị kết quả
print(value.decode())  # Output: Hello, Redis!
