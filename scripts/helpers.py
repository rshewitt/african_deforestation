import json 

def json_2_dict( in_file ):

    output = None 
    
    with open( in_file ) as f:
        output = json.load( f ) 
    
    return output 