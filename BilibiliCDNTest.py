import socket
import requests
import subprocess

domains = [
    "mirrorks3.bilivideo.com",
    "upos-sz-mirrorks3b.bilivideo.com",
    "upos-sz-mirrorks3c.bilivideo.com",
    "upos-sz-mirrorks32.bilivideo.com",
    "upos-sz-mirrorcos.bilivideo.com",
    "upos-sz-mirrorcosb.bilivideo.com",
    "upos-sz-mirrorbos.bilivideo.com",
    "upos-sz-mirrorhw.bilivideo.com",
    "upos-sz-mirrorhwb.bilivideo.com",
    "upos-sz-upcdnbda2.bilivideo.com",
    "upos-sz-upcdnws.bilivideo.com",
    "upos-sz-upcdnhw.bilivideo.com",
    "upos-tf-all-js.bilivideo.com",
    "cn-hk-eq-bcache-01.bilivideo.com",
    "upos-hz-mirrorakam.akamaized.net",
    "upos-sz-mirrorali.bilivideo.com",
    "upos-sz-mirroraliov.bilivideo.com",
    "upos-sz-mirror08h.bilivideo.com",
]

# IP归属地查询API
ip_api_url = "http://ip-api.com/json/"

# 函数：检查IP是否属于美国
def is_ip_in_us(ip):
    try:
        response = requests.get(ip_api_url + ip)
        data = response.json()
        return data['countryCode'] == 'US'
    except Exception as e:
        print(f"Error while checking IP: {e}")
        return False

# 函数：执行ping测试
def ping_test(ip):
    try:
        # 注意：Windows系统使用 '-n' 参数代替 '-c'
        result = subprocess.run(["ping", "-n", "3", ip], stdout=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error while pinging IP: {e}")
        return "Ping test failed."

# 主程序
for domain in domains:
    # 尝试获取IP地址
    try:
        # 获取IPv4地址
        ipv4 = socket.gethostbyname(domain)
        if is_ip_in_us(ipv4):  # 检查IPv4是否属于美国
            print(f"Domain: {domain}, IPv4: {ipv4}")
            print(ping_test(ipv4))  # 进行ping测试
        else:
            pass
            #print(f"Domain: {domain}, IPv4: {ipv4} is not in the US.")
    except socket.gaierror:
        pass
        #print(f"Domain: {domain} has no IPv4 address.")

    # 尝试获取IPv6地址
    try:
        ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
        ipv6 = ipv6_info[0][4][0]
        if is_ip_in_us(ipv6):  # 检查IPv6是否属于美国
            print(f"Domain: {domain}, IPv6: {ipv6}")
            print(ping_test(ipv6))  # 进行ping测试
        else:
            pass
            #print(f"Domain: {domain}, IPv6: {ipv6} is not in the US.")
    except socket.gaierror:
        pass
        #print(f"Domain: {domain} has no IPv6 address.")