## История бронирований пользователя:
### Шаблон компоненты:
```html
    <Base/>
    <DeleteBooking ref="del"/>
    <UpdateBooking ref="upt"/>
    <div v-if="this.user" class="booking__history__container">
    <h1>История бронирований</h1>
    <table class="booking__table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Номер</th>
                <th>Дата бронирования</th>
                <th>Статус</th>
                <th>Оплата</th>
                <th>Действия</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="booking in bookings" :key="booking.id">
                <td>{{ booking.id }}</td>
                <td>{{ booking.room }}</td>
                <td>{{ booking.booking_date }}</td>
                <td>{{ booking.state }}</td>
                <td>{{ booking.payment_status }}</td>
                <td v-if="booking.state != 'finished'">
                    <a class="action__button delete__button" @click="showModalDelete(booking.id)">удалить</a> 
                    <a class="action__button edit__button" @click="showModalUpdate(booking.id)">редактировать</a> 
                </td>
                <td v-if="booking.state == 'finished'"> нельзя внести изменения </td>
            </tr>
        </tbody>
    </table>
    </div>
```
### В данной компоненте также используются 3 дочерние компоненты: Base( для шапки), DeleteBooking и UpdateBooking (для открытия модальных окон с соответствующими CRUD операциями)

### Скрипт компоненты:
```javascript
    import Base from '@/components/Base.vue';
    import DeleteBooking from '@/components/DeleteBooking.vue';
    import UpdateBooking from '@/components/UpdateBooking.vue';
    import axios from 'axios';

    export default {
        name: 'BookingList',
        components: {
            Base, DeleteBooking, UpdateBooking
        },
        data() {
            return {
                bookings: [],
                user: {}
            }
        },
        methods: {
            showModalDelete: function (id) {
                this.$refs.del.show = true
                this.$refs.del.bookingId = id
            },
            showModalUpdate: function (id) {
                this.$refs.upt.show = true
                this.$refs.upt.bookingId = id
            },
            async fetchUserBookings () {
                this.user = JSON.parse(localStorage.getItem('user'));
                try {
                    const response = await axios.get(`http://127.0.0.1:8000/users/${this.user.id}/`);
                    this.bookings = response.data.bookings;
                    this.bookings.forEach(async (booking) => {
                        const room_resp = await axios.get(`http://127.0.0.1:8000/rooms/${booking.room}/`);
                        booking.room = room_resp.data.number;
                    });
                    console.log(this.bookings);
                } catch (e) {
                    if (e.response) {
                        switch (e.response.status) {
                            case 401:
                                this.user = {};
                                break;
                            default:
                        }
                    }
                }
            }
        }, 
        mounted() {
            this.fetchUserBookings()
        }
    }
```

## Внешний вид истории бронирований
![alt text](https://raw.githubusercontent.com/nikita-itmo-gh-acc/ITMO_ICT_WebDevelopment_2024-2025/refs/heads/main/students/K3340/laboratory_works/Ananiev_Nikita/site/assets/images/book_history.jpg)

## Можем отредактировать даты
![alt text](https://raw.githubusercontent.com/nikita-itmo-gh-acc/ITMO_ICT_WebDevelopment_2024-2025/refs/heads/main/students/K3340/laboratory_works/Ananiev_Nikita/site/assets/images/update_book.jpg)

## Можем удалить бронь
![alt text](https://raw.githubusercontent.com/nikita-itmo-gh-acc/ITMO_ICT_WebDevelopment_2024-2025/refs/heads/main/students/K3340/laboratory_works/Ananiev_Nikita/site/assets/images/delete_book.jpg)