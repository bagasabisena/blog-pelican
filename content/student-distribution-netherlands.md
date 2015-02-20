Title: Distribution of Indonesian Student in the Netherlands
Date: 2014-11-29
Category: Blog
<<<<<<< HEAD
=======
Slug: student
>>>>>>> gallery
Tags: data visualization, d3.js

Well, wise man says that first blog post should be meaningful, so here I am. Below is a simple visualization built on [awesome D3.js](https://www.d3js.org). It shows the distribution of Indonesian student in cities of Netherlands in the year of 2013. Please note that I don't own the data. The data is made by PPI Belanda (Indonesian Student Union in the Netherlands). Big thanks to Arip Muttaqien for giving me the permission to use the data. Here goes! (Oh btw you can hover the cursor on the bubble and it will show you the real percentage and the universities where the students study).

<style>
    .place-label {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 10px;
        fill: #444;
    }

    .place {
        fill: #444;
    }

    .d3-tip {
      line-height: 1;
      font-weight: bold;
      padding: 12px;
      background: rgba(250, 250, 250, 0.8);
      color: #000;
      border-radius: 2px;
      pointer-events: none;
    }

    /* Creates a small triangle extender for the tooltip */
    .d3-tip:after {
      box-sizing: border-box;
      display: inline;
      font-size: 10px;
      width: 100%;
      line-height: 1;
      color: rgba(250, 250, 250, 0.8);
      position: absolute;
      pointer-events: none;
    }

    /* Northward tooltips */
    .d3-tip.n:after {
      content: "\25BC";
      margin: -1px 0 0 0;
      top: 100%;
      left: 0;
      text-align: center;
    }

    /* Eastward tooltips */
    .d3-tip.e:after {
      content: "\25C0";
      margin: -4px 0 0 0;
      top: 50%;
      left: -8px;
    }

    /* Southward tooltips */
    .d3-tip.s:after {
      content: "\25B2";
      margin: 0 0 1px 0;
      top: -8px;
      left: 0;
      text-align: center;
    }

    /* Westward tooltips */
    .d3-tip.w:after {
      content: "\25B6";
      margin: -4px 0 0 -1px;
      top: 50%;
      left: 100%;
    }

</style>

<div id="example"></div>

<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<<<<<<< HEAD
<script src="/js/topojson.v1.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
<script src="/js/tip.js"></script>
<script src="/js/mustache.js"></script>
=======
<script src="http://d3js.org/topojson.v1.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.6.3/d3-tip.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mustache.js/0.8.1/mustache.min.js"></script>
>>>>>>> gallery
<script id="template" type="x-tmpl-mustache">
    <div class="tip-container">
        <p style="font-size:80%">{{name}}: {{percent}}%</p>
        {{#uni_name}}
        <p style="font-size: 60%">{{.}}</p>
        {{/uni_name}}
    </div>
</script>
<script>

    var template = $('#template').html();
    Mustache.parse(template);

    var tip = d3.tip()
        .attr('class', 'd3-tip')
        .direction(function(d){
            if (d.name == 'Delft' || d.name == "Rotterdam" || d.name == "Tilburg") {
                return "sw"
            } else {
                return "ne"
            }
        })
        .html(function(d) {
            return Mustache.render(template, d);
        });

    var width = 960;
    var height = 780;

    var svg = d3.select('div#example').append('svg')
        .attr('width', width)
        .attr('height', height);

    svg.call(tip);

    var projection = d3.geo.mercator()
        .center([6.5,53.5])
        .scale(8500)
        .translate([width / 2, length / 3]);

    d3.json('/data/nld.json', function(err, nld) {
        if (err) return console.log(err);

        var subunits = topojson.feature(nld, nld.objects.subunits);

        var path = d3.geo.path()
            .projection(projection)
            .pointRadius(2);

        svg.append('path')
            .datum(subunits)
            .attr('d', path)
            .attr('fill', '#f0f0f0');

        d3.csv('/data/city.csv', function(error, data) {

            data.forEach(function(d){
                d.name = d.name;
                d.lat = +d.lat;
                d.long = +d.long;
                d.percent = +d.percent;
                d.uni_name = d.uni_name.split("|");
                d.uni_percent = d.uni_percent.split("|");
                for (var i = d.uni_name.length - 1; i >= 0; i--) {
                    d.uni = {uni_name: d.uni_name, uni_percent: d.uni_percent};
                };
            })
            
            var color = d3.scale.category20();
            var radiusScale = d3.scale.linear()
                .domain(d3.extent(data, function(d){return d.percent}))
                .range([5,30])

            svg.append('g')
                .attr('class', 'places')
                .selectAll("circle")
                .data(data)
                .enter()
                .append('circle')
                    .attr('class','place')
                    .attr('cx',function(d){return projection([d.long, d.lat])[0]})
                    .attr('cy',function(d){return projection([d.long, d.lat])[1]})
                    .attr('r', function(d){return radiusScale(d.percent)})
                    .style('fill', function(d){return color(d.name);})
                    .on('mouseover', function(d){
                        var radius = radiusScale(d.percent);
                        d3.select(this)
                            .attr('r', radius)
                            .transition()
                            .duration(250)
                            .attr('r', 1.2*radius)

                        tip.show(d);
                            // .transition()
                            // .duration(500)
                            // .attr('r', radius)
                            // .transition()
                            // .duration(500)
                            // .attr('r', 1.5*radius)
                            // .transition()
                            // .duration(500)
                            // .attr('r', radius)
                    })
                    .on('mouseout', function(d){
                        var radius = radiusScale(d.percent);
                        d3.select(this)
                            .transition()
                            .duration(250)
                            .attr('r',radius)

                        tip.hide(d);
                    });

            svg.select('g.places')
                .selectAll('.place-label')
                .data(data)
                .enter()
                .append('text')
                    .attr("class", "place-label")
                    .attr("transform", function(d) {return "translate(" + projection([d.long, d.lat]) + ")"; })
                    .attr("dy", ".35em")
                    .attr('dx', '1.2em')
                    .text(function(d) { return d.name; });

          
        });


      
    });
    
    

</script>