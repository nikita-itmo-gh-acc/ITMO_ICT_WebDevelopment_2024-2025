## Назначение: получить список юзеров, которые прибыли из определенного города

### **URL**: ```/users/{from_town}/ ```
### **Method**: ```GET```
### **Permissions**: ```IsAuthenticated```

## Success Response:
### **Code**: ```200 OK```
### Content example (request URL ```/users/SPB/```):
```
    [
    {
        "email": "game.azog@gmail.com",
        "firstname": "Nikita",
        "lastname": "Ananiev",
        "phone": "89116469049",
        "bookings": [
            3,
            7
        ]
    },
    {
        "email": "user@test.com",
        "firstname": "test",
        "lastname": "user",
        "phone": "+7999999999",
        "bookings": [
            4
        ]
    },
    {
        "email": "game.azog@gmail.com",
        "firstname": "Nikita",
        "lastname": "Ananiev",
        "phone": "89116469049",
        "bookings": [
            3,
            7
        ]
    }
]
```