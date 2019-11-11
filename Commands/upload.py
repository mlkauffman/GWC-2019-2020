import urllib3
import sys

with open(sys.argv[1], 'rb') as fp:
    file_data = fp.read()

http = urllib3.PoolManager()

r = http.request(
    'POST',
    sys.argv[2],
    fields={
        'file': (sys.argv[1], file_data),
        'Name': sys.argv[3]
    }
)

print(str(r.data))
