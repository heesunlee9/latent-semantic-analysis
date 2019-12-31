from flask import Flask, render_template
import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition  import LatentDirichletAllocation

app = Flask(__name__) 

@app.route('/') 
def hello_world():
    my_docs = ["The global warming is becoming more severe",
           "The movie was simply awesome",
           "I like South Asian food",
           "Samsung is announcing a new technology",
           "Machine Learning is an example of awesome technology",
           "All of us were excited at the movie",
           "We have to do more to reverse the global warming"]

    my_docs = [x.lower() for x in my_docs]

    vectorizer = CountVectorizer(max_features = 15, min_df = 1, max_df = 3, stop_words = ENGLISH_STOP_WORDS)
    X = vectorizer.fit_transform(my_docs).toarray() 
    print(X)
    print(X.shape)

    features = vectorizer.get_feature_names()
    print(features)
    print(len(features))

    n_topics = 3
    lda = LatentDirichletAllocation(n_components=n_topics)
    my_docs_topic = lda.fit_transform(X)  
    print(my_docs_topic)
    my_docs_topic.sum(axis=1)

    topic_composition = lda.components_
    print(topic_composition.shape)

    n_top = 3
    for i in range(n_topics):
        topic_features = [features[idx] for idx in np.argsort(-topic_composition[i,:])]   # argsort는 소 -> 대의 순서로 정렬.
        topic_features_top = topic_features[0:n_top]
        if i == 0:
            topic_matrix = [topic_features_top]                
        else:
            topic_matrix.append(topic_features_top)
    print(topic_matrix)

    topic_names = ['Technology', 'Movie + Cuisine', 'Environment']

    n_docs = len(my_docs)
    results = []
    for i in range(n_docs):
        topic_pick = np.argmax(my_docs_topic[i,:])
        print("Document " + str(i+1) + " = " + topic_names[topic_pick])
        results.append("Document " + str(i+1) + " = " + topic_names[topic_pick])

    return render_template('results.html', topic_names=topic_names, my_docs=my_docs, results=results)
    
if __name__ == '__main__': 
    app.debug = True 
    app.run()
