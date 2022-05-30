"""
1. Create an auxiliary network to train the network representations of the three generators E, F, H on the commutator relations.
    *We will have three bracket/commutation equations to train on.
    *From these we have 6 sides of equations, that come in pairs.
    *The auxillary network has 6 parts to it; 6*input dim is the shape of the output. Each side of an equation gives one part of the network.
2. Create the loss function for the purpose of training the networks on these commutator relations.
    *We will train on difference/take the loss between paired sides.
    *The total loss will be the sum of the three losses, one from each equation.
3. Eventually have the networks over the Complex numbers rather than Reals.
"""
