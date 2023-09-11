"""
Повторение - мать учения.
Достаньте имя из словаря
"""
super_dificult_dict = {
    1:{
        "pochti":{
        "Esche chutka":{
            ("Eto","Chto?","kortezh??"):{
                "za chto???":[[1,2,3],["1",2,(13,"oleg")]]
            }
        }
        }
    }
}

print(list(list(list(list(list(super_dificult_dict.values())[0].values())[0].values())[0].values())[0].values())[0][1][2][1])