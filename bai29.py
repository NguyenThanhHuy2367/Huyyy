n = int(input("Nhập các số N nguyên dương = "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Tổng các chữ số của là", s)