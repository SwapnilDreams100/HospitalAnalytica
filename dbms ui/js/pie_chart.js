function pie_chart(r,title, data_new) {

var chart = new CanvasJS.Chart("chartContainer"+r, {
	animationEnabled: true,
	title: {
		text:title
	},
	data: [{
		type: "pie",
		dataPoints: data_new
	}]
});
chart.render();
}