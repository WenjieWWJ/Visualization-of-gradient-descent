
var data_x=[];
var data_y=[];

function drawLossGraph(){
    var myChart = echarts.init(document.getElementById('lossGraph'));

    option = {
        title: {
            text: 'loss'
        },
        tooltip: {
            trigger: 'axis'
        },
        // legend: {
        //     data:
        // },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: data_x
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'loss',
                type:'line',
                smooth: true,
                data:data_y
            }
            
        ]
    };

    myChart.setOption(option);

}