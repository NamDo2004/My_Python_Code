def modulo_power(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result


base = int(input("Nhập số cơ số (base): "))
exponent = int(input("Nhập số mũ (exponent): "))
modulus = int(input("Nhập số module (modulus): "))
result = modulo_power(base, exponent, modulus)
print(f"{base}^{exponent} mod {modulus} = {result}")

