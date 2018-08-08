import string



def infographic_cloud(clean_string):
    my_dict = {}

    max = 1

    list_to_exclude = ["and", "he", "the", "to", "is"]

    parts = [p for p in clean_string.split(" ")]
    print parts

    for i in parts:
        if i not in list_to_exclude:
            if i in my_dict:
                val = my_dict[i]
                if max < val + 1:
                    max = val+1
                my_dict[i] = val+1
            else:
                my_dict[i] = 1

    out = []
    for key,value in my_dict.items():
        if value is max:
            out.append(key)

    print out



infographic_cloud("jack and jill went to the market to buy bread and cheese cheese is jack favorite food")


