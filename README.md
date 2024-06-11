BCP, LLC - Real Estate Price Prediction

This project, developed by BCP, LLC, aims to predict real estate prices in Florida using machine learning and a user-friendly web interface. It empowers users to make informed decisions through data-driven insights.

Project Structure

Project Overview: Introduces the project's goals and functionalities.

Technical Aspects: Details the technologies used for data collection, analysis, modeling, and visualization.

User Interface: Describes the user-friendly interface for interacting with the prediction model (if applicable).

Tableau Dashboard: Discusses the interactive visualization tool built with Tableau. Users can explore the dashboard at: https://public.tableau.com/app/profile/brennan.bradley/viz/Project_4_Dash/MainDashboard

Ethical Considerations: Addresses the ethical implications of using machine learning for real estate prediction.
Disclosures, References, and More: Provides information on data sources, libraries, and other relevant details.

Thanks: Acknowledges contributors and resources used in the project.

Data Source
The real estate dataset for Florida was obtained from Kaggle (link to Kaggle dataset - https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset/data), a reputable platform for data exploration and analysis.

Technologies Used

Front-End:
HTML, CSS, JavaScript
Tableau

Back-End:
Python
Libraries:
pandas (data manipulation)
matplotlib (data visualization)
numpy (numerical computations)
scikit-learn (machine learning)
SQLAlchemy (database interaction)
sqlite3 (database management)

Application:
Python Flask server (server.py, util.py)
Usage Instructions

Installation:
The project requires Python libraries like pandas, matplotlib, numpy, scikit-learn, and SQLAlchemy. Install them using pip install pandas matplotlib numpy scikit-learn sqlalchemy sqlite3 flask.
Tableau Desktop for the visualization component.

Data Setup:
Download the real estate dataset for Florida from Kaggle (link to Kaggle dataset).
Ensure the data is compatible with pandas (e.g., CSV format).

Data Preprocessing:
This may involve handling missing values, correcting inconsistencies, and creating new features.

Model Training (real_estate_model_build.ipynb):
The real_estate_model_build.ipynb script allows users to modify parameters like features, model selection, and hyperparameter tuning.
Run python real_estate_model_build.ipynb to train the machine learning model.

Model Evaluation:
Analyze the results and consider improvements if necessary.

Web Interface:

Tableau Dashboard:
Explore the interactive Tableau dashboard at link (https://public.tableau.com/app/profile/brennan.bradley/viz/Project_4_Dash/MainDashboard) to gain further insights into the data and model predictions.
