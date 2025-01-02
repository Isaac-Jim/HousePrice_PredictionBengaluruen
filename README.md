

# Bengaluruen Home Price Prediction Project  
Are you curious about how data can be leveraged to predict real-world outcomes like home prices? This project takes you on a journey through the entire lifecycle of a machine learning project, from raw data to a fully functioning web application.

Using real-world housing data from Bengaluruen, I built a machine learning model to predict home prices based on user inputs like square footage, number of bedrooms, and location. The project combines the power of data science, machine learning, and web development into a seamless solution that demonstrates practical applications of predictive analytics.

This end-to-end project covers everything from data preprocessing and model training to deploying the solution through a Python Flask server and an intuitive web interface. It’s not just a tool for predicting prices but also a showcase of the step-by-step process behind crafting data-driven solutions.


## Project Overview  

This project integrates three key components:  

1. **Machine Learning Model**:  
   A predictive model was trained using the Bengaluruen Home Prices Dataset from Kaggle. After comparing algorithms like Linear Regression, Random Forest, and XGBoost, XGBoost delivered the best results, achieving **92% accuracy**. The model’s hyperparameters were optimized using **GridSearchCV**, and its performance was validated through **k-fold cross-validation**.  

2. **Python Flask API**:  
   A lightweight Flask server was implemented to host the trained model, allowing it to process user inputs and return predictions dynamically via HTTP requests.  

3. **Interactive Web Interface**:  
   A responsive frontend was developed using HTML, CSS, and JavaScript, providing users with an intuitive platform to input home details and receive real-time price predictions.  



## Key Features  

- **Comprehensive Workflow**:  
  - Data cleaning,handling missing values, outlier detection, and removal.  
  - Feature engineering and dimensionality reduction.  
  - Hyperparameter tuning with **GridSearchCV**.  
  - Evaluation through **k-fold cross-validation**.  

- **Model Comparison and Selection**:  
  - Multiple algorithms were compared, with XGBoost outperforming Linear Regression and Random Forest in both accuracy and robustness.  

- **End-to-End Solution**:  
  - Seamless integration of backend and frontend components ensures a user-friendly experience.  



## Technologies and Tools  

- **Python**: Core programming language for data preprocessing, model training, and backend development.  
- **Numpy** and **Pandas**: For data manipulation and analysis.  
- **Matplotlib**: For exploratory data visualization.  
- **Scikit-learn**: For building, optimizing, and evaluating the machine learning model.  
- **XGBoost**: Final model for price prediction.  
- **Flask**: Backend server for hosting the model API.  
- **HTML, CSS, and JavaScript**: Frontend technologies for building the user interface.  
- **Jupyter Notebook**: For prototyping and experimentation.  

---

## How It Works  

1. **Data Preprocessing**:  
   The dataset was prepared by cleaning missing values, removing outliers, and engineering relevant features to improve model performance.  

2. **Model Training**:  
   After testing various algorithms, XGBoost was selected for its high accuracy and efficiency. Hyperparameters were fine-tuned using GridSearchCV, and the model was validated with k-fold cross-validation for reliability.  

3. **API Development**:  
   A Flask API was created to serve the trained model. It processes user inputs (e.g., square footage, bedrooms) and returns predicted prices in real time.  

4. **Frontend Integration**:  
   The website allows users to input property details via an interactive form. These inputs are sent to the Flask API, which returns the predicted home price for display.  

---

## Installation  

### Prerequisites  
- Python 3.x  
- Jupyter Notebook  
- Flask  

### Setup Instructions  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/Isaac-Jim/HousePrice_PredictionBengaluruen.git  
   cd HousePrice_PredictionBengaluruen  

   ```  

2. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the Flask server:  
   ```bash  
   python server.py  
   ```  

4. Access the web application in your browser:  
   `http://127.0.0.1:5000/`  



## Results  

- **Model Accuracy**: The XGBoost model achieved **92% accuracy**, outperforming Linear Regression and Random Forest models.  
- **Comparison**: XGBoost demonstrated superior handling of complex feature interactions and outliers compared to other algorithms.  



## Future Improvements  

 **Deployment**: The next step is to deploy the web application to **AWS**, making it accessible to users online.  

