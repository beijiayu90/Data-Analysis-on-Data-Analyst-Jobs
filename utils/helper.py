import re

def process_revenue(revenue_string):
    
    contains_billion = False
    contains_million = False
    is_max = False
    is_min = False
    
    if re.search('billion', revenue_string):
        contains_billion = True
    if re.search('million', revenue_string):
        contains_million = True
    if re.search(r'\+', revenue_string):
        is_min = True
    if re.search('Less', revenue_string):
        is_max = True
        
    splitted = [string.strip() for string in revenue_string.split('to')]
    
    tmp_string = ' '.join(splitted)
    
    splitted = re.split(r'[m|b]illion|\+|Less than', tmp_string)
    
    splitted = [int(item) for item in ' '.join(splitted).split()]
    
    max_revenue = None
    min_revenue = None
    
    if is_max:
        max_revenue = splitted[0]
    elif is_min:
        min_revenue = splitted[0]
    else:
        min_revenue, max_revenue = splitted
        

    if contains_billion and max_revenue != None:
        max_revenue = max_revenue * 1000
    if not contains_million:
        min_revenue = min_revenue * 1000
        
    return min_revenue, max_revenue