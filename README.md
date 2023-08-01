# N-Tier-Architecture Flask App for Kidney Disease Detection/Prediction

This repository contains a Flask web application built using N-tier architecture to detect/predict kidney disease using machine learning models. The N-tier architecture is a software design pattern that divides the application into multiple layers, each serving a specific role. This design pattern enhances modularity, maintainability, scalability, and reusability of the software, making it more flexible and easier to manage.

## N-Tier Architecture Overview

The N-tier architecture used in this Flask app consists of three tiers, each with its specific responsibilities:

1. **Presentation Tier (or User Interface Tier)**:

   - This topmost layer interacts directly with users, handling user input and displaying information.
   - For this Flask app, the presentation tier is implemented using HTML, CSS, JavaScript, and Flask's templating engine.

2. **Application Tier (or Business Logic Tier)**:

   - The application tier contains the business logic of the kidney disease detection/prediction application.
   - It processes user input, performs computations, and coordinates the application's workflow.
   - In this Flask app, the application tier is implemented using Python and Flask.

3. **Data Tier (or Data Access Tier)**:
   - The data tier is responsible for managing data storage and retrieval.
   - It handles accessing and manipulating data from various data sources, such as databases, file systems, or external APIs.
   - The data tier abstracts the complexities of data storage, allowing other tiers to interact with data without needing to know the underlying storage details.

Additional tiers, such as a service tier or integration tier, could be added to handle specific functionalities like external service integration or data synchronization if required.

## Setting Up the Flask App

To set up the Flask app locally, follow these steps:

1. **Clone the Repository**:
   Clone this repository to your local machine using `git clone`.

2. **Create a Virtual Environment**:
   Navigate to the cloned repository's directory and create a virtual environment named 'flaskenv'. Use the following command for virtual environment creation:

   ```bash
   python -m venv flaskenv
   ```

3. **Activate the Virtual Environment**:
   On Windows, activate the virtual environment using:

   ```bash
   flaskenv\Scripts\activate
   ```

   On macOS or Linux, activate the virtual environment using:

   ```bash
   source flaskenv/bin/activate
   ```

4. **Install Dependencies**:
   Install the required Python dependencies by running the following command:

   ```bash
   pip install flask
   ```

5. **Run the Flask App**:
   Start the Flask app using the following command:

   ```bash
   flask run
   ```

   The app will be accessible at `http://127.0.0.1:5000/`.

## Machine Learning Notebook and Models

This repository also contains a Jupyter Notebook (`ipynb` file) that includes the machine learning code used to train the kidney disease detection/prediction models. The trained models are located in the `models` directory.

## Note

The application only accepts input in the precise format as it is found in the dataset used to train the models. Ensure that you provide input data in the correct format for accurate predictions.

The Flask app, along with the machine learning models, can be further extended and customized to suit your specific use case or integrated into larger applications following the N-tier architecture principles.
