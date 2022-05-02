'''
utility functions for network creation and training
'''

'''
functions to create:

1) creates a network that serves as a representation of a group generator
2) creates a multiple of networks for each generator of the group using (1)
3) train the network on the relations of the group *
    * confusion about how the group relations are being used for network loss here
4) gives the error on satisfying the relation of the group

'''

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layer
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.layers import Lambda
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Concatenate


def generator(input_dim, activation_func, bias):
   
   """
   Purpose: 
      This is a network that can used to represent element/generator in a given representation.
   """
   
   model = keras.Sequential(
      [
      layers.Dense(2*input_dim+2, use_bias=bias, activation=activation_func, input_shape=[input_dim]),
      layers.Dense(2*input_dim+2, use_bias=bias, activation=activation_func),
      layers.Dense(100, use_bias=bias, activation=activation_func),
      layers.Dense(50, use_bias=bias, activation=activation_func),
      layers.Dense(input_dim)
      ])
   
   return model


def get_n_generators(input_dim, activation_func, bias, n_of_generators):
   """
   Purpose:
      Helper function to create all the needed generators in a list for a given presentation of an algebraic object.
   """
   
   list_of_gen = [ generator(input_dim, activation_func, bias) for i in range(0, n_of_generators)]
   
   return list_of_gen
   
   
def train_net(model,x_data,y_data,model_name,lossfunction,lr,batch_size,epochs):
    
    """
    Taken from Mustafa
    Parameters: 
    ----------            
        model : keras model
        x_data : training X data
        y_data : training Y data
        model_name : name of the file where the model is going to be saved.
        lr: learning rate
        batch_size : batch size
        epochs : number of epochs
    
    """     
    
    checkpoint = ModelCheckpoint(model_name, monitor='loss', verbose=1, save_best_only=True, mode='min')
    
    callbacks_list = [checkpoint]   
    
    model.compile(optimizer=keras.optimizers.Adam(lr=lr), loss = lossfunction  )           
    
    model.fit(x_data, y_data,  batch_size=batch_size, epochs=epochs, shuffle = True,  verbose=1,callbacks_list=callbacks_list)  
    
    return 
    
def get_relation_tensor(modelpath,model,data):
    
    """
    Taken from Mustafa
    Parameters:
    ----------    
        modelpath: folder where the model weights are located.
        model : keras model
        data : the data that we want to infer the model on.
    Returns:
    -------    
        the prediction of the input model on the input data.
            
    """
    
    model.load_weights(modelpath)

    return model.predict(data)
   
