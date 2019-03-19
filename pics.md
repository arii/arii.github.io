---
title: PhD Videos
layout: default
---


<div class="row">
<div class="col-lg-12 text-center ">
<h1>PhD Videos</h1>
<p class="text-justify"> Here are some pictures and videos from my PhD thesis.
</p>
</div>
</div>

<div class="row" >
<div class="col-lg-6">
<a href ="/phd/sixblock.mp4">
<img class="projects" src="/phd/sixblock.png" alt="">
</a>
</div>
<div class="col-lg-6">
	<a href ="/phd/sixblock.mp4">
    <h3>PR2 reliably arranging six blocks
    </h3>
    </a>
    <p> 
    Here the robot is assembling 1-inch blocks using a mixture of placing and pushing actions.  What we see here is the execution of a conformant plan.  Prior to execution, we used machine learning to characterise the uncertainty of the placing and pushing actions; then, we used a conformant planner to find a sequence of actions that form the desired arrangement.  
    </p>
    </div>
</div>

<div class="row" >
<div class="col-lg-6">
<a href ="/phd/beliefoverlay.avi">
<img class="projects" src="/phd/beliefoverlay.png" alt="">
</a>
</div>
<div class="col-lg-6">
	<a href ="/phd/beliefoverlay.avi">
    <h3>Arranging objects with belief overlay
    </h3>
    </a>
    <p> 
    This video shows a visualization of the robot's belief of the objects location during the arrangement process.  The robot did not use perception during the execution-- this overlay is created for us to visualize the algorithm (and debugging).
    </p>
    </div>
</div>

 
<div class="row" >
<div class="col-lg-6">
<a href ="/phd/placing.mp4">
<img class="projects" src="/phd/placing.png" alt="">
</a>
</div>
<div class="col-lg-6">
	<a href ="/phd/placing.mp4">
    <h3>PR2 placing blocks
    </h3>
    </a>
    <p> 
    This video shows some of the placing experiments I conducted to characterise the uncertainty of a place action.  As you can see, there is considerable noise whne placing the block-- this is due to the block sticking to the robots finger's while being dropped.  I estimated the placing offset to have about plus or or minus 0.15 inch noise in desired x or y position and up to 15 degrees rotational offset.
    </p>
    </div>
</div>

    
<div class="row" >
<div class="col-lg-2">
<a href ="/phd/tetris1.avi">
<img class="projects" src="/phd/tetris1.png" alt="">
<h4>Original Plan</h4>
</a>
</div>
<div class="col-lg-2">
<a href ="/phd/tetris2.avi">
<img class="projects" src="/phd/tetris2.png" alt="">
<h4>Original Plan executed with noise (19/1000 reliablity score)</h4>
</a>
</div>
<div class="col-lg-2">
<a href ="/phd/tetris3.avi">
<img class="projects" src="/phd/tetris3.png" alt="">
<h4>Improved plan executed with noise (807/1000 reliability score)</h4>
</a>
</div>
<div class="col-lg-6">
    <h3>Plan improvement with fixture placement
    </h3>
    <p> 
   The second part of my thesis looked at improving plans that were originally found without considering uncertainty.  Given this easier initial planning problem, we could solve plans for more complicated shapes and desired poses. Then, we ran an optimization algorithm to improve the initial plan by placing <em>fixtures</em>. </p>
  <!-- 
   <p>In these videos, the goal is to merge the two tetris shapes together relative to one another.  
   The "original plan" video shows a forward simulation of running the initial plan, but without considering uncertainty.  In the second video, we show that adding noise to the execution results in many failed arrangements (19/1000 reliability score).  In the third video, we show several fixtures that are added to improve the overall reliablity (807/1000 reliability score).  The description of this algorithm is provided in detail in my thesis.
    </p>
    -->
    </div>
</div>


<div class="row" >
<div class="col-lg-6">
<img class="projects" src="/phd/eric.png" alt="">
</div>
<div class="col-lg-6">
    <h3>Eric the red robot
    </h3>
    <p> 
    This is Eric, the cartoon robot that was prevelant in every slide during my thesis defense.</p>
    <p>
    Eric is named and based off of Leslie P. Kaelbling's "Eric the Red Robot". Leslie attributes her robot stick figure drawing to her advisor and came before the original "Eric" robot even existed.  
    </p>
    <p>
    Here are a couple of versions of Eric I created using Inkscape:  <a href="/phd/eric1.png">Eric with a picketing sign</a> and <a href="/phd/eric2.png">Blindfolded Eric not using his perception sensors</a>. </p>
    </div>
</div>


