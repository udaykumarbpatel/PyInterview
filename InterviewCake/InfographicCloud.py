import string

def infographic_cloud(input_string):
    my_dict = {}
    clean_string = input_string.translate(None, string.punctuation).lower()

    parts = [p for p in clean_string.split(" ")]
    print parts
    for i in parts:
        if i in my_dict:
            val = my_dict[i]
            my_dict[i] = val+1
        else:
            my_dict[i] = 1

    for key in my_dict:
        print key + "=" + str(my_dict[key])



infographic_cloud("'After beating the eggs, Dana read the next step:' 'Add milk and eggs, then add flour and sugar.'")


