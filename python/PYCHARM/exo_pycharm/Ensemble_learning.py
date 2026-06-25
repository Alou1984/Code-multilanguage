
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
X, y = make_moons(n_samples = 500, noise = 0.3, random_state=0)
plt.scatter(X[:,0], X[:,1], c=y)
#plt.show()

# train an test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3,random_state=0 )

# Definition of model
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

model_1 = SGDClassifier(random_state=0)
model_2 = DecisionTreeClassifier (random_state=0)
model_3 = KNeighborsClassifier(n_neighbors=2)
model_4 = VotingClassifier( [('SGD', model_1),
                             ('Tree', model_2),
                             ('KNN', model_3)],
                            voting='hard')
'''
for model in (model_1, model_2, model_3, model_4):
     model.fit(X_train, y_train)
     print(model.__class__.__name__, model.score(X_test,y_test))
'''
'''
bagging:
bagging(et la random forest) permet d'obtenir des ensemble de modèles
diversifiés en entraînant chaque modèle sur une portion aléatoire
 des données (en échantillonnant le dataset avec le Bootstrapping)
'''
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
'''
model = BaggingClassifier(estimator= KNeighborsClassifier(),
                         n_estimators=100)
model.fit(X_train, y_train)
model.score(X_test, y_test)
print(model.score(X_test, y_test))
'''
#Boosting:
'''
Le Boosting permet quant à lui de construire des modèles les uns après
les autres, en demandant à chaque modèle de corriger les erreurs de son
prédécesseur. (Adaboost et GradientBoosting sont des exemples d'algorithmes)
'''
from sklearn.ensemble import  RandomForestClassifier
''''
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
model.score(X_test, y_test)
model.fit(X_train, y_train)

'''
# addBoosting
'''
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier
model = AdaBoostClassifier( n_estimators=100)
model.fit(X_train, y_train)
model.score(X_test, y_test)
print(model.score(X_test, y_test))
'''

#staking:
'''
Le Stacking permet d’entraîner un modèle de machine learning a reconnaître
qui a tort et qui a raison dans un ensemble de modèles, ce qui améliore encore
plus la performance générale
'''
from sklearn.ensemble import StackingClassifier

model5 = StackingClassifier( [('SGD', model_1),
                             ('Tree', model_2),
                             ('KNN', model_3)],
                            final_estimator= KNeighborsClassifier())
model.fit(X_train, y_train)
model.score(X_test, y_test)
print(model.score(X_test, y_test))
