---
title: "Reliably Arranging Objects (PhD Thesis)"
date: "2019"
readTime: 5
tags:
  - PR2
  - Conformant Planning
  - Belief State
  - Manipulation
  - MIT CSAIL
summary: "Conformant planning approach to reliable robot manipulation under severe sensing and control uncertainty."
category: Robotics & AI
author: Ariel Anders
status: published
---

## Reliably arranging objects: a conformant planning approach to robot manipulation

A crucial challenge in robotics is achieving reliable results in spite of sensing and control uncertainty. In this work, we explore the conformant planning approach to reliable robot manipulation. In particular, we tackle the problem of pushing multiple planar objects simultaneously to achieve a specified arrangement without using external sensing. A conformant plan is a sequence of manipulation actions that reliably achieve a goal arrangement in spite of uncertainty in object pose and nondeterministic action outcomes, and without assuming the availability of additional observations.

To find conformant plans, we explored two different approaches:

*   **1) Conformant planning through plan improvement.** This approach takes a deterministic manipulation plan and augments it by adding fixtures (movable obstacles) to push parts up against. This method uses an optimization-based approach to determine the ideal fixture placement location.
*   **2) Conformant planning by construction.** This approach reformalizes conformant planning as a belief-state planning problem. A belief state is the set of all possible states of the world, and the objective is to find a sequence of actions that will bring an initial belief state to a goal belief state. To do forward belief-state planning, we created a deterministic belief-state transition model from on-line physics-based simulations and supervised learning based on off-line physics simulations.

This thesis provides insight and develops approaches toward scalable methods for solving challenging planar manipulation problems with multiple objects or concave shape geometry. We show the success of these approaches based on planning times and robustness in real and simulated experiments.
