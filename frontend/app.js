const vm = new Vue({
    el: '#app',
    data: {
      results: []
    },
    mounted() {
        axios.get("http://127.0.0.1:5000/meterusage")
        .then(response => {
            this.results = response.data
        })
    }
  });
  