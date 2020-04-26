from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from sklearn.linear_model import LogisticRegression
from keras.models import Sequential,Model,load_model
from keras.layers import Dense,Activation,Input
from keras.utils import np_utils

def recommend(data):

    inp = Input(shape=(10,))
    h1 = Dense(16)(inp)
    h2 = Dense(16)(h1)
    h3 = Dense(16)(h2)
    h4 = Dense(16)(h3)
    h5 = Dense(1)(h4)
    out = Activation('elu')(h5)
    model = Model(inputs=inp,outputs=out)
    model.summary()
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    