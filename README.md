# DeepFoodie

Deep Learning Systems Project Files



# Guidelines to create all dataset files

* each dataset image in different directory with naming convention: dataset_{id}_images
* each dataset csv a different csv with columns: = ['Title','Instructions','Image_Name','Cleaned_Ingredients','dataset','id']
* each csv name: cleaned_dataset_{id}.csv

* dataset URL: https://www.kaggle.com/alphadraco/deepfoodie


# Description of each column
* Title: lower cased, no special characters
* Instructions: lower cased, no word numbers
* Cleaned_Ingredients: only words no numbers, probably from a many to one dictionary


# model architectures to try out
* Resnet50, EfficientNet
* Different embeddings: Glove, embeddings from food datasets, 1M+ embeddings
* Prediction Ranker

