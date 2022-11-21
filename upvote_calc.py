import numpy as np

def calc_reddit(v,r):
    up = int(round((((v-1)*r)+1)/((2*r)-1),1))
    down = up-v
    cr=(up+1)/((up+down)+1)
    dr=100*(r-cr)
    print(f'\t{up} upvotes + {down} downvotes: {up+down} total votes')   
    print(f'\treal upvotes + freeby: {up+1} padded upvotes')         
    print(f'\t{up+down} votes + freeby: {up+down+1} padded votes') 
    print(f'\t{(up)}/{(up+down+1)}: {int(round(100*cr,0))}% upvote rate')
    print(f'\t{round(dr,2)}% error')

def prompt_calc():
    score = int(input('What is the post score (upvotes-downvotes)?\n\t'))
    uprate = int(input('What is the post upvote rate as a percentage?\n\t'))
    calc_reddit(score,uprate/100)

prompt_calc()
