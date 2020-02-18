#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yaml Interpreter -> Python Model 

Created on Fri Feb  7 15:59:02 2020

@author: jacobalexander

Take in a Yaml datamodel, 
create a file of definitions for the 
"""
import yaml 
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce

#%% take in the DataModels

def read_yaml(filename):
    with open(filename) as f: 
        content = yaml.load(f)
    return content
    


#%% Intepretation:
"""
Stages of interpretation: 
    1. Yaml is sorted based on whether it's yaml or OAS, 
    2. ...recurison through yaml, sorting the ordering of the definitions and schemas. 
    3. 
"""    

class Interpreter:
    """
    Interpreter main-class: 
    TODO: Fill the documentation here.
    TODO: Check Program Flow. 
    TODO: Split the interpretation of YAML and OAS.yaml. 
    """
    def __init__(self): 
        "Currently just setting up containers for sorting."
        # Note: need to sort the models in order of dependencies. 
        # This means that we'll have to store a map 
        self.header = r'''
#!/usr/bin/env python3
"""
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce
'''
       # Model = Schema, Type = Enum, et.c. 
        self.models = {} # Name: string-interpretation (raw-str)
        self.types = {} # Name: string-interpretation (raw-str), 
        self.namespace = {} # Name : 'Types'/'Models' 
        self.model_refs = {} # name : name 
        # references are from models to models, or types to models
        
        
    def export(self):
        "export function when the yaml has been worked through"
        non_dependent = [model_val for model_key,model_val in self.models.items() if model_key not in self.model_refs.values()]
        dependent = [model_val for model_key,model_val in self.models.items() if model_key in self.model_refs.values()]
        print(non_dependent)
        output = r'''
{0}
{1}
{2}      
{3}
        '''.format( self.header, 
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y), self.types.values()),
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y), non_dependent ) if non_dependent else '', 
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y),dependent) if dependent else '')
        return output
        
    def ref_interpret(self,yaml_input,parent=None):
        "For each case of $ref we need to store a pointer in the model_maps\
        that tells us the order we wish to declare these in. "
        
        # Check if 
        
        
    
    def enum_interpret(self,yaml_input):
        "for cases where we have enums, we need to extract these, and build them \
        as their own BaseModel-cases. "
        descr = yaml_input['description'] if 'description' in yaml_input.keys() else '...Generic description...'
        title = yaml_input['title'] if 'title' in yaml_input.keys() else '_title'
        typ = self.type_interpret(yaml_input['type']) if 'type' in yaml_input.keys() else str
        
        enum_lines = [r"{0} = '{1}'".format(cont.lower(),cont) for cont in yaml_input['enum']]
        
        content= r'''class {0}({1},Enum):
    """
    {2}
    """
    {3}'''.format(title.capitalize(),
                   typ,
                   descr, 
                   reduce(lambda x,y: "{}\n    {}".format(x,y), enum_lines) if enum_lines else 'pass')
        self.namespace[title] = 'Types'
        self.types[title] = content
        return title.capitalize() # returns this so that it's 
    
    def type_interpret(self,type_string,subtype='str'):
        "interpret and translate types to admissible ones.\
        need to specify subtypes for the arrays etc."
        types = {'string': 'str', 
                 'int':'int',
                 'number':'int',
                 'object':'object',
                 'boolean' : 'bool',
                 'array':'List[{}]'.format(subtype)}
        if type_string in types.keys():
            return types[type_string]
    
    def prop_interpret(self,yaml_input,name,required):
        "Interpret properties-field (smaller dictionary)"
        #TODO: Catch prop with $ref into ref_interpreter ?
        title = yaml_input['title'] if 'title' in yaml_input.keys() else name
        req = '...' if required else None
        if 'enum' in yaml_input.keys():
            typ_ = self.enum_interpret(yaml_input)
        else:
            typ_= self.type_interpret(yaml_input['type']) if 'type' in yaml_input.keys() else 'None'
        descr_string = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'
        description = '"{}"'.format(descr_string.replace('\n',' ')) if descr_string else 'no description'
        return r"""{0}: {1} = Field({2}, description={3})""".format(title,typ_,req,description)
        
    
    def schema_interpreter(self,yaml_input,name):
        "Take in a single schema and unpack it."
        print(name)
        description = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'# 1
        required = yaml_input['required'] if 'required' in yaml_input.keys() else []
        # Below we get pass the tuple of property and required-boolean
        
        properties = [self.prop_interpret(val,key,key in required) for key,val in yaml_input['properties'].items()] \
                      if 'properties' in yaml_input.keys() else None#3
        title = yaml_input['title'] if 'title' in yaml_input.keys() else name #0
        #tpe = yaml_input['type'] #2
        # Add in interpretation of inherited #allOf etc. 
        content= r"""
class {0}(BaseModel):
    '''
    {1}
    '''
    {2}""".format(  title.capitalize(),
                    description,
                    reduce(lambda x,y: "{}\n    {}".format(x,y), properties) if properties else "pass")
        self.models[title] = content
        self.namespace[title] = 'Models'
        
    def interpretation_staging(self,dict_of_names, map_of_dependencies):
        #TODO: stage the components, i.e. sort based on references
        pass 
    
    def yaml_interpret(self,yaml_input):
        """
        Note: Yamls are loaded as dictionaries. 
        This means we can traverse them and set the properties either as strings, 
        or just fully build them here. 
        """
        interpreted = [self.schema_interpreter(definition,name) for name,definition in yaml_input.items()]
        # Given a list of schemas/definitions
        # use tuples to filter by dependencies/references,
        return interpreted
        
    
    def definitions_interpreter(self,yaml_input):
        """Input top level: take a schema, and sort it into an executable string"""
        definition_models = self.yaml_interpret(yaml_input['definitions'])

        formatting = r"""
{0}""".format(reduce(lambda x,y: "{}\n    {}".format(x,y), definition_models))
        return formatting
        

#%% Run-utils 
        

def write_to_py(content,filename='yaml_test.py'):
    with open(filename,'w') as f:
        f.write(content)    

def Build_From_Yaml(filename):
    "Generic function to build from a yaml-filename"
    yaml_from_file = read_yaml(filename)
    #TODO: build-directory
    test = Interpreter() 
    test.definitions_interpreter(yaml_from_file)
    write_to_py(test.export())



#%% Magic. 

       

if __name__ == '__main__':
    """
    If you want to execute this, run: 
    > python thisfile.py yaml-source target-app-name
    
    """
    
    