def konversi_celsius_ke_fahrenheit(suhu_celsius):
    suhu_fahrenheit = (suhu_celsius * 9/5) + 32
    return suhu_fahrenheit

def main():
    suhu_celsius = float(input("Masukkan Suhu Dalam Derajat Celsius: "))
    suhu_fahrenheit = konversi_celsius_ke_fahrenheit(suhu_celsius)
    print("Derajat Fahrenheit:", suhu_fahrenheit)

if __name__ == "__main__":
    main()