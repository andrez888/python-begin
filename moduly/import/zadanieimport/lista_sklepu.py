students = [
    {
        "name": "Jakub",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "fizyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "historia",
                "grades": [2, 3, 5, 1, 3, 5]
            }
        ]
    },
    {
        "name": "Mikołaj",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "fizyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "historia",
                "grades": [2, 1, 1, 1, 2, 1]
            }
        ]
    }
]
sklep = [
    {'name':'chleb',
     'opis':
         {'cena': 3.30,
          'ilosc': 120}},
     {'name': 'piwo',
      'opis':{
          'cena':2.50,
          'ilosc': 500
      }}
]
# print(sklep)
# print(students)
# for item in sklep:
#     print(item["opis"]["cena"])
# for student in students:
#      print(student["subjects_results"][0]["subject"])
# shop = sklep[0]['opisy']
# print(shop)
for x in sklep:
    print(x)