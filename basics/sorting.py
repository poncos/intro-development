import sys


def sort(numbers):
    sorted_numbers = [0] * len(numbers)

    for i in range(len(numbers)):
        min_index = get_minimum(numbers)
        sorted_numbers[i] = numbers.pop(min_index)

    return sorted_numbers


def get_minimum(elements):
    min_element = 0
    for index in range(len(elements)):
        if elements[index] < elements[min_element]:
            min_element = index

    return min_element


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong number of arguments: python ", sys.argv[0], " <list>")
        sys.exit(1)

    unsorted_list = [int(x) for x in sys.argv[1].split(",")]
    sorted_list = sort(unsorted_list)

    print("sorted list: ", sorted_list)
