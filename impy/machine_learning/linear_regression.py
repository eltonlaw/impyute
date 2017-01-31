import numpy as np
import tensorflow as tf

class LinearRegression:
    def __init__(self,epochs_n=100):
        self.type = "LinearRegression" 
        self.epochs_n = epochs_n
    def train(self,X,Y):
        weights = tf.Variable(tf.random_uniform(tf.shape(X)[1],name="weights"))
        y_pred = tf.matmul(X,weights)
        sq_error = tf.square(y-y_pred)
        
        training_op = tf.train.GradientDescentOptimizer(0.01).minimize(sq_error)

        with tf.Session() as sess:
            tf.global_variabls.initializer().run()
            for i in range(epochs_n):
                for x_i,y_i in zip(X,Y):
                    sess.run(training_op,feed_dict={X:x_i,Y:y_i})
        self.weights = weights
    def predict(self,X):
        y_pred = tf.matmul(X,self.weights)
        with tf.Session() as sess:
            out = sess.run(y_pred,feed_dict={X:X})
        return output

