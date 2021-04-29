
#https://atrium.ai/resources/build-and-deploy-a-docker-containerized-python-machine-learning-model-on-heroku/

from  sklearn import  datasets
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3)

knn=neighbors.KNeighborsClassifier()
knn.fit(x_train,y_train)
predictions=knn.predict(x_test)
print("Accuracy = ", accuracy_score(y_test,predictions))


import pickle
with open('./model.pkl','wb') as model_pkl:
    pickle.dump(knn, model_pkl)


#sudo docker build . -t flask_two:1.0.0

#sudo docker images

#sudo docker run --rm -it flask_two:1.0.0















