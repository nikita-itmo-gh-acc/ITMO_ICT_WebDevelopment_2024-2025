<template>
    <h1 style="text-align: center;"> Вы успешно вышли из аккаунта </h1>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'Logout',
        methods: {
            async logout () {
                const token = localStorage.getItem('token');
                if (token) {
                    console.log(token)
                    try {
                        const response = await axios.post('http://127.0.0.1:8000/auth/token/logout/');
                        console.log(response.data)
                        console.log('aaa')
                    } catch (e) {
                        if (e.response) {
                            switch (e.response.status) {
                                case 401:
                                    break;
                                default:
                            }
                        }
                    } finally {
                        console.log('here delete all')
                        localStorage.removeItem('token');
                        localStorage.removeItem('user');
                        delete axios.defaults.headers.common["Authorization"];
                    }
                }
            }
        }, 
        mounted() {
            this.logout() 
        }
    }

    
</script>
    
<style>

</style>