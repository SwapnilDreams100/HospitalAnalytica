function line_chart(r,title,x_title,y_title, data_new) {

var chart = new CanvasJS.Chart("chartContainer"+r, {
	animationEnabled: true,
	title: {
		text: title
	},
	axisX: {
		title: x_title
	},
	axisY: {
		title: y_title,
		includeZero: false,
// 		scaleBreaks: {
// 			autoCalculate: true
// }
	
	},
	data: [{
		type: "line",
		dataPoints: data_new
	}]
}
);
chart.render();

}