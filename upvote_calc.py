import numpy as np

def calc_reddit(v,r):
    down = np.arange(100)
    up = np.arange(100)+v
    total = up+down
    dmin = r
    for d,u,t in zip(down,up,total):
        new_u = u+1
        new_t = t+1
        new_r = new_u/new_t
        diff_r = np.abs(r-new_r)
        if diff_r < dmin:
            dmin = diff_r
        else:
            old_u=u-1
            old_d=d-1
            old_t=t-2
            old_r=(old_u+1)/(old_t+1)
            print(f'(solved after {d} iterations)')
            print(f'\t{old_u} upvotes + {old_d} downvotes: {old_t} total votes')   
            print(f'\treal upvotes + freeby: {old_u+1} padded upvotes')         
            print(f'\t{old_t} votes + freeby: {old_t+1} padded votes') 
            print(f'\t{(old_u+1)}/{(old_t+1)}: {int(round(100*old_r,0))}% upvote rate')
            break

def prompt_calc():
    score = int(input('What is the post score (upvotes-downvotes)?\n\t'))
    uprate = int(input('What is the post upvote rate as a percentage?\n\t'))
    calc_reddit(score,uprate/100)

prompt_calc()
