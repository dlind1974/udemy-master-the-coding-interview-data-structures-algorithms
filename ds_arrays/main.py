if __name__ == "__main__":
    cars = ["Ford", "Volvo", "BMW"]
    print(cars[2])
    print(len(cars))

    for car in cars:
        print(car)

    print("Modifying cars...")

    cars.append("Maserati")
    cars.append("Ferrari")
    cars.remove("Ford")

    popped = cars.pop(1)
    print("popped: ", popped)

    for i in range(len(cars)):
        print(cars[i])

    translato = [car + "lito" for car in cars]
    print(translato)

    translato.sort()
    print(translato)

    my_list = [2, 3, 4]
    number_to_add = 1

    # Using insert method
    my_list.insert(0, number_to_add)

    print(my_list)
    print(my_list[:0])

    my_list = [3, 4, 5]
    numbers_to_add = [1, 2]

    # Preparing the list to be added at the beginning
    my_list[:0] = numbers_to_add

    print(my_list)

    my_list[:0] = [2777]
    print(my_list)

    # Splicing (foga ihop, skarva)
    my_list = [1, 2, 3, 4, 5]
    my_list[1:4] = [9, 8]  # Replace elements at indices 1 and 2
    print(my_list)  # Output: [1, 9, 8, 4, 5]




