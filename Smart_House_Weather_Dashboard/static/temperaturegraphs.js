window.onload = function () {

var chart = new CanvasJS.Chart("dailyTemperatureGraph", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Daily Temperature Graph °C (Last 30 Days)"
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

var chart = new CanvasJS.Chart("monthlyTemperatureGraph", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Monthly Temperature Graph °C (Last 12 Months)"
	},
	data: [{
		type: "line", lineColor: "#0057fd", lineThickness: 5,
      	indexLabelFontSize: 16,
		dataPoints: [
			{label: "Jan", y: -20 },
			{label: "Feb", y: -10 },
			{label: "Mar", y: 0 },
			{label: "Apr", y: 10 },
			{label: "May", y: 20 },
			{label: "Jun", y: 30 },
			{label: "Jul", y: 40 },
			{label: "Aug", y: 50 },
			{label: "Sep", y: 35 },
			{label: "Oct", y: 16 },
			{label: "Nov", y: 2 },
			{label: "Dec", y: -10 }
		]
	}]
});
chart.render();

}

