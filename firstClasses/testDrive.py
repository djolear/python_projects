from car import Car


def main():
        Mercedes = Car('Mercedes', 'S Class', 'Red');

        print(Mercedes.color)
        print(Mercedes.condition)

        Mercedes.drive()
        print(Mercedes.condition)

        Mercedes.brand = "BMW"

        print(Mercedes.brand)

if __name__ == "__main__":main()
