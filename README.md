# Python GitHub Template

![Python CI](https://github.com/aghakishiyeva/ids706-python-template/actions/workflows/main.yml/badge.svg)

This is a basic Python template with CI setup using GitHub Actions. It also provides a .devcontainer setup for seamless development inside a Docker container with Visual Studio Code.

## Getting Started
### Local Development with VS Code and .devcontainer
1. Ensure you have <u>Docker</u> installed and running on your machine.<br>
2. Install the <u>Remote - Containers</u> extension in VS Code.<br>
3. Open the repository in VS Code.<br>
4. A notification will pop up suggesting you to reopen the project in a container. Click on "Reopen in Container". (Alternatively, you can press **F1**, type "Remote-Containers: Reopen Folder in Container" and press Enter.)<br>
5. The first time you do this, it might take a few minutes as Docker builds the image based on the provided **Dockerfile**.<br>
6. Once inside, you'll have a Python environment ready to go, isolated from your local machine.

   
### Running Tests
To run tests, execute the following command:

**__pytest__**

## File Structure
* main.py: Contains the primary function greet which returns a greeting message.<br>
* test_main.py: Contains the unit tests for the greet function.<br>
* requirements.txt: Lists the Python dependencies required by the project.<br>
* .devcontainer: Contains the configuration for the VS Code remote container development.<br>
* .github/workflows/main.yml: Contains the GitHub Actions workflow for Continuous Integration.<br>

## Contributing
1. Fork the repository. <br>
2. Create a new branch for your changes. <br>
3. Make your changes. <br>
4. Run tests to ensure your changes do not introduce bugs. <br>
5. Submit a pull request.<br>

_ _This README is organized to give an overview of the project, guide on how to use the **.devcontainer**, detail how to run tests, and provide a brief on how to contribute. You can expand upon or modify any sections as per your project's requirements._ _
