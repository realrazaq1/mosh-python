# machine learning is sub section of AI(artificial intelligence). it's one of the trending topics this days and its going to have a lot of applications in the future
# example: write a program to scan an image to tell if it's a cat or a dog

# How Machine Learning works
# - we build a model or an engine and give it lots of data. example, we give tens of thousands of pictures of cats and dogs
# - the model will then find and learn patterns in the input data, so we can give a new picture of a cat it hasn't seen before and ask if it's a cat or dog or a horse and it will tell us with certain level of accuracy. the more input data we give it, the more accurate our model is going to be.

# Machine learning has other applications in;
# - Self-driving Cars
# - Robotics
# - Language Processing
# - Vision Processing
# - Forecasting Stock Market Trends, Weather, Games, etc

# Machine learning project involves a number of steps

# 1. Import the data: the first step is to import our data which often comes in a form of csv file. you can have a database with lots of data, we can simply export that data and store in a csv file for the purpose of our machine learning project

# 2. Clean the data: this involves task such as removing duplicate data. if we have duplicate data, we don't want to feed it to our model otherwise our model will learn bad pattern in the data, and it will produce the wrong result. we should make sure that our input data is in a good and clean shape, if there are data that is irrelevant, we should remove them, if there are duplicate or incomplete, we can remove or modify them. if our data is text based like the name of countries or journal of music or cats and dogs, we need to convert them to numerical values. this step really depends on the kind of data we are working with. every project is different

# 3. Split the Data into Training/Test Sets: now that we have clean dataset, we need to split it into two segments; one for training our model and the other for testing it to make sure that our model produces the right result. For example if you have 1,000 pictures of cats and dogs, we can reserve %80 for training and the other %20 for testing

# 4. Create a Model: this involves selecting an algorithm to analyze the data. there are so many machine learning algorithm out there such as Decisions Tree, Neural Networks and so on. each algorithm has pros and cos in terms of accuracy and performance. the algorithm you choose depends on the kind of problem you are trying to solve and your input data. the good news is that we don't have explicitly program an algorithm. there are libraries out there that provides this algorithms, one of the most popular ones is SciKitLearn

# 5. Train the Model: next we need to train our model. we feed in our training data. our model will then look for patterns in the data

# 6. Make Predictions: next we can ask it to make predictions. we can ask is it a cat or a dog and our model will make a prediction. the prediction is not always accurate. it's very likely that your predictions are inaccurate

# 7. Evaluate and Improve: we need to measure the predictions and evaluate their accuracy. then we need to get back to our model and either select a different algorithm that is going to produce a more accurate result for the kind of problem we are trying to solve or finetune the parameters of our model. each algorithm has parameters we can modify to optimize the accuracy

# ====== Libraries & Tools for ML =======

# 1. Numpy: provides multi-dimensional array

# 2. Pandas: data analysis library that provides a concept called data frame. a data frame is a 2-dimensional data structure similar to an Excel spreadsheet. we have rows and columns, we can select data in a row or column or range of rows and columns. very popular in machine learning and daa science projects

# 3. MatPlotLib: 2-dimensional plotting library for creating graphs and plots

# 4. Scikit-Learn: provides common machine learning algorithms like Decision Trees, Neural Networks and so on

# === ENVIRONMENT ===
# When working with machine learning projects, we use an environment called Jupyter Notebook to write our code. technically we can still use vscode or any other code editor but these editors are not ideal for machine learning projects, because we frequently need inspect the data and that is hard in environments like vscode and terminal. it makes it really easy to inspect our data

# To install Jupyter we use an environment called Anaconda. go to anaconda.com/download and download it for your OS

