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

# one possible option if we can't figure out arg parsing with input splitting
# which ranges (if at all) for int/float inputs?
# add break for testing mode
# should probably make this a function in utilities or something

# mode
while True:
    mode = input("Choose mode (training, testing): ")
    if mode not in ["training", "testing"]:
        print("Must choose training or testing.")
        continue
    else:
        break

# structure
while True:
    structure = input("Choose structure (ZxZ_group): ")
    if structure not in ["ZxZ_group"]:
        print("Must choose ZxZ_group")
        continue
    else:
        break

# dimension
while True:
    try:
        dim = int(input("Choose dimension (integer between 1 and 10): "))
    except ValueError:
        print("Must choose integer between 1 and 10.")
        continue
    if dim not in range(1, 11):
        print("Must choose integer between 1 and 10.")
        continue
    else:
        break

# optional arguments
while True:
    options = input("Would you like to input optional arguments? (yes or no): ")
    if options not in ["yes", "no"]:
        print("Must choose yes or no.")
        continue
    elif options == "yes":

        # activation
        while True:
            activation = input("Choose activation type (linear, affine, nonlinear): ")
            if activation not in ["linear", "affine", "nonlinear"]:
                print("Must choose linear, affine, or nonlinear.")
                continue
            else:
                if activation == "linear":
                    bias = False
                elif activation == "affine":
                    bias = True
                else:
                    while True:
                        bias = input("Would you like to add bias? (yes or no): ")
                        if bias == "yes":
                            bias = True
                        elif bias == "no":
                            bias = False
                        else:
                            print("Must choose yes or no.")
                            continue
                        break
                break

        # number of epochs
        while True:
            try:
                epoch = int(input("Choose number of epochs (integer between 1 and 10): "))
            except ValueError:
                print("Must choose integer between 1 and 10.")
                continue
            if epoch not in range(1, 11):
                print("Must choose integer between 1 and 10.")
                continue
            else:
                break

        # learning rate    
        while True:
            try:
                lr = float(input("Choose learning rate (between 0 and 1): "))
            except ValueError:
                print("Must choose value between 0 and 1.")
                continue
            if not (0 <= lr <= 1):
                print("Must choose value between 0 and 1.")
                continue
            else:
                break

        # batch size    
        while True:
            try:
                batch_size = int(input("Choose batch size (integer between 100 and 10000): "))
            except ValueError:
                print("Must choose integer between 100 and 10000.")
                continue
            if batch_size not in range(100, 10001):
                print("Must choose integer between 100 and 10000.")
                continue
            else:
                break
        break

    # default optional arguments        
    else:
        activation = "linear"
        bias = False
        epoch = 2
        lr = 0.002
        batch_size = 2000
        break

if structure == "ZxZ_group":
    # outline functions needed from utilities and from ZxZ file
        # such as "get_n_operators" function, "ZxZ_group_rep_net" function, "train_net" function, "ZxZ_group_rep_loss" function, "get_relation_tensor" function
    # outline procedure on the use of these functions


    
    
    
