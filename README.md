# Redis Powered DNS Server in Python

Simple DNS server with Redis as the backend. Redis records are stored according to the FQDN (with trailing dot) as the key, and a JSON payload as the value.

#Json Payload:
```
{
      "key": "www.google.com.",  
      "ttl": 400,
      "a": ["172.217.31.196", "216.239.38.10"]
}
```

# Usage 

Initialize redis db for the first time <br>
```$python3 init_redis.py```

Terminal 1 : start server <br>
```$sudo python3 dns.py```

Terminal 2 : send dns request <br>
```$dig www.google.co.in @127.0.0.1```

# Output 
```
; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.google.co.in @127.0.0.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63518
;; flags: qr aa; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;www.google.co.in.		IN	A

;; ANSWER SECTION:
www.google.co.in.	400	IN	A	172.217.31.196
www.google.co.in.	400	IN	A	216.239.38.10

;; Query time: 2 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Sat Apr 28 18:24:26 IST 2018
;; MSG SIZE  rcvd: 66
```

