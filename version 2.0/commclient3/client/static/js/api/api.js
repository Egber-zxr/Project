let APP_PATH = "http://127.0.0.1:8000/";


let LOCAL_APP_PATH = window.location.protocol+"//"+window.location.host+"/";


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

let ApiLocalManager = {


	post:function(url,data,success){
        console.log(LOCAL_APP_PATH+url)
		axios({
		    method: 'post',
		    url: LOCAL_APP_PATH+url,
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
		    url: LOCAL_APP_PATH+url,
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
