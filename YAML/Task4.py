"""
Достаньте имя из словаря
"""

task = {
    "kluch1":[
        {"info1": "not name"},
        {
            "info2":{"still not name": "not name",
                     ("not name","oleg","another name"):"that what we need"
                     }
        }
    ]
}

print(list(list(list(task.values())[0][1].values())[0])[1][1])