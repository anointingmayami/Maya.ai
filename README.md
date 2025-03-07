# Maya.ai - AI Architectural Framework

Maya.ai is an AI architectural framework designed to ensure ethical, optimized, and compliant AI integration in business and research applications. The framework provides guidance on AI ethics, compliance, business strategy, and AI-driven education while fostering innovation.

## 🌟 Features
- Ensures structured AI project development
- Promotes ethical and compliant AI integration
- Provides a scalable framework for AI research and business applications
- Includes Maya CLI for quick AI project setup

## 🆕 New Release Features
Maya CLI has been updated with new features to enhance AI project development. The latest version introduces:
- **Enhanced Project Templates**: More predefined templates for diverse AI applications.
- **Versioning Support**: Track and manage different versions of AI projects.
- **Improved Compliance Checks**: Automatic compliance validation for ethical AI development.
- **Extended API Integrations**: Seamless connection with external AI services.

### 🔗 Read the Full Documentation
For a detailed breakdown of the new features and CLI commands, check out our official documentation:
[View Documentation](https://github.com/anointingmayami/Maya.ai/blob/main/maya_cli/README.md)

## 🛠 Maya CLI - AI Project Generator
Maya CLI is one of the core features of Maya.ai, designed to generate structured AI project templates. It helps AI developers quickly set up their projects with predefined folders and files, ensuring organization and scalability.

### 📦 Installation Guide (For Dummies)

#### Step 1: Install Python
Maya CLI requires Python. To install Python:
- Download the latest version of Python from [python.org](https://www.python.org/downloads/)
- Run the installer and ensure "Add Python to PATH" is checked
- Verify installation by running:
  ```sh
  python --version
  ```

#### Step 2: Install Virtual Environment (Optional but Recommended)
Using a virtual environment helps manage dependencies. Install it using:
```sh
pip install virtualenv
```
To create and activate a virtual environment:
```sh
virtualenv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

#### Step 3: Install Maya CLI
Maya CLI is available on PyPI. Install it using pip:
```sh
pip install maya-cli
```

### 🚀 Usage
Once installed, use the following command to create a new AI project:
```sh
maya create <project_name>
```
Example:
```sh
maya create my_ai_project
```
This will generate the following structure:
```
my_ai_project/
│── data_source/
│   ├── ingestion/
│   ├── processing/
│   ├── storage/
│── knowledge_base/
│   ├── models/
│   ├── training/
│   ├── evaluation/
│── ai_governance/
│   ├── compliance/
│   ├── fairness/
│   ├── monitoring/
│── api/
│   ├── endpoints/
│   ├── authentication/
│── tests/
│── docs/
│── scripts/
│── configs/
```

# Quick Guide to Getting Started with Maya AI

## Step 1: Installation and Setup Development Environment
To begin using Maya AI, you need to set up your development environment. Follow these steps:

1. Ensure you have Python installed (preferably Python 3.8+).
2. Install the required dependencies using pip:
   ```sh
   pip install click python-dotenv openai
   ```
3. Clone the Maya AI repository (if applicable) or set up your project directory.

## Step 2: Set Up OpenAI Key in Environment Variables
To integrate OpenAI services, you must configure your API key in an `.env` file:

1. Create a `.env` file in your project directory.
2. Use the `set_env` command to store your OpenAI API key:
   ```sh
   maya set-env OPENAI_API_KEY your_api_key_here
   ```
   This command will securely save your key in the `.env` file.

## Step 3: Create a Maya AI Project
Once the environment is set up, you can create a new AI project using the Maya CLI:

1. Run the following command to create a new project:
   ```sh
   maya create your_project_name
   ```
2. This will generate the necessary project structure for your AI application.
3. Navigate into your project directory and start developing.


### 🛠 API Documentation
#### CLI Commands
##### `maya create <project_name>`
Creates a new AI project structure with organized folders.

#### `project_generator.py`
##### `create_project_structure(base_path, structure)`
Recursively creates folders based on the defined project structure.

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📞 Support
For any issues, contact the developers via GitHub or raise an issue in the repository.

