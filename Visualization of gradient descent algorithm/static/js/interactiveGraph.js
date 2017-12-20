
// var data_points=[[15, 0], [-50, 10], [-56.5, 20], [-46.5, 30], [-22.1, 40]];
// var data_line = [[15, 0], [-50, 10],[-20,30]];

var data_points=[];
var data_line=[];


function drawInteractiveGraph(){
    var InteractiveChart = echarts.init(document.getElementById('interactiveGraph'));
    var symbolSize = 15;
    var symbolSize2 = 0;
    // data_points =
    // data_line =
    // console.log('data_points',data_points);

    option = {
        title: {
            text: 'Click to Add Points'
        },
        tooltip: {
            // formatter: function (params) {
            //     var data_points = params.data_points || [0, 0];
            //     return data_points[0].toFixed(2) + ', ' + data_points[1].toFixed(2);
            // },
            // trigger: 'axis'
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        // xAxis: {
        //     min: -1,
        //     max: 1,
        //     type: 'value',
        //     axisLine: {onZero: false}
        // },
        // yAxis: {
        //     min: -5,
        //     max: 5,
        //     type: 'value',
        //     axisLine: {onZero: false}
        // },
        xAxis: {
            type: 'value',
            boundaryGap: false,
            // data: data_x
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                id: 'a',
                type: 'scatter',
                smooth: true,
                symbolSize: symbolSize,
                data: data_points
            },
            {
                id: 'b',
                type: 'line',
                smooth: true,
                // tooltip:{
                // },
                symbolSize: symbolSize2,
                data: data_line
            }
        ],

    };
    InteractiveChart.setOption(option);

    var zr = InteractiveChart.getZr();


    zr.on('click', function (params) {
        var pointInPixel = [params.offsetX, params.offsetY];
        var pointInGrid = InteractiveChart.convertFromPixel('grid', pointInPixel);

        if (InteractiveChart.containPixel('grid', pointInPixel)) {
            data_points.push(pointInGrid);

            InteractiveChart.setOption({
                series: [{
                    id: 'a',
                    data: data_points
                }]
            });
        }
    });

    zr.on('mousemove', function (params) {
        var pointInPixel = [params.offsetX, params.offsetY];
        zr.setCursorStyle(InteractiveChart.containPixel('grid', pointInPixel) ? 'copy' : 'default');
    });

}
