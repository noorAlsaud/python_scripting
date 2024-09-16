def mean(numbers): 
    return sum(numbers) / len(numbers)

def add_five(numbers): 
    return [n + 5 for n in numbers] 

def main(): 
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17,29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == "__main__":
    main()