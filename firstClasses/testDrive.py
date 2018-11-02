from car import Car

Mercedes = Car('Mercedes', 'S Class', 'Red');

def main():
        print(Mercedes.color)
        print(Mercedes.condition)

        Mercedes.drive()
        print(Mercedes.condition)

        Mercedes.brand = "BMW"

        print(Mercedes.brand)

if __name__ == "__main__":main()
