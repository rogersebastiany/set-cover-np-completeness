import argparse
import set_cover


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="Show execution logs", action="store_true")
args = parser.parse_args()



U = {0, 1, 2, 3, 4, 5}                                        
S = [{0, 1}, {2, 3}, {4, 5}, {0, 1, 2, 3}]                    
k = 3                                                         

if(not args.log):
    print(set_cover.brute_force(U, S))
else:
    print("Brute force method for the set cover problem")     
    print:"Input data: \n"                                    
    print("Universe: ", U, "\n")                              
    print("Set of sub-sets of U:", S, "\n")                   
    print("Value of K:", k, "\n")                             
    print("Answer: ")                                         
    B = set_cover.brute_force(U, S)                           
    bf = 0                                                    
    for b in B:                                            
        if b == 1:
            bf += 1
    if bf<=k:                                                 
        print("Yes, sub-sets needed:", bf, B,"\n")            
    else:                                                     
        print("No.")                                         
    print("Feel free to change any input by editing main.py") 