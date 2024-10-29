var chart2 = am4core.create("chartdiv", am4charts.XYChart);

chart2.data = [{
  "hour": "01",
  "temperature": 10
}, {
  "hour": "02",
  "temperature": 6
}, {
  "hour": "03",
  "temperature": 1
}, {
  "hour": "04",
  "temperature": -3
}, {
  "hour": "05",
  "temperature": -7
}, {
  "hour": "06",
  "temperature": -6
}, {
  "hour": "07",
  "temperature": -4
}, {
  "hour": "08",
  "temperature": 0
}, {
  "hour": "09",
  "temperature": 5
}, {
  "hour": "10",
  "temperature": 7
}, {
  "hour": "11",
  "temperature": 14
}, {
  "hour": "12",
  "temperature": 21
}, {
  "hour": "13",
  "temperature": 27
}, {
  "hour": "14",
  "temperature": 31
}, {
  "hour": "15",
  "temperature": 30
}, {
  "hour": "16",
  "temperature": 27
}, {
  "hour": "17",
  "temperature": 22
}, {
  "hour": "18",
  "temperature": 20
}, {
  "hour": "19",
  "temperature": 20
}, {
  "hour": "20",
  "temperature": 16
}, {
  "hour": "21",
  "temperature": 14
}, {
  "hour": "22",
  "temperature": 11
}, {
  "hour": "23",
  "temperature": 6
}, {
  "hour": "Now",
  "temperature": 5
}, ];

chart2.padding(40, 40, 40, 40);

let categoryAxis = chart2.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.renderer.grid.template.location = 0;
categoryAxis.dataFields.category = "hour";
categoryAxis.renderer.minGridDistance = 60;

let valueAxis = chart2.yAxes.push(new am4charts.ValueAxis());

let series = chart2.series.push(new am4charts.ColumnSeries());
series.dataFields.categoryX = "hour";
series.dataFields.valueY = "temperature";
series.tooltipText = "{name}: {valueY}";
series.name = "Temperature (ºC)";
series.columns.template.focusable = true;
series.columns.template.hoverOnFocus = true;
series.columns.template.tooltipText = "xx {valueY}";
series.properties.fill = am4core.color("#29c996");


chart2.scrollbarX = new am4core.Scrollbar();

chart2.legend = new am4charts.Legend();


chart2.cursor = new am4charts.XYCursor();



/**
 * ========================================================
 * Enabling responsive features
 * ========================================================
 */

chart2.responsive.enabled = true;
chart2.responsive.useDefault = false

chart2.responsive.rules.push({
  relevant: function(target) {
    if (target.pixelWidth <= 400) {
      return true;
    }
    
    return false;
  },
  state: function(target, stateId) {
    
    if (target instanceof am4charts.Chart) {
      console.log("xy chart state")
      var state = target.states.create(stateId);
      state.properties.paddingTop = 0;
      state.properties.paddingRight = 15;
      state.properties.paddingBottom = 5;
      state.properties.paddingLeft = 15;
      return state;
    }
    
    if (target instanceof am4core.Scrollbar) {
      console.log("xy scrollbar state")
      var state = target.states.create(stateId);
      state.properties.marginBottom = -10;
      return state;
    }
    
    if (target instanceof am4charts.Legend) {
      console.log("xy legend state")
      var state = target.states.create(stateId);
      state.properties.paddingTop = 0;
      state.properties.paddingRight = 0;
      state.properties.paddingBottom = 0;
      state.properties.paddingLeft = 0;
      state.properties.marginLeft = 0;
      target.setStateOnChildren = true;
      target.itemContainers.template.setStateOnChildren = true;
      target.itemContainers.template.applyOnClones = true;
      target.markers.template.applyOnClones = true;
      var markerState = target.markers.template.states.create(stateId);
      markerState.properties.width = 15;
      markerState.properties.height = 10;
      return state;
    }
    
    if (target instanceof am4charts.AxisRendererY) {
      console.log("xy yaxis state")
      var state = target.states.create(stateId);
      state.properties.inside = true;
      state.properties.maxLabelPosition = 0.99;
      return state;
    }
    
    if ((target instanceof am4charts.AxisLabel) && (target.parent instanceof am4charts.AxisRendererY)) { 
      console.log("xy axis label state")
      var state = target.states.create(stateId);
      state.properties.dy = -15;
      state.properties.paddingTop = 3;
      state.properties.paddingRight = 5;
      state.properties.paddingBottom = 3;
      state.properties.paddingLeft = 5;
      
      // Create a separate state for background
      target.setStateOnChildren = true;
      var bgstate = target.background.states.create(stateId);
      bgstate.properties.fill = am4core.color("#fff");
      bgstate.properties.fillOpacity = 0.7;
      
      return state;
    }
    
    // if ((target instanceof am4core.Rectangle) && (target.parent instanceof am4charts.AxisLabel) && (target.parent.parent instanceof am4charts.AxisRendererY)) { 
    //   var state = target.states.create(stateId);
    //   state.properties.fill = am4core.color("#f00");
    //   state.properties.fillOpacity = 0.5;
    //   return state;
    // }
    
    return null;
  }
});

chart2.responsive.rules.push({
  relevant: function (target) {
    if (target.pixelWidth > target.pixelHeight) {
      return true;
    }
    return false;
  },
  state: function (target, stateId) {
    if (target instanceof am4charts.Legend) {
      console.log("xy move legend state")
      var state = target.states.create(stateId);
      state.properties.position = "right";
      return state;
      //target.position = "right";
    }

  }
});