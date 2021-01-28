<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Mi nombre es:  Miguel Castro</h2>
    <ul>
      <li>
        <a
          href="http://localhost:8080/problem-1/"
          target="_self"
        >
          Problema #1: Liga de Padel
        </a>
      </li>
    </ul>    
    <ul>
      <li>
        <a
          href="http://localhost:8080/problem-2/"
          target="_blank"
        >
          Problema #2: 
        </a>
      </li>
    </ul>       
    <ul>
      <li>
        <a
          href="http://localhost:8080/problem-3/"
          target="_blank"
        >
          Problema #1:
        </a>
      </li>
    </ul>    
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Bienvenido a mi Prueba de Desarrollo Web'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
