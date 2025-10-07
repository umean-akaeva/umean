try:
    num = input("Введіть число: ")

    num = int(num)

    print("Ви ввели число:", num)

except ValueError:

    print("Помилка! Це не можна перетворити в ціле число.")
