from faker import Faker


fake = Faker()


def main():
    return f"Hello, {fake.first_name()}!"


if __name__ == "__main__":
    print(main())
