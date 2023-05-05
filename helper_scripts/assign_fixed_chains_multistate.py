import json

def ms_assign_chains(input_path, chain_list, output_path):
    with open(input_path, 'r') as json_file:
        json_list = list(json_file)
    
    global_designed_chain_list = []
    if chain_list != '':
        global_designed_chain_list = [str(item) for item in chain_list.split()]
    my_dict = {}
    for json_str in json_list:
        result = json.loads(json_str)
        all_chain_list = [item[-1:] for item in list(result) if item[:9]=='seq_chain'] #['A','B', 'C',...]
        if len(global_designed_chain_list) > 0:
            designed_chain_list = global_designed_chain_list
        else:
            #manually specify, e.g.
            designed_chain_list = ["A"]
        fixed_chain_list = [letter for letter in all_chain_list if letter not in designed_chain_list] #fix/do not redesign these chains 
        my_dict[result['name']]= (designed_chain_list, fixed_chain_list)
    
    with open(output_path, 'w') as f:
        f.write(json.dumps(my_dict) + '\n')

# Output looks like this:
# {"5TTA": [["A"], ["B"]], "3LIS": [["A"], ["B"]]}