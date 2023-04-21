let APP_PATH = "http://127.0.0.1:8000/";

let ApiManager = {
	
	post:function(url,data,success){

		axios({
		    method: 'post',
		    url: APP_PATH+url,
		    headers: {
		        'Content-type': 'application/json'
		    },
		    data: data
		})
		  .then(function (response) {
			success(response.data);
		  })
		  .catch(function (error) {
		    console.log(error);
		  });
		  
	},
	get:function(url,data,success){

		axios({
		    method: 'get',
		    url: APP_PATH+url,
		    headers: {
		        'Content-type': 'application/json'
		    },
		    params: data
		})
		  .then(function (response) {
			success(response.data);
		  })
		  .catch(function (error) {
		    console.log(error);
		  });
		  
	}
	
}