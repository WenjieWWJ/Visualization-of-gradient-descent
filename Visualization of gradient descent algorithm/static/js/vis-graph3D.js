var data ;
var graph_3d = [];
var graph3d;
var container;
function custom(x, y, t) {
  return Math.sin(x/50 + t/10) * Math.cos(y/50 + t/10) * 50 + 50;
}

// Called when the Visualization API is loaded.
function drawVisualization() {
  // console.log("graph_3d is null : " + (graph_3d == null))
  // console.log("graph_3d is [] : " + (graph_3d == []))
  // console.log("graph_3d is '' : " + (graph_3d == ''))
  // console.log("graph_3d is :" + graph_3d)
  if(graph_3d != '')
  {
      // Create and populate a data table.
      // create some nice looking data with sin/cos
      // var counter = 0;
      // var steps = 50;  // number of datapoints will be steps*steps
      // var axisMax = 314;
      // var axisStep = axisMax / steps;
      // var z = 0
      // for (var x = 0; x < axisMax; x+=axisStep) {
      //     for (var y = 0; y < axisMax; y+=axisStep) {
      //         var value = (Math.sin(x/50) * Math.cos(y/50) * 50 + 50);
      //         data.add({id:counter++,x:x,y:y,z:value,style:value});
      //     }
      // }

      // points
      data = new vis.DataSet();
      var len = graph_3d.length;
      var x, y, z = 0;
      for (var i = 0;i < len;++ i)
      {
        x = graph_3d[i][0];
        y = graph_3d[i][1];
        z = graph_3d[i][2];
        data.add({id:i++,x:x,y:y,z:z,style:z});
      }


      // specify options
      var options = {
          width:  '450px',
          height: '450px',
          style: 'surface',
          showPerspective: true,
          showGrid: true,
          showShadow: false,
          keepAspectRatio: true,
          verticalRatio: 0.5,
          tooltip: {
              trigger: 'axis'
          },
      };

      // Instantiate our graph object.
      container = document.getElementById('gradientGraph');
      graph3d = new vis.Graph3d(container, data, options);
  }
}
