# [Transferable Skills Workshops] - Good Practicies for Reproducible Open Source Code

## Why this workshop?
Open-source software is more than just sharing code; it’s about fostering collaboration, transparency, and reproducibility. In research, industry, and education, the ability to write clear, reproducible code is a vital skill. By adopting good practices in open-source software development, we can ensure that our code is not only easier to read and understand but also guarantees reproducibility across different machines and environments.

This approach enhances the quality of our work and opens the door to effective collaboration, enabling others to build upon our contributions with confidence. Whether you’re a student, researcher, or developer, mastering these practices is key to creating software that stands the test of time and benefits the broader community.

## Learning objectives

* Understand the importance of good practices for reproducibility and collaboration.
* Apply dependency management techniques using tools like Poetry.
* Understand the best practices in repository organization.
* Create and integrate a LICENSE file to meet open-source requirements.
* Develop and execute unit tests to ensure code functionality and reliability.

## Prerequisites

> [!IMPORTANT]  
> Please make sure that you have gone through the checklist in [TSW00-LABS-PREREQUISITES](https://github.com/UCL-Photonics-Society/TSW00-LABS-PREREQUISITES).

## Lab instructions

### How does the lab works?
This repository contains python files that can be used to generate different optical signals, and study the effect of dispersion during propagation in a fiber.
Althought the code is functional (you see for yourself by running the command `python main.py` in a terminal), this python project doesn't follow the good practices of open-source software development.

Step-by-step, we are going to restructure this project in order to make it complient with best practices, ensuring readability and reproducibility.

> [!TIP]
> We have created an autograding script that allows you to visualise your progress. To do so, simply go to the open Pull request `main->feedback` created in task#1.



### Tasks

#### 1️⃣ - Initialise the lab
>[!NOTE]
> If you are doing this lab as a Github Classroom assignment part of an official workshop, skip to task 2.

  * *fork* this repository using the fork button at the top of this repository.
  * From your forked repository, click on `main -> view all branches -> new branch`, and name the new branch `feedback`.
  * Create a pull request in your forked repository from branch `main` to branch `feedback`. Do not close it now!

#### 2️⃣ - Build a list of dependencies with Poetry
*TBD*

#### 3️⃣ - Restructure repository 
>[!CAUTION]
> The folder `.github/workflows/` contains the autograding script that assesses your progression and displays it in the pull request.
> 
> **Do not change anything in it**.



#### 4️⃣ - Add a LICENCE file
*TBD*

#### 5️⃣ - Write tests 
*TBD*

#### 6️⃣ - Check completion and submit
*TBD*

## Contributions
*TBD: Main contributors / maintainers.*
*TBD: Guide for using issues to suggest edits and improvements*
