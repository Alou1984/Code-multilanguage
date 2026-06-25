
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier

iris = load_iris()
X = iris.data
y = iris.target
plt.plot(X)
plt.legend(iris.feature_names)
# plt.show()
X.var(axis=0)
#print(X.var(axis=0))
from sklearn.feature_selection import SelectKBest, chi2
chi2 (X,y)
print(chi2(X,y))

#selection of var where score is high ( most dependencies between X and y)
'''
selector = SelectKBest (chi2, k=2)
selector.fit_transform(X,y)
print(selector.fit_transform(X,y))
selector.get_support()
print(selector.get_support())
'''
#selection from model most important variable for estimator
'''
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import SGDClassifier
selector = SelectFromModel (SGDClassifier(random_state=0),threshold='mean')
selector.fit_transform(X,y)
print(selector.fit_transform(X,y))
print(selector.get_support())
print(selector.estimator_.coef_.mean(axis=0))
print(selector.estimator_.coef_.mean(axis=0).mean())
'''
#selection recursive elimination of less important variable in estimator (RFECV)
from sklearn.feature_selection import RFE, RFECV

selector = RFECV (SGDClassifier(random_state = 0), step =1, min_features_to_select= 2, cv=5)
selector.fit(X,y)
print('the ranking of estimator:')
print(selector.ranking_)  # ranking of score
print('the ranking of estimator:')
print(selector.grid_scores_) # Scoring for each iteration