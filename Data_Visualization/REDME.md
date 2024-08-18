# Project Name

## Installation

1. **Python Environment:**
   - Ensure you have Python installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Create Virtual Environment:**
   - Open a terminal or command prompt.
   - Navigate to your project directory.
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv env
     ```
     This command creates a virtual environment named "env."

3. **Activate Virtual Environment:**
   - Activate the virtual environment based on your operating system:
     - **On Windows:**
       ```bash
       .\env\Scripts\activate
       ```
     - **On macOS/Linux:**
       ```bash
       source env/bin/activate
       ```

4. **Install Dependencies:**
   - With the virtual environment activated, install project dependencies using the following command:
     ```bash
     pip install -r requirements.txt
     ```

5. **Jupyter Notebook Kernel:**
   - If you plan to use Jupyter Notebook, make sure to add the virtual environment as a kernel. Run the following command:
     ```bash
     python -m ipykernel install --user --name=env
     ```
     Replace "env" with the name of your virtual environment.

6. **Launch Jupyter Notebook:**
   - Start Jupyter Notebook by running:
     ```bash
     jupyter notebook
     ```
   - Open your notebook and select the "env" kernel from the Kernel menu.

## Project Structure

- **`/src`**: Contains the source code files.
- **`/data`**: Place data files here.
- **`/notebooks`**: Jupyter Notebooks for analysis and visualization.
- **`/docs`**: Documentation for the project.
- **`/img`**: SVG files for plots.
- **`/quarto`**: Quarto bibliography files.
- **`requirements.txt`**: List of project dependencies.

## Usage

- Run the Jupyter Notebooks climate_change_in_switzerland_en.ipynb for data analysis and visualization.

## Documentation

- The project documentation is available in the `/docs` directory.

## Contributors

- Lukas Loup

