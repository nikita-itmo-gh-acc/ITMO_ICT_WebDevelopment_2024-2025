## Назначение: получить список юзеров, которые проживали в данном номере за период времени

### **URL**: ```/rooms/{id}/users/{from}/{to}/ ```
### **Method**: ```GET```
### **Permissions**: ```IsAdminUser```

## Success Response:
### **Code**: ```200 OK```
### Content example (request URL ```/rooms/2/users/2022-04-04/2024-10-10/```):
```
[
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
        "email": "admin@admim.con",
        "firstname": "admin",
        "lastname": "admin",
        "phone": "",
        "bookings": [
            5
        ]
    },
    {
        "email": "just@man.ru",
        "firstname": "Test",
        "lastname": "Djoser",
        "phone": "89116469049",
        "bookings": [
            6
        ]
    }
]
```