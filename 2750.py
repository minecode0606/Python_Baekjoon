def sort_ascending(input_list):
    outputlist = []

    for _ in input_list:
        maximum = input_list[0]


if __name__ == "__main__":
    ln = []
    forloop_input = int(input(""))
    for _ in range(forloop_input):
        inputappend = int(input(""))
        ln.append(inputappend)
    output = sort_ascending(ln)
    print(output)