letter = ''' 
        Dear <|Name|>,
        You are selected!
        <|Date|>'''
        
print(letter.replace("<|Name|>" , "Rudra").replace("<|Date|>", "24 September 2050"))
    
        