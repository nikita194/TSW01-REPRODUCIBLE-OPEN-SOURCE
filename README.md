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
> We have created an autograding script that allows you to visualise your progress. To do so, simply go to the open Pull request `main->feedback` created in task#0.



### Tasks

#### 0️⃣ - Initialise the lab
>[!NOTE]
> If you are doing this lab as a Github Classroom assignment part of an official workshop, skip to task 1.

  * *fork* this repository using the fork button at the top of this repository.
  * From your forked repository, click on `main -> view all branches -> new branch`, and name the new branch `feedback`.
  * Create a pull request in your forked repository from branch `main` to branch `feedback`. Do not close it now!



#### 1️⃣ - Restructure repository 
In this task, you must restructure the repository following the best practice of python package structure for a librairy. We will call this librairy `opticaldisp`.

>[!CAUTION]
> The folder `.github/workflows/` contains the autograding script that assesses your progression and displays it in the pull request, it must not be modified.

* Make the codebase modular:
  * Create a `waveforms.py` file, and move all the waveform generating functions found in `main.py` there.
  * Create a `dispersion.py` file, and move the function `apply_dispersion` there.
  * Create a `optical_signals.py` file, and move the class `OpticalSignal`.
* Group all the files containing functions and classes into a `src/opticaldisp/` folder.
* Add imports to your python files:
  * In `waveform.py`, `dispersion.py`, and `optical_signals.py`, import the specific python packages that are used by the functions and classes used in their respective files.
  * In `main.py`, import the functions and classes you moved to `waveform.py`, `dispersion.py`, and `optical_signals.py`. For example, if you want to import the class `OpticalSignal` in `main.py`, use `from src.opticaldisp.optical_signals import OpticalSignal`
 
>[!TIP]
> Run `python main.py` to check if you have handled imports successfully.

For this task to be completed, you must be able to run `python main.py` without errors, and the repository must have the following structure:

```plaintext
├── tsw01
│   ├── src
│   │   ├── opticaldisp
│   │   │   ├── waveforms.py
│   │   │   ├── optical_signals.py
│   │   │   ├── dispersion.py
│   ├── .github
│   │   ├── workflows
│   │   │   ├── autograding.yml
│   ├── main.py
│   ├── README.md
│   ├── .gitignore
```

#### 2️⃣ - Build a list of dependencies with Poetry

#### 3️⃣ - Linting and formatting



#### 4️⃣ - Add a LICENCE file
*TBD*

#### 5️⃣ - Write tests 
*TBD*

#### 6️⃣ - Check completion and submit
*TBD*

## Contributions
### Contributors
* [David Gerard](https://github.com/David-GERARD) - PhD student @ UCL
* [Mikulas Poul](https://github.com/mikicz) - Staff engineer @ Xelix

> [!TIP]
> * If you encounter a bug, please let us know using the [Issues tab](https://github.com/UCL-Photonics-Society/TSW01-REPRODUCIBLE-OPEN-SOURCE/issues).
> * If you have improvement ideas, *fork* the repository, implement them, and create a pull request in which you provide a detailed changelog and the motivations for it.

### Maintainers
If need be, you can reach out to [David Gerard](https://github.com/David-GERARD) at david.gerard.23@ucl.ac.uk.
