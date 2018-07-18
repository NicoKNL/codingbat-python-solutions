def cat_dog(str):
    cat_count = 0
    dog_count = 0
    i = 0
    while i < len(str) - 2:
        sub = str[i:i + 3]
        if sub == "cat":
            cat_count += 1
        elif sub == "dog":
            dog_count += 1
        i += 1

    return cat_count == dog_count
