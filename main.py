'''
File to run that prompts choice of parameters.
'''

'''
Outline:
need python agrument parsing
    might want something that allows for options without having to go through option each time
    defaults, etc.
this will run the appropriate file for training or testing the network under the group/parameter choices

    # mode : testing or training
    
    # type of structure. Options : TL, braid_group, symmetric_group, ZxZ

    # type of rep. Types are : linear, affine, nonlinear. Activation + bias determine the type.
    
    #(1) dim of the rep
    parser.add_argument('-dim', '--generator_dimension',type=int,default=2,help='domain dimension of the gen network.')

    #(2) determines the type of the of the rep: non-linear, affine or linear? 
*For non-linear, should we turn on Bias always, never, choice between?
*affine -> linear activation with Bias turned on
*linear -> linear activation with Bias turned off

    # training arguments:
    
    #(1) number of epochs   
   
    #(2) learning rate   

    #(3) batchsize
'''

mode = input("Choose between training or testing")
if mode not in {'training', 'testing'}:
    print('Error')
    # add exception
structure = input("Choose between structures: ZxZ_group")
    # add exception
dim = int(input("What dimension should the representation be?"))
    # add exception
options = input("Add additional options, yes or no?"):
activation = 'linear'
bias = 'False'
epoch = 2
learningrate = 0.002
batchsize = 2000
if options == "yes":
    activation = 'linear'
        # add exception
    bias = 'False'
        # add exception
    epoch = 2
        # add exception
    learningrate = 0.002
        # add exception
    batchsize = 2000   
        # add exception

if structure == "ZxZ_group":
    # outline functions needed from utilities and from ZxZ file
        # such as "get_n_operators" function, "ZxZ_group_rep_net" function, "train_net" function, "ZxZ_group_rep_loss" function, "get_relation_tensor" function
    # outline procedure on the use of these functions


    
    
    
