
def reverse(text_forward):
    char_list_forward = list(text_forward)
    backwards = [i for i in reversed(char_list_forward)]
    return ''.join(backwards)


def reverse_idiomatic(text_forward):
    return ''.join(reversed(text_forward))


if __name__ == "__main__":
    str_forward = "Hi, my namn is Daniel"

    print(reverse(str_forward))
    print(reverse_idiomatic(str_forward))

    print(reversed(str_forward))
    print(next(reversed(str_forward)))
    print(list(reversed(str_forward)))
    print(type(reversed(str_forward)))

    for i in str_forward:
        print(i)
