## Назначение: Добавление нового бронирования

### **URL**: ```/bookings/add/ ```
### **Method**: ```POST```
### **Permissions**: ```IsAuthenticated```
### Request Body example:
```
{
    "client": 5,
    "room": 3,
    "booking_date": 25.12.2024,
    "from_town": "Moscow"
}
```

### **Code**: ```201 Created```

