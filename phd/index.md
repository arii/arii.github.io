---
title: Reliably Arranging Objects
layout: default
---


<div class="row ">
<div class="col-lg-12 text-center"> 
<h2> Reliably arranging objects: a conformant planning approach to robot manipulation </h2>
<p class="text-justify">
This page is dedicated to my PhD Thesis. I studied arranging objects into desired arrangements using a robot. Specifically, I considered the problem when there was substantial uncertainty in the problem due to inaccurate sensing and control, and imperfect knowledge of the world (eg.: friction, mass, properties of objects). In spite of these challenges, I was able to program a robot to robustly assemble some arrangements by using uncertainty-reducing actions, such as pushing, and successfully characterizing the noise of different actions. Using a conformant planner, I was able to sequence together different primitive actions that resulted in robust execution of desired arrangement in simulation and on a real robot.
</p>
</div>
</div>

<div class="row ">
<div class="col-lg-2">
<h3>Abstract</h3>
</div>
<div class="col-lg-10">
<p>A crucial challenge in robotics is achieving reliable results in spite of sensing and control uncertainty. In this work, we explore the conformant planning approach to reliable robot manipulation. In particular, we tackle the problem of pushing multiple planar objects simultaneously to achieve a specified arrangement without using external sensing.  A conformant plan is a sequence of manipulation actions that reliably achieve a goal arrangement in spite of uncertainty in object pose and nondeterministic action outcomes, and without assuming the availability of additional observations. To find conformant plans, we explored two different approaches:</p>
<p><em> 1) Conformant planning through plan improvement. </em> This approach takes a deterministic manipulation plan and augments it by adding fixtures (movable obstacles) to push parts up against. This method uses an optimization-based approach to determine the ideal fixture placement location.</p>
<p><em> 2) Conformant planning by construction.</em> This approach reformalizes conformant planning as a belief-state planning problem. A belief state is the set of all possible states of the world, and the objective is to find a sequence of actions that will bring an initial belief state to a goal belief state. To do forward belief-state planning, we created a deterministic belief-state transition model from on-line physics-based simulations and supervised learning based on off-line physics simulations.</p>
<p>
This thesis provides insight and develops approaches toward scalable methods for solving challenging planar manipulation problems with multiple objects or concave shape geometry.  We show the success of these approaches based on planning times and robustness in real and simulated experiments.
</p>
</div>
</div>

<div class="row ">
<div class="col-lg-2">
<h3>Thesis</h3>
</div>
<div class="col-lg-10">
<p>
Link to thesis coming soon!
</p>
</div>
</div>

<div class="row ">
<div class="col-lg-2">
<h3>Slides</h3>
</div>
<div class="col-lg-10">
<iframe src="https://mitprod-my.sharepoint.com/personal/aanders_mit_edu/_layouts/15/Doc.aspx?sourcedoc={3928306b-b08c-4425-9c11-f4a850da59ff}&amp;action=embedview&amp;wdAr=1.7777777777777777" width="610px" height="367px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office Online</a>.</iframe>
</div>
</div>

