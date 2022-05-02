# network for training relations for ZxZ

'''
Outline of functions to create:

1) "auxilarly" network, used to train the other networks that serve as representations of the generators
2) a loss function for the relations of ZxZ, i.e. commutativity
3) Change to complex instead of real networks

'''

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def ZxZ_group_rep_net(a_op, b_op, input_dim):
  
  #left hand side of commutation relation
  input_tensor = Input(input_shape=(input_dim,))
  side_1 = a_op(side_1)
  side_1 = b_op(side_1)
  
  #right hand side of commutation relation
  side_2 = b_op(input_tensor)
  side_2 = a_op(side_2)
  
  output_tensor = Concatenate()([side_1, side_2])    
  both_sides_aux = Model(inputs=[input_tensor], outputs=output_tensor)
  
  return both_sides_aux

def ZxZ_group_rep_loss(input_dim):

  def loss(y_true,y_pred):
    
    # split the output relation tensor of the model 
    side_1_out=tf.slice(y_pred,[0,0],[-1,input_dim]) #all rows, first input_dim number of columns
    side_2_out=tf.slice(y_pred,[0,input_dim],[-1,input_dim]) #all rows, last input_dim number of columns 
        
    A=K.mean(math_ops.square(side_1_out - side_2_out), axis=-1)                 
    return A
    
  return loss
