import socket, time

# Test primary Telegram IPs as used by python-telegram-bot
ips = ["149.154.167.220", "149.154.167.221", "149.154.167.222", "149.154.167.188", "149.154.166.110", "149.154.166.111", "149.154.166.112"]
print("Testing core Telegram IPs...")
for ip in ips:
    try:
        sock = socket.create_connection((ip, 443), timeout=5)
        sock.close()
        print(f"  {ip}: OK")
    except Exception as e:
        print(f"  {ip}: {e}")
print("Done")
