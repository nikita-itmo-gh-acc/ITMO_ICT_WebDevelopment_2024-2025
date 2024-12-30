## Отображение номеров в отеле:
### Шаблон компоненты:
```html
    <Base />
    <Booking :show_list="true" ref="create" @update-state="showList"/>
    <h1 v-if="show_list" style="text-align: center;">Список номеров</h1>
    <div v-if="show_list" class="rooms__container">
        <div class="room__card" v-for="room in rooms">
            <div><span style="font-size: large; font-weight: bold;">Номер {{ room.number }}</span></div>
            <div><span>Площадь {{ room.area }}</span></div>
            <div v-if="room.is_occupied">
                <span>Занят на данный момент</span> <br>
                <button class="book__button"  @click="showBooking(room.id)">Забронировать</button>
            </div>
            <div v-if="!room.is_occupied">
                <span>Свободен</span> <br>
                <button class="book__button" @click="showBooking(room.id)">Забронировать</button>
            </div>
        </div>
    </div>
```
### В компоненте дополнительно используются дочерние компоненты Base (для отображения шапки) и Booking, для бронирования номера.

### Скрипт компоненты:
```javascript
import axios from "axios";
import Base from '@/components/Base.vue'
import Booking from "@/components/Booking.vue";

export default {
    components: {
        Base, Booking
    },
    name: "Rooms",
    data() {
        return {
            rooms: [],
            show_list: true,
        }
    },
    methods: {
        showBooking: function (id) {
            const user = JSON.parse(localStorage.getItem('user'));
            if (user) {
                this.$refs.create.show = true
                this.$refs.create.booking.room = id
                this.show_list = false
            } else {
                this.$router.push('/login');
            }
            
        },
        showList() {
            this.$refs.create.show = false
            this.show_list = true
        },
        async fetchRoomList () {
            try {
                const response = await axios.get('http://127.0.0.1:8000/rooms/list/');
                this.rooms = response.data
            } catch (e) {
                if (e.response) {
                    switch (e.response.status) {
                        case 404:
                            break;
                        default:
                            alert('Ошибка ответа!');
                    } 
                } else if (e.request) {
                    alert('Ошибка запроса!');
                }
            }
        }
    },
    mounted() {
        this.fetchRoomList() 
    }
}
```