window.onload = function () {

var chart = new CanvasJS.Chart("monthlyTemperatureGraph", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Monthly Temperature Graph °C (Last 12 Months)"
	},
	data: [{
		type: "line", lineColor: "#21d39a", lineThickness: 5,
      	indexLabelFontSize: 16,
		dataPoints: [
			{ y: 5 },
			{ y: 0 },
			{ y: 5 },
			{ y: 6 },
			{ y: 4 },
			{ y: 10 },
			{ y: 11 },
			{ y: 15 },
			{ y: 20 },
			{ y: 21 },
			{ y: 26 },
			{ y: 38 },
            { y: 35 },
            { y: 39 },
            { y: 43 },
            { y: 40 },
            { y: 35 },
            { y: -3 },
            { y: 17 },
            { y: -30 },
            { y: -23 },
            { y: -13 },
            { y: -7 },
            { y: 0 },
            { y: 3 },
            { y: 9 },
            { y: 16 },
            { y: 23 },
            { y: 25 },
            { y: 40 },
            { y: 51 }
		]
	}]
});
chart.render();

}