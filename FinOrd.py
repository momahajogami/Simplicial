

# I want to show how one builds Categories out
# of Categories by providing Simplicial Sets, 
class FinOrd:

    # Create a map in FinOrd.

    # The data for such
    # a map is the domain and codomain sizes
    # and a non-decreading list of integers of
    # length equal to the size of the domain
    # and containing no integers greater than
    # the size of the codomain minus one. 
    
    def __init__(self, domain_size, codomain_size, data):
        self.id = config.generate_id

    def compose(self, other):
        
        
        
# Maybe a simplicial set is a list of these
# things. 
