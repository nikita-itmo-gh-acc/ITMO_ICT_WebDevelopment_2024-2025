<template>
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
    
</template>

<script>
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
</script>

<style>
    .rooms__container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        justify-content: center;
        max-width: 80%;
        margin: auto;
        column-gap: 1em;    
        row-gap: 1em;
    }

    .room__card {
        background-color: #fff;
        border-radius: 10px;
        padding: 10%;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        max-width: 100%;
        transition: transform 0.3s;
    }

    .room__card div {
        margin-top: 5px;
        margin-bottom: 5px;
    }

    .room__card:hover {
        transform: translateY(-5px);
    }

    .book__button {
        background-color: #42b983;
        color: white;
        border: none;
        padding: 10px 15px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
</style>