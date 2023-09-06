# Python GitHub Template

![Python CI](https://github.com/aghakishiyeva/ids706-mini-project-1/actions/workflows/main.yml/badge.svg)

This is a basic Python template with CI setup using GitHub Actions. It also provides a **.devcontainer** setup for seamless development inside a Docker container with Visual Studio Code..

## 🚀 Getting Started
### Local Development with VS Code and .devcontainer
1. Ensure you have **Docker** installed and running on your machine.
2. Install the **Remote - Containers** extension in VS Code.
3. Clone the repository onto your local machine.
4. Open the repository in VS Code.
5. A notification will pop up suggesting you reopen the project in a container. Click on "Reopen in Container". (Alternatively, you can press **F1**, type "Remote-Containers: Reopen Folder in Container", and press Enter.)
6. The first time you do this, Docker will build an image based on the provided **Dockerfile**. This may take a few minutes.
7. Once inside the container, you'll have a ready-to-use Python environment, isolated from your local system.

### 🧪 Running Tests

To run tests in this project, use the following command:

```bash
pytest
```

This command runs all the unit tests and ensures that any changes made haven't introduced new issues.

## 🛠️ File Structure
* src/main.py: Contains the primary function greet which returns a greeting message.
* tests/test_main.py: Holds unit tests for the greet function.
* requirements.txt: Specifies the Python dependencies required for this project.
* .devcontainer: Configurations for the VS Code remote container development environment.
* .github/workflows/main.yml: Workflow definitions for Continuous Integration using GitHub Actions.

## ✨ Contributing
1. Fork the repository.<br>
2. Create a new branch for your contributions.<br>
3. Implement your changes.<br>
4. Run tests using pytest to ensure no new bugs have been introduced.<br>
5. Submit a pull request detailing your changes.

*_This README provides an overview of the project, guides on the .devcontainer usage, instructions on running tests, file structure and outlines the contribution process. Modify or expand sections as needed for your project's specific requirements._*


