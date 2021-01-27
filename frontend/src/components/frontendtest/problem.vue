<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Liga de Padel</h2>
                <span>Lista de partidos:</span>
                <br>
                <b-form-textarea
                    id="input-1"
                    v-model="text"
                    placeholder="Enter something..."
                    prop="text"
                    rows="10"
                    cosl="2"
                ></b-form-textarea>
                <br>
                <b-button v-on:click="getData()">Enviar lista</b-button>
                <br> 
                <br> 
                <span>Resultados:</span>
                <br>
                <pre id="output-1">{{ resp }}
                </pre>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios)
export default {
    name:"problem",
    data(){
        return{
            text:null,
            resp:null
        }
    },
    methods:{
        getData(e){
            this.axios.post('http://127.0.0.1:8000/problem-1/',this.text).then((response)=>{
                this.resp=""
                for (const prop in response.data) {
                    this.resp=this.resp +" "+response.data[prop]+"\n"
                }
            })
        }
    }
}
</script>

<style lang="css" scoped>

</style>
