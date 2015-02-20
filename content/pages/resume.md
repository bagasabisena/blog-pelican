Title: Resume
Date: 2015-02-20 11:20
Summary: My current Resume

[**pdf version**](/raw/resume.pdf)

-------

<div id='cv-content'>

<style type="text/css">code{white-space: pre;}</style>
<style type="text/css">
  /*
   * Copyright 2013 Christophe-Marie Duquesne <chmd@chmd.fr>
   *
   * CSS for making a resume with pandoc. Inspired by moderncv.
   *
   * This CSS document is delivered to you under the CC BY-SA 3.0 License.
   * https://creativecommons.org/licenses/by-sa/3.0/deed.en_US
   */

   @import url("http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css");

  /* Whole document */
  #cv-content {
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      width: 800px;
      margin: auto;
      background: #FFFFFF;
      padding: 10px 10px 10px 10px;
  }

  [class*='custom-col-'] {
    float: left;
  }

  .custom-col-2-3 {
    width: 60%;
  }
  .custom-col-1-3 {
    width: 40%;
  }

  .custom-grid:after {
    content: "";
    display: table;
    clear: both;
  }

  /* Title of the resume */
  div#cv-content h1 {
      font-size: 38px;
      color: #3F51B5;
      /*text-align:left;
      margin-bottom:15px;*/
  }
  /*h1:hover {
      background-color: #757575;
      color: #FFFFFF;
      text-shadow: 1px 1px 1px #333;
  }*/

  /* Titles of categories */
  div#cv-content h2 {
      /* This is called "sectioncolor" in the ConTeXt stylesheet. */
      color: #7986CB;
  }
  /* There is a bar just before each category */
  /*h2:before {
      content: "";
      display: inline-block;
      margin-right:1%;
      width: 16%;
      height: 10px;
      background-color: #9CB770;
  }
  h2:hover {
      background-color: #397249;
      color: #FFFFFF;
      text-shadow: 1px 1px 1px #333;
  }*/

  /* Definitions */
  div#cv-content dt {
      float: left;
      clear: left;
      width: 17%;
      /*font-weight: bold;*/
  }
  div#cv-content dd {
      margin-left: 17%;
  }
  div#cv-content p {
      margin-top:0;
      margin-bottom:7px;
  }

  /* Blockquotes */
  div#cv-content blockquote {
      text-align: center
  }

  /* Links */
  div#cv-content a {
      text-decoration: none;
      color: #9FA8DA;
  }
  div#cv-content a:hover, a:active {
      background-color: #9FA8DA;
      color: #FFFFFF;
      text-decoration: none;
      text-shadow: 1px 1px 1px #333;
  }

  /* Horizontal separators */
  div#cv-content hr {
      color: #A6A6A6;
  }

  div#cv-content table {
      width: 100%;
  }
</style>

<div class="custom-grid" markdown="1">
<div class="custom-col-2-3">
<h1>Bagas Abisena Swastanto</h1>
</div>
<div class="custom-col-1-3">
<ul class="fa-ul">
<li>
<i class="fa fa-li fa-envelope-o"></i><script type="text/javascript">
<!--
h='&#x67;&#x6d;&#x61;&#x69;&#108;&#46;&#x63;&#x6f;&#x6d;';a='&#64;';n='&#98;&#x61;&#x67;&#x61;&#x73;&#x61;&#98;&#x69;&#x73;&#x65;&#110;&#x61;';e=n+a+h;
document.write('<a h'+'ref'+'="ma'+'ilto'+':'+e+'" clas'+'s="em' + 'ail">'+e+'<\/'+'a'+'>');
// -->
</script><noscript>&#98;&#x61;&#x67;&#x61;&#x73;&#x61;&#98;&#x69;&#x73;&#x65;&#110;&#x61;&#32;&#x61;&#116;&#32;&#x67;&#x6d;&#x61;&#x69;&#108;&#32;&#100;&#x6f;&#116;&#32;&#x63;&#x6f;&#x6d;</noscript>
</li>
<li>
<i class="fa fa-li fa-globe"></i><a href="http://abisena.me">abisena.me</a>
</li>
<li>
<i class="fa fa-li fa-home"></i>Delft, Netherlands
</li>
</ul>
</div>
</div>
<hr />
<h2 id="education">Education</h2>
<dl>
<dt>2014-2016 (Expected)</dt>
<dd><p><strong>MSc in Computer Science</strong> Delft University of Technology, The Netherlands</p>
<ul>
<li><strong>Courses</strong>: Pattern Recognition, Statistical Multivariate Data Analysis, Data Visualization, High-Tech Startup, Information Retrieval, Machine Learning, Applied Optimization Technique.</li>
</ul>
</dd>
<dt>2007-2011</dt>
<dd><p><strong>BSc in Telecommunication Engineering</strong> Institut Teknologi Bandung, Indonesia</p>
<p>(GPA: 3.43 of 4.00)</p>
<ul>
<li><strong>Thesis</strong>: <em>Video Processing Application for Intelligent Traffic Monitoring using Optical Flow Technique</em>. Calculate vehicle speed using OpenCV's implementation of <em>optical flow</em> motion tracking algorithm. <a href="http://www.abisena.me/drafts/bachelor">Link</a></li>
</ul>
</dd>
</dl>
<hr />
<h2 id="work-experience">Work Experience</h2>
<dl>
<dt>September 2011-August 2014</dt>
<dd><p><strong>Network Engineer</strong> Ericsson Indonesia</p>
<ul>
<li>Key engineer for Ericsson IPWorks (Linux-based DNS/DHCP/AAA server) in Indonesia.</li>
<li>Aside from daily server installation, administration, and troubleshooting, I also did many Python scripting to ease out the work.</li>
<li><strong>Notable project</strong>: Deployed biggest fixed IP Multimedia Subsystem (IMS) network in Asia Pacific for Telkom Indonesia between 2012-2013. I played important role in designing and implementing IMS DNS solution for whole network with team consisted of multinational engineers.</li>
</ul>
</dd>
</dl>
<hr />
<h2 id="technical-experience">Technical Experience</h2>
<h3 id="programming-languages">Programming Languages</h3>
<ul>
<li><p><strong>Java</strong> Mostly proficient in Android. I also worked on with Spring Framework and Grails for backend in the past.</p></li>
<li><p><strong>Python</strong> I have experience in using Django for developing Restful backend. I also utilize python for crawling website and other small scripting stuffs.</p></li>
<li><p><strong>Others</strong> I use <strong>Matlab</strong> for coursework in Pattern Recognition and Machine Learning, <strong>R</strong> for statistical data analysis, and <strong>Javascript</strong> for D3.js visualization. I also have basic knowledge of frontend web development (bootstrap3, jquery, html, css). Apart from programming, I have great understanding about <strong>TCP/IP</strong> stack.</p></li>
</ul>
<h3 id="projects">Projects</h3>
<ul>
<li><p><strong>Cravn (2013)</strong></p>
<p>A prototype for business idea <a href="http://www.abisena.me/drafts/cravn">Cravn</a>, a wishlist sharing social media. This was a working Android application in conjuction with restful API backend made in Grails and later ported to Django. Data was modeled with graph in Neo4j graph database instead of traditional SQL, enabled easy relationship and recommendation analysis.</p></li>
<li><p><strong>NIST Digit Handwriting Recognition (2015)</strong></p>
<p>Group-based assignment for Pattern Recognition course. Implemented using Matlab and <a href="http://prtools.org/">PRTools</a>.</p>
<ul>
<li>Achieved 97% accuracy with 5000 training digits with radial basis Support Vector Machine (SVM). We used pixel as representation.</li>
<li>Achieved 75% accuracy with 100 training digits with 1-Nearest Neighbor (1-NN). We used euclidean dissimiliarity as representation.</li>
</ul></li>
<li><p><strong>Progress-Tree Visualization (2015)</strong></p>
<p>A visualization project to provide an alternative of progress bar by modelling leaves that grow on leafless tree in spring to visualize progress. The tree was drawn using D3.js. See more <a href="http://www.abisena.me/progress-tree">here</a></p></li>
<li><p><strong>Dota2 Spatial-Temporal Analytics (2014)</strong></p>
<p>Given time-series dataset about position of Dota2 players (in x and y coordinate), me and my project partner were able to identify that players from different skill tiers have different positioning pattern across the map. The insight was visualized with heatmap using D3.js and canvas.</p></li>
<li><p><strong>Rumpy (2012)</strong></p>
<p>Prototype for business idea <a href="http://www.abisena.me/rumpy">Rumpy</a>, an instant messenger application over websocket protocol. Client was built in Android and server was developed in Java on top of Netty Framework.</p></li>
<li><p><strong>Student Distribution Map (2014)</strong></p>
<p>A simple interactive visualization I made in D3.js about the distribution of Indonesian students in the Netherlands. It is now featured in the Indonesian Student Association <a href="http://ppibelanda.org/infografis/">website</a>.</p></li>
<li><p><strong>Others</strong> Check my other hobby projects in my <a href="http://github.abisena.me">github</a></p></li>
</ul>
<hr />
<h2 id="achievements">Achievements</h2>
<ul>
<li><p><strong>Indonesia Endowment Fund for Education Scholarship Awardee</strong> Full scholarship covers tuition and living cost for my master study in the Netherlands.</p></li>
<li><p><strong>Indonesia ICT Awards (INAICTA) 2013 Finalist</strong> The business idea Cravn was selected as one of eight finalists (category: Digital Interactive Media) from thousands of participants in the annual nationwide ICT application competition held by Ministry of Communication and Information Republic of Indonesia.</p></li>
<li><p><strong>Samsung Developer Competition 2013 Finalist</strong> Finalist in Android application developer competition held by Samsung Indonesia for Cravn prototype.</p></li>
<li><p><strong>Ericsson Indonesia Team of the Quarter Q1 2013</strong> Successfully deployed the IMS network at first time in Asia Pacific.</p></li>
<li><p><strong>Ericsson Indonesia Employee of the Month May 2014</strong> The award was given to me for successfully implementing and testing DHCP failover servers across 4 cities in Indonesia under one month giving the project one month lead time.</p></li>
</ul>
<hr />
<h2 id="organizational-experience">Organizational Experience</h2>
<ul>
<li><p><strong>Indonesian Student Association in The Netherlands (Present)</strong> Leading a demographic research project which the goals are to collect student information from various sources (survey, social media), make analysis, and visualize the findings to map the potential of Indonesian scholars in the Netherlands.</p></li>
<li><p><strong>Electrical Engineering Student Union Institut Teknologi Bandung (2010)</strong> Leading the division of Internal Affairs with team of 10 people. We created several breakthrough programs such as graduation gala dinner and movie night that are now become the routine in the organization.</p></li>
</ul>
<hr />
<h2 id="others">Others</h2>
<ul>
<li><strong>Human languages</strong> Indonesian (mother tongue) and English (IELTS: 7.0)</li>
<li><strong>Hobby</strong> I like taking photos especially in travel and street photography. Please check my photos in my <a href="http://flickr.abisena.me">flickr</a>.</li>
</ul>

