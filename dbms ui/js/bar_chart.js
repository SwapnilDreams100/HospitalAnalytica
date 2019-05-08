function bar_chart(r,title,x_title,y_title, data_new) {
	console.log(data_new)
// if('x' in Object.keys(data_new[0])){
// var chart = new CanvasJS.Chart("chartContainer"+r, {
// 	animationEnabled: true,
// 	title: {
// 		text: title
// 	},
// 	axisX: {
// 		title: x_title
// 	},
// 	axisY: {
// 		title: y_title
	
// 	},
// 	data: [{
// 		type: "column",
// 		dataPoints: data_new
// 	}]
// });
// chart.render();

// }
// else{
// 	console.log('in')
// var chart = new CanvasJS.Chart("chartContainer"+r, {
// 	animationEnabled: true,
// 	title: {
// 		text: title
// 	},
// 	axisX: {
// 		title: x_title,
// 		interval:1
// 	},
// 	axisY: {
// 		title: y_title
	
// 	},
// 	data: [{
// 		type: "column",
// 		dataPoints: data_new
// 	}]
// });
// chart.render();

// }
var chart = new CanvasJS.Chart("chartContainer"+r, {
	animationEnabled: true,
	title: {
		text: title
	},
	axisX: {
		title: x_title
	},
	axisY: {
		title: y_title
	
	},
	data: [{
		type: "column",
		dataPoints: data_new
	}]
});
chart.render();

}