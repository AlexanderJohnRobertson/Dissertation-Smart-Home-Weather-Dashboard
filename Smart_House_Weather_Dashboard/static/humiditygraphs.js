window.onload = function () {

var chart = new CanvasJS.Chart("dailyHumidityGraph", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Daily Humidity Graph % (Last 30 Days)"
	},
	data: [{
		type: "line", lineColor: "#21d39a", lineThickness: 5,
      	indexLabelFontSize: 16,
		dataPoints: [
			{ y: 0 },
			{ y: 5 },
			{ y: 10 },
			{ y: 15 },
			{ y: 20 },
			{ y: 25 },
			{ y: 30 },
			{ y: 35 },
			{ y: 40 },
			{ y: 45 },
			{ y: 50 },
			{ y: 55 },
            { y: 60 },
            { y: 65 },
            { y: 70 },
            { y: 75 },
            { y: 80 },
            { y: 85 },
            { y: 90 },
            { y: 95 },
            { y: 100 },
            { y: 96 },
            { y: 85 },
            { y: 75 },
            { y: 63 },
            { y: 52 },
            { y: 64 },
            { y: 98 },
            { y: 78 },
            { y: 63 },
            { y: 51 }
		]
	}]
});
chart.render();

var chart = new CanvasJS.Chart("monthlyHumidityGraph", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Monthly Humidity Graph % (Last 12 Months)"
	},
	data: [{
		type: "line", lineColor: "#0057fd", lineThickness: 5,
      	indexLabelFontSize: 16,
		dataPoints: [
			{label: "Jan", y: 20 },
			{label: "Feb", y: 30 },
			{label: "Mar", y: 40 },
			{label: "Apr", y: 50 },
			{label: "May", y: 60 },
			{label: "Jun", y: 70 },
			{label: "Jul", y: 80 },
			{label: "Aug", y: 90 },
			{label: "Sep", y: 100 },
			{label: "Oct", y: 75 },
			{label: "Nov", y: 63 },
			{label: "Dec", y: 78 }
		]
	}]
});
chart.render();

}

