def convert(fuel_str):
    try:
        x, y = fuel_str.split("/")
        new_x = int(x)
        new_y = int(y)
        if new_x > new_y:
            raise ValueError("X cannot be greater than Y")
        if new_y == 0:
            raise ZeroDivisionError("Y cannot be zero")
        percentage = round(new_x / new_y * 100)
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        return percentage
    except ValueError as ve:
        raise ValueError(f"Invalid input: {fuel_str}. {str(ve)}")
    except ZeroDivisionError as zde:
        raise ZeroDivisionError(f"Invalid input: {fuel_str}. {str(zde)}")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    while True:
        fuel_str = input("Fraction: ")
        try:
            percentage = convert(fuel_str)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError) as e:
            print(str(e))


if __name__ == "__main__":
    main()
