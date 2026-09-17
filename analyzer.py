from collections import Counter

failed_ips = []

with open("sample.log", "r") as file:
    for line in file:
        if "FAILED" in line:
            parts = line.split()

            ip = parts[-1]
            failed_ips.append(ip)

print("Failed Login Attempts:")
print("----------------------")

for ip, count in Counter(failed_ips).items():
    print(ip, "->", count, "failed attempts")