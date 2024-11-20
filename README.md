
# [Transferable Skills Workshops] - Good Practices for Reproducible Open Source Code

---

## Why this Workshop?

Open-source software is more than just sharing code; it’s about fostering **collaboration**, **transparency**, and **reproducibility**. Whether in research, industry, or education, writing clear and reproducible code is a critical skill. Adopting good practices ensures your code is:

- Easier to read and understand.
- Reproducible across machines and environments.

This leads to higher-quality work and fosters collaboration, allowing others to confidently build upon your contributions.

---

## Learning Objectives

- Understand the importance of good practices for reproducibility and collaboration.
- Apply dependency management techniques using tools like Poetry.
- Restructure repositories using best practices.
- Create and integrate a LICENSE file for open-source compliance.
- Develop and execute unit tests to ensure code reliability.

---

## Prerequisites

> [!IMPORTANT]
> Please ensure you've completed the checklist in [TSW00-LABS-PREREQUISITES](https://github.com/UCL-Photonics-Society/TSW00-LABS-PREREQUISITES).

---

## Lab Instructions

### **How Does the Lab Work?**

This repository contains Python files to generate optical signals and study dispersion effects during fiber propagation. While functional (`python main.py` runs the code), it does not follow good open-source practices.

In this lab, you will **restructure** the project step-by-step to make it compliant with best practices, ensuring **readability** and **reproducibility**.

> [!TIP] 
> Use the autograding script in the open pull request `main -> feedback` (created in Task #0) to track your progress.

---

### **Tasks**

#### 0️⃣ - Initialize the Lab

> [!NOTE]  
> If this is part of a GitHub Classroom assignment, skip to Task #1.

1. **Fork** this repository using the button at the top.  
2. Create a new branch: `main -> view all branches -> new branch` and name it `feedback`.  
3. Create a pull request in your fork: branch `main` -> branch `feedback`. Leave the PR open.

---

#### 1️⃣ - Clone the Repository Locally

1. On your fork (or Classroom assignment), click `Code -> Copy URL to Clipboard`.  
2. Open a terminal and navigate to the desired folder.  
3. Clone the repository using:  
   ```bash
   git clone <repository_url>
   ```

---

#### 2️⃣ - Setup a Virtual Environment and Manage Dependencies with Poetry

Currently, the project lacks reproducibility. Let’s fix that with **Poetry**:

1. Install Poetry:  
   ```bash
   pip install poetry
   ```
2. Navigate to the repository root and check the contents:  
   ```bash
   ls
   ```
3. Initialize Poetry:  
   ```bash
   poetry init
   ```
   Follow the prompts:  
   - **Package name**: `opticaldisp`  
   - **Version**: `0.0.1`  
   - **Description**: Add a short description.  
   - **Author/License**: Press Enter to skip.  
   - **Python versions**: Enter `^3.<your_version>` (check with `python --version`).  
   - For dependencies: Enter `no` for both.

> [!TIP]
> A `pyproject.toml` file is now created with your project information.

4. Add dependencies by examining the code (e.g., `numpy`, `matplotlib`):  
   ```bash
   poetry add <package_name>
   ```
5. Verify everything works:  
   ```bash
   poetry run python main.py
   ```

> [!TIP]
> You should now see a `poetry.lock` file and generated figures.

6. Commit and push changes:  
   ```bash
   git status  
   git add .  
   git commit -m "chore: setup Poetry and dependencies"  
   git push
   ```

---

#### 3️⃣ - Restructure the Repository

Make the repository modular, following best practices:

1. **Create new files**:  
   - `waveforms.py`: Move waveform-generating functions here.  
   - `dispersion.py`: Move `apply_dispersion` function here.  
   - `optical_signals.py`: Move `OpticalSignal` class here.

2. **Organize the files**:  
   - Group all function/class files under `src/opticaldisp/`.

3. **Update imports**:  
   - Add necessary imports to each new file.  
   - In `main.py`, import from `src.opticaldisp`.

4. Test the new structure:  
   ```bash
   poetry run python main.py
   ```

> [!TIP] 
> The final repository structure should look like this:  

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
│   ├── pyproject.toml
│   ├── poetry.lock
```

5. Commit and push changes:  
   ```bash
   git status  
   git add .  
   git commit -m "chore: setup Poetry and dependencies"  
   git push
   ```

---

#### 4️⃣ - Linting and Formatting

*(Coming soon.)*

---

#### 5️⃣ - Add a LICENSE File

*(Coming soon.)*

---

#### 6️⃣ - Write Tests

*(Coming soon.)*

---

#### 7️⃣ - Check Completion and Submit

*(Coming soon.)*

---

## Contributions

### Contributors

- [David Gerard](https://github.com/David-GERARD) - PhD student @ UCL  
- [Mikulas Poul](https://github.com/mikicz) - Staff engineer @ Xelix  

> **[!TIP]**  
> - Found a bug? [Open an issue](https://github.com/UCL-Photonics-Society/TSW01-REPRODUCIBLE-OPEN-SOURCE/issues).  
> - Have ideas? *Fork* the repository, implement your changes, and submit a pull request with a changelog.

---

### Maintainers

For any questions, reach out to [David Gerard](https://github.com/David-GERARD) at david.gerard.23@ucl.ac.uk.
