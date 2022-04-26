drzewo_gnelaogiczne = {
    'imię': 'Andrzej',
    'nazwisko': 'Piontkowski',
    'dob' : '19.01.1988',
    'parents' :
        [
            {'imię': 'Zofia',
             'nazwisko': 'Moczyńska',
             'dob' : '04.07.1953',
             'parents' : [] },
            {'imie' : 'Bogdan',
             'naziwsko' : 'Piontkowski',
             'dob' : '26.03.1954',
             'parents' : []}

    ]

}
my_family = {
    "first_name": "Mikołaj",
    "last_name": "Lewandowski",
    "birth_date": "23-11-1991",
    "parents": [
        {
            "first_name": "Jan",
            "last_name": "Lewandowski",
            "birth_date": "15-11-1961",
            "parents": [
                {
                    "first_name": "Piotr",
                    "last_name": "Lewandowski",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
                {
                    "first_name": "Beata",
                    "last_name": "Lewandowska",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
            ]
        },
        {
            "first_name": "Alicja",
            "last_name": "Lewandowski",
            "birth_date": "15-11-1961",
            "parents": [
                {
                    "first_name": "Paweł",
                    "last_name": "Kowalski",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
                {
                    "first_name": "Anna",
                    "last_name": "Kowalska",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
            ]

        }
    ],
}
print(drzewo_gnelaogiczne)