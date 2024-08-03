def convert_temperature(value, unit):
    if unit == 'C':
        return value, (value * 9/5) + 32, value + 273.15
    elif unit == 'F':
        c = (value - 32) * 5/9
        return c, value, c + 273.15
    elif unit == 'K':
        c = value - 273.15
        return c, (c * 9/5) + 32, value
    else:
        raise ValueError("Invalid unit. Use 'C', 'F', or 'K'.")

value = float(input("Enter temperature value: "))
unit = input("Enter unit (C, F, K): ").upper()

try:
    c, f, k = convert_temperature(value, unit)
    print(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
except ValueError as e:
    print(e)
