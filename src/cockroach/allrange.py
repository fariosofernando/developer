"""
Modulo responsavel por manipulação de dados semelhante ao função range, 
só que de uma forma mais expansiva. 
"""

#// List of which the user will receive at the end.
elements = list()

def allrange(start, end, forElements, step = 0):
    """ This function was not made to substitude the range function(), but rather to increase
    the functionality of being able to apply range in lists. Be it a list generated by the range itself()
    or a list defined by the programmer."""
    
    if step != 0:
        immutablestep = step+1
      
        for element in forElements:

            #// Capturing the index of the element.
            index = forElements.index(element)

            #// Taking the step.
            if index == step:

                #// Incrementing the step, so that it executes the next jump.
                step = step+immutablestep

            #// If it fails then it will happen normally with the checks below.
            else:
                if index >= start -1:
                    elements.append(element)
                    if index == end -1:
                        break
             
        #//Returning the generated list after it is handled and created.
        return elements

    if step == 0:
        for element in forElements:

            #// Capturing the index of the element.
            index = forElements.index(element)

            """ If it is equal to the start value, it will print.But that's just to define the beginning of our 
            Range. And basically if it's the end, it makes a break in the. """
            if index >= start -1:
                elements.append(element)
                if index == end -1:
                    break
        
        #//Returning the generated list after it is handled and created.
        return elements