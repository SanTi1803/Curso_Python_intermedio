def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"fristname": "Santiago", "lastname": "Morales" }

    super_list = [
        {"fristname": "Santiago", "lastname": "Morales" },
        {"fristname": "Franco", "lastname": "Morales" },
        {"fristname": "Facundo", "lastname": "Pineda" },
        {"fristname": "Rocio", "lastname": "Mallorca" }
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.4, 4.5, 5.7]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

   # for i in super_list:
    #    print(i["fristname"], "-", i["lastname"])

if __name__ == "__main__":
    run()