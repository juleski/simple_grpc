const vm = new Vue({
    el: '#app',
    data: {
      results: [],
      page: 1,
      page_size: 20
    },
    mounted() {
        axios.get("http://127.0.0.1:5000/meterusage")
        .then(response => {
            this.results = response.data
        })
    },
    methods: {
      fetch() {
        let url = `http://127.0.0.1:5000/meterusage?page=${this.page}&page_size=${this.page_size}`
        axios.get(url)
        .then(response => {
            this.results = response.data
        })
      }
    }
  });
  