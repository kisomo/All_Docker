
#https://www.youtube.com/watch?v=oCaoMuY9Vjo

#https://www.youtube.com/watch?v=7-7p6WuDtbs

#https://atrium.ai/resources/build-and-deploy-a-docker-containerized-python-machine-learning-model-on-heroku/

#https://www.jitsejan.com/creating-model-as-a-service.html

import nltk 
nltk.download('stopwords')

from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

set(stopwords.words('english'))
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/',methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    text1 = request.form['text1'].lower()
    text2 = request.form['text2'].lower()
    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])
    processed_doc2 = ' '.join([word2 for word2 in text2.split() if word2 not in stop_words])
    corpus = [processed_doc1, processed_doc2]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    similarity_matrix = cosine_similarity(tfidf)[0,1]
    return render_template('form.html',final=similarity_matrix,text1=text1,text2=text2)

if __name__ == "__main__":
    app.run(debug = True, host="127.0.0.1",port=5002,threaded=True)


#sudo docker build . -t flask_one:1.0.0

#sudo docker images

#sudo docker run --rm -it flask_one:1.0.0










