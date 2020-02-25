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
    

def string_convert(string): 
    #TODO: Make flexible for titles, etc... and pervasive throughout. 
    "From utf-8 valid variable-name (lower-case and underscore)"
    return "".join([ char if char.isalnum() or char in ["&"," ","-"] else "" 
                    for char in string]).replace(" ", "_").replace("&","and").replace("-","_")
#%% Intepretation:
#TODO: Write this doc. 
"""

Stages of interpretation: 
    1. Yaml is sorted based on whether it's yaml or OAS, 
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
        self.header = r'''#!/usr/bin/env python3
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
        # ^on the name-space, this is used for refs. so storing them 
        #  currently only by their 
        self.model_refs = {} # name : name 
        # references are from models to models, or types to models
        self.name = "<name of yaml + loc>"
        
    def export(self):
        "export function when the yaml has been worked through"
        non_dependent = [model_val for model_key,model_val in self.models.items() if model_key not in self.model_refs.values()]
        dependent = [model_val for model_key,model_val in self.models.items() if model_key in self.model_refs.values()]
        #print(non_dependent)
        output = r'''{0}
###################
# Enums and Types #
###################
{1}
##########
# Models #
##########
{2}      
{3}

        '''.format( self.header, 
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y), self.types.values()),
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y), non_dependent ) if non_dependent else '', 
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y),dependent) if dependent else '')
        return output
        
    def ref_interpret(self,yaml_input):
        "For each case of $ref we need to store a pointer in the model_maps\
        that tells us the order we wish to declare these in. "        
        ref = yaml_input['$ref'].split('/')[-1] #assuming it's at an end
        return ref
        # Check if existing in namespace, in which case use that reference. 
        
        
        
    
    def enum_interpret(self,yaml_input,name):
        "for cases where we have enums, we need to extract these, and build them \
        as their own BaseModel-cases. "
        descr = yaml_input['description'] if 'description' in yaml_input.keys() else '...Generic description...'
        title = name #if name[0].isupper() else name.capitalize() #yaml_input['title'] if 'title' in yaml_input.keys() else name
        typ = self.type_interpret(yaml_input['type'],yaml_input) if 'type' in yaml_input.keys() else str
        
        enum_lines = [r"{0} = '{1}'".format(string_convert(cont.lower()),cont) for cont in yaml_input['enum']]
        print(name,enum_lines)
        content= r'''class {0}({1},Enum):
    """
    {2}
    """
    {3}'''.format(title,
                   typ,
                   descr, 
                   reduce(lambda x,y: "{}\n    {}".format(x,y), enum_lines) if enum_lines else 'pass')
        self.namespace[title] = 'Types'
        self.types[title] = content
        return title # returns this so that it's 
    
    def type_interpret(self,type_string,yaml_input):
        "interpret and translate types to admissible ones.\
        need to specify subtypes for the arrays etc."
        
        types = {'string': 'str', 
                 'int':'int',
                 'number':'int',
                 'object':'object',
                 'boolean' : 'bool'}
        if type_string == 'array':
            #print(yaml_input)
            return "List[{}]".format(self.item_interpret(yaml_input['items']) if 'items' in yaml_input.keys() else 'str')
        elif 'allOf' in yaml_input.keys():
            return self.ref_interpret(yaml_input['allOf'][0])
        elif type_string in types.keys():
            return types[type_string]
    
    def item_interpret(self,items):
        "for items in an array. "
        for key,val in items.items():
            if key == '$ref':
                return self.ref_interpret(items)
            elif type(val) == list: 
                str
            else: 
                return self.type_interpret(items['type'],items)
        
    
    def prop_interpret(self,yaml_input,name,required):
        "Interpret properties-field (smaller dictionary)"
        #TODO: Catch prop with $ref into ref_interpreter ?
        title = name #yaml_input['title'] if 'title' in yaml_input.keys() else name
        req = '...' if required else None
        
        if 'enum' in yaml_input.keys():
            typ_ = self.enum_interpret(yaml_input,name)
        elif '$ref' in yaml_input.keys():
            typ_ = self.ref_interpret(yaml_input)
        elif 'allOf' in yaml_input.keys():
            typ_ = self.ref_interpret(yaml_input['allOf'][0])
        else:
            typ_= self.type_interpret(yaml_input['type'],yaml_input) if 'type' in yaml_input.keys() else 'None'
        descr_string = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'
        description = '"{}"'.format(descr_string.replace('\n',' ')) if descr_string else '"no description"'
        return r"""{0}: {1} = Field({2}, description={3})""".format(string_convert(title).lower(),typ_,req,description)
        
    
    def schema_interpreter(self,yaml_input,name):
        "Take in a single schema and unpack it."
        #print(name)
        #print(yaml_input.keys())
        description = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'# 1
        # Below we get pass the tuple of property and required-boolean
        if 'allOf' in yaml_input.keys():
            subdicts = yaml_input['allOf']
            subseq = {}
            ref = {}
            for item in subdicts: 
                if '$ref' in item.keys():
                    ref.update(item)
                else: 
                    subseq.update(item)
            #ref = {**subdict for subdict in subdicts if '$ref' in subdict.keys()}
            #subseq = {}.update([subdict for subdict in subdicts if '$ref' not in subdict.keys()])
            required = subseq['required'] if 'required' in subseq.keys() else []
            properties =  [self.prop_interpret(val,key,key in required) for key,val in subseq['properties'].items()] \
                      if 'properties' in subseq.keys() else None#3
            parent = self.ref_interpret(ref)
        else: 
            required = yaml_input['required'] if 'required' in yaml_input.keys() else []
            parent = 'BaseModel'
            properties = [self.prop_interpret(val,key,key in required) for key,val in yaml_input['properties'].items()] \
                      if 'properties' in yaml_input.keys() else None#3
        
        title = name#yaml_input['title'] if 'title' in yaml_input.keys() else name #0
        #tpe = yaml_input['type'] #2
        # Add in interpretation of inherited #allOf etc. 
        content= r"""
class {0}({3}):
    '''
    {1}
    '''
    {2}""".format(  string_convert(title),
                    description,
                    reduce(lambda x,y: "{}\n    {}".format(x,y), properties) if properties else "pass",
                    parent)
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
        interpreted = []
        for name,definition in yaml_input.items():
            if 'enum' in definition.keys():
                self.enum_interpret(definition,name)    
            else: 
                interpreted.append(self.schema_interpreter(definition,name))
        # Given a list of schemas/definitions
        # use tuples to filter by dependencies/references,
        return interpreted
        
    
    def definitions_interpreter(self,yaml_input):
        """Input top level: take a schema, and sort it into an executable string"""
        definition_models = self.yaml_interpret(yaml_input['definitions'])

        formatting = r"""
{0}""".format(reduce(lambda x,y: "{}\n    {}".format(x,y), definition_models))
        return formatting
        

#%% OAS class 
        
class OAS(Interpreter):
    "Subclass for OAS-interpretation."
    #TODO: Create formatting spec-file s.t. generated stubs etc. can 
    #      be easily modified and tailored based on API. 
    #TODO: Additional support for the OAS-structures:
    # - components 
    # - - schemas (same struct at yaml. )
    # - - ... 
    # - info
    # - paths 
    # - tags
    # - - name: 
    # - - description
    # - openapi (str)  - versioning
    # 
    # Import explicit schemas from the DataModel-generation ? 
    def __init__(self, yaml_input):
        #Interpreter.__init__()
        self.components = yaml_input['components']
        self.imports = {} # Track imports from data-model, and explicitly import ? 
        self.info = yaml_input['info']
        self.tags = yaml_input['tags'] #name, descript
        self.header =r'''#!/usr/bin/env python3
"""
Project: {title}
OpenAPI: {openapi}
----
{info}
----
{tags}
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce

'''.format(info=self.unpack_info(yaml_input),
           openapi=yaml_input['openapi'],
           title=yaml_input['info']['title'],
           tags=tags) #1


    
    def unpack_info(self,yaml_input):
        "information-unpack , including open-api versioning. "
        #TODO: Pull format of info from external spec. 
        info = yaml_input['info']
        description = info['description']
        version=info['version']
        title=info['title']
        contact=info['contact']
        license_= info['license']
        formatting = r"""```{title}```
{version}
        """.format(title=title,
        )
    
    def interpret_paths(self,yaml_input):
        
        paths = yaml_input['paths']
        
    def unpack_path(self,yaml_input):
        "extract a path"

    def make_request(self, yaml_input):
        "make request"
        request_type = yaml_input[]
        template = r'''
        
        '''
        
    
    def make_components(self,yaml_input):
        "basically pad with same as model-interpreting"
        
    
        
    

#%% Run-utils 
        

def write_to_py(content,filename='yaml_test.py'):
    with open(filename,'w') as f:
        f.write(content)    

def Build_From_Yaml(filename,asname='yaml_test.py'):
    "Generic function to build from a yaml-filename"
    yaml_from_file = read_yaml(filename)
    #TODO: build-directory
    test = Interpreter() 
    test.definitions_interpreter(yaml_from_file)
    
    write_to_py(test.export(),asname)



#%% Magic. 

       

if __name__ == '__main__':
    """
    If you want to execute this, run: 
    > python thisfile.py yaml-source target-app-name
    
    """
    
    