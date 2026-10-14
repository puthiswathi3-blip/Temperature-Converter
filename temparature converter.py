
# Temperature Converter
# Converts temperatures between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature(value, source, target):
    # Convert the input temperature to Celsius first
    if source == "C":
        celsius = value
    elif source == "F":
        celsius = fahrenheit_to_celsius(value)
    else:
        celsius = kelvin_to_celsius(value)

    # Convert Celsius to the required temperature unit
    if target == "C":
        return celsius
    elif target == "F":
        return celsius_to_fahrenheit(celsius)
    else:
        return celsius_to_kelvin(celsius)


def main():
    print("=" * 40)
    print("       TEMPERATURE CONVERTER")
    print("=" * 40)

    print("Available units:")
    print("C - Celsius")
    print("F - Fahrenheit")
    print("K - Kelvin")

    try:
        temperature = float(input("\nEnter temperature: "))

        source = input("Convert from (C/F/K): ").strip().upper()
        target = input("Convert to (C/F/K): ").strip().upper()

        # Validate temperature units
        if source not in ("C", "F", "K") or target not in ("C", "F", "K"):
            print("Invalid unit! Please enter C, F, or K.")
            return

        # Validate physically meaningful temperatures
        if source == "K" and temperature < 0:
            print("Error: Kelvin temperature cannot be below 0 K.")
            return

        if source == "C" and temperature < -273.15:
            print("Error: Celsius temperature cannot be below -273.15 C.")
            return

        if source == "F" and temperature < -459.67:
            print("Error: Fahrenheit temperature cannot be below -459.67 F.")
            return

        result = convert_temperature(temperature, source, target)

        unit_names = {
            "C": "Celsius",
            "F": "Fahrenheit",
            "K": "Kelvin"
        }

        print("\n" + "-" * 40)
        print(f"Input:  {temperature:.2f} {source}")
        print(f"Output: {result:.2f} {target}")
        print(f"Result: {temperature:.2f} degrees "
              f"{unit_names[source]} = {result:.2f} "
              f"degrees {unit_names[target]}")
        print("-" * 40)

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
