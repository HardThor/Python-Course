for item in range(10):
    for new_item in range(10):
        print(f"new_item is {new_item}")
        if new_item == 5:
            print("it's break inside 'new_item' cyclic")
            break
        else:
            print("it's continue inside 'new_item' cyclic")
            continue
    print(f"item is {item}")
    if item == 8:
        print("it's break inside 'item' cyclic")
        break
    else:
        print("it's continue inside 'item' cyclic")
        continue
