<template>
    <div v-if="show" class="booking__form__container">
        <h2>Бронирование</h2>
        <form @submit.prevent="createBooking">
            <div class="form__group">
                <label for="booking.from_town">Укажите ваш город</label>
                <input type="text" id="__username" v-model="booking.from_town" required />
            </div>
            <div class="form__group">
                <label for="booking.planned_begin_date">Запланированная дата начала</label>
                <input type="date" id="__username" v-model="booking.planned_begin_date" required />
            </div>
            <div class="form__group">
                <label for="booking.planned_end_date">Запланированная дата окончания</label>
                <input type="date" id="__checkInDate" v-model="booking.planned_end_date" required />
            </div>
            <button type="submit" class="submit__button">Забронировать</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Booking',
        data() {
            return {
                booking: {
                    room: '',
                    client: '',
                    booking_date: '',
                    planned_begin_date: '',
                    planned_end_date: '',
                    from_town: '',
                },
                show: false,
            }
        },
        props : [
            'show_list'
        ],
        methods: {
            hideBooking () {
                this.$emit('update-state', true)
            },
            async createBooking () {
                try {
                    this.booking.client = JSON.parse(localStorage.getItem('user')).id;
                    this.booking.booking_date = new Date().toJSON().slice(0, 10);
                    console.log(this.booking)
                    await axios.post('http://127.0.0.1:8000/bookings/add/', this.booking);
                    this.$router.push('/bookings');
                } catch (e) {
                    alert('error');
                    if (e.response) {
                        switch (e.response.status) {
                            case 401:
                                break;
                            default:
                        }
                    }
                }
            }
        }
    }
</script>

<style>
    @import '../assets/booking.css';
</style>