import urllib.request, json, socket, ssl

# Test 1: DNS
print("=== DNS Test ===")
try:
    ips = socket.getaddrinfo("api.telegram.org", 443)
    for ip in ips[:3]:
        print(f"  {ip[4][0]}")
except Exception as e:
    print(f"  DNS FAILED: {e}")

# Test 2: HTTPS Connection
print("\n=== HTTPS Test ===")
try:
    ctx = ssl.create_default_context()
    with socket.create_connection(("api.telegram.org", 443), timeout=10) as sock:
        with ctx.wrap_socket(sock, server_hostname="api.telegram.org") as ssock:
            print(f"  Connected to {ssock.version()}")
            print(f"  Cipher: {ssock.cipher()}")
except Exception as e:
    print(f"  FAILED: {e}")

# Test 3: HTTP Request (without auth)
print("\n=== HTTP Request Test ===")
try:
    req = urllib.request.Request("https://api.telegram.org/bot", method="GET")
    with urllib.request.urlopen(req, timeout=10) as r:
        print(f"  Status: {r.status}")
        print(f"  Body: {r.read().decode()[:200]}")
except Exception as e:
    print(f"  FAILED: {e}")

print("\n=== Done ===")
