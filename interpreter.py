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






#%% Intepretation:
"""
Stages of interpretation: 
    1. Yaml is sorted based on whether it's yaml or OAS, 
    2. 
"""     
def ref_interpret(yaml_input):
    "For cases of $ref: we need to make the actual references to the \
    models built for these.. I think."

def enum_interpret(yaml_input):
    "for cases where we have enums, we need to extract these, and build them \
    as their own BaseModel-cases. "
    descr = yaml_input['description'] if 'description' in yaml_input.keys() else '...Generic description...'
    title = yaml_input['title'] if 'title' in yaml_input.keys() else '_title'
    typ = type_interpret(yaml_input['type']) if 'type' in yaml_input.keys() else str
    
    enum_lines = [r"{0} = '{1}'".format(cont.lower(),cont) for cont in yaml_input['enum']]
    return r'''class {0}(str,Enum):
    """
    {1}
    """
    {2}
    '''.format(title.capitalize(),descr, reduce(lambda x,y: "{}\n    {}".format(x,y), enum_lines))

def type_interpret(type_string,subtype='str'):
    "interpret and translate types to admissible ones.\
    need to specify subtypes for the arrays etc."
    #TODO: Catch if contains enum. 
    types = {'string': 'str', 
             'int':'int',
             'number':'int',
             'object':'object',
             'boolean' : 'bool',
             'array':'List[{}]'.format(subtype)}
    if type_string in types.keys():
        return types[type_string]

def prop_interpret(yaml_input,name,required):
    "Interpret properties-field (smaller dictionary)"
    #TODO: Catch prop with $ref into ref_interpreter
    title = yaml_input['title'] if 'title' in yaml_input.keys() else name #0
    req = '...' if required else None
    print(yaml_input)
    typ_= type_interpret(yaml_input['type']) if 'type' in yaml_input.keys() else 'None'
    descr_string = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'
    description = '"{}"'.format(descr_string.replace('\n',' '))
    return r"""{0}: {1} = Field({2}, description={3})""".format(title,typ_,req,description)
    

def schema_interpreter(yaml_input,name):
    "Take in a single schema and unpack it."
    print(name)
    description = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'# 1
    required = yaml_input['required'] if 'required' in yaml_input.keys() else []
    # Below we get pass the tuple of property and required-boolean
    
    properties = [prop_interpret(val,key,key in required) for key,val in yaml_input['properties'].items()] \
                  if 'properties' in yaml_input.keys() else None#3
    title = yaml_input['title'] if 'title' in yaml_input.keys() else name #0
    #tpe = yaml_input['type'] #2
    # Add in interpretation of inherited #allOf etc. 
    return (r"""
class {0}(BaseModel):
    '''
    {1}
    '''
    {2}
    """.format(title,description,reduce(lambda x,y: "{}\n    {}".format(x,y), properties) if properties else "Pass"))
    
def interpretation_staging(list_of_interpretations):
    #TODO: stage the components, 
    pass 

def yaml_interpret(yaml_input):
    """
    Note: Yamls are loaded as dictionaries. 
    This means we can traverse them and set the properties either as strings, 
    or just fully build them here. 
    """
    interpreted = [(schema_interpreter(definition,name),name) for name,definition in yaml_input.items()]
    # Given a list of schemas/definitions
    # use tuples to filter by dependencies/references,
    return interpreted
    

def interpreter_top(yaml_input):
    """Input top level: take a schema, and sort it into an executable string"""
    imports = r"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce"""
    definition_models = yaml_interpret(yaml_input['definitions'])
    
    formatting = r"""
#!/usr/bin/env python3
'''
Generic Statement to be inserted here... 
'''
{0}
{1}
    """.format(imports, reduce(lambda x,y: "{}\n    {}".format(x,y), definition_models))
    return formatting
    

def write_to_py(content,filename='yaml_test.py'):
    with open(filename,'w') as f:
        f.write(content)
#%%
        
def Build_From_Yaml(filename):
    pass


#%% Magic. 

       

if __name__ == '__main__':
    """
    If you want to execute this, run: 
    > python thisfile.py yaml-source target-app-name
    
    """
    
#%%  Tests, based on earlier examples: 
def __test():
    class test_Difficulty(str,Enum):
        advanced=  "Advanced"
        beginner = "Beginner"
        intermediate= "Intermediate"
    
    class test_Challenge(BaseModel):
        "Set of Exercises combined to test a skillset"
        id: str = Field(..., description="test")
        created: int = Field(..., description="Date and time of object creation. Unix format") 
        title: str = Field(..., description="Short description of challenge")
        tagline: str = Field(..., description="add-on text with more details to the title")
        description: str = Field(None, description="Longer, in-depth description of challenge")
        promoImage: str = Field(..., description="visual description of challenge")
        promoVideo: str = Field(None, description="in-depth stimulating descript of challenge")
        duration: int = Field(None, decription="Total time measured in seconds")
        difficulty: test_Difficulty = Field(None, description="difficulty level")
        languages: List[str] = Field(None, description="supported languages for challenge")
        type: str = Field(..., description="type of challenge" )
        exercises: List[str] = Field(None, description="exercises in challenge")
        organizers: List[str] = Field(..., description="organisation(s) hosting/supporting the challenge")
 
    diff_yaml_str= """
    difficulty:
        description: The difficulty level of the challenge.
        enum:
          - Advanced
          - Beginner
          - Intermediate
        type: string
        title: difficulty"""    
    challenge_yaml_str="""
    Challenge:
    description: Basically a set of exercises combined for the purpose of testing skills.
    title: Challenge
    type: object
    properties:
      id:
        description: Unique identifier for the object.
        type: string
        title: id
      created:
        description:
          Date and Time at which the object was created. Measured in seconds
          since the Unix epoch.
        type: string
        format: date-time
        title: created
      title:
        description: A short text describing the challenge.
        type: string
        title: title
      tagline:
        description: A short add-on text, adding more details to the title.
        type: string
        title: tagline
      description:
        description: A in-depth text describing the challenge.
        type: string
        title: description
      promoImage:
        description: A visual description of the challenge.
        type: string
        title: promoImage
      promoVideo:
        description: In-depth stimulating descrpitionof the challenge.
        type: string
        title: promoVideo
      duration:
        description: Total time, measured in seconds
        type: number
        title: duration
      difficulty:
        description: The difficulty level of the challenge.
        enum:
          - Advanced
          - Beginner
          - Intermediate
        type: string
        title: difficulty
      langauges:
        description: The supported languages for this challenge.
        type: array
        items:
          $ref: "#/definitions/Language"
        title: langauges
      type:
        description: The type of challenge.
        enum:
          - Live Quiz
          - Online Project
        type: string
        title: type
      exercises:
        description: The exercises making up the challenge.
        type: array
        items:
          $ref: "#/definitions/Exercise"
        title: exercises
      organizers:
        description: The organization(s) hosting the challenge
        type: array
        items:
          $ref: "#/definitions/Organization"
        title: organizers
    required:
      - created
      - id
      - organizers
      - promoImage
      - tagline
      - title
      - type
      """
    
    test_interpret_diff = schema_interpreter(diff_yaml_str)
    diff_test = test_interpret_diff == test_Difficulty
    
    test_intepret_challenge= schema_interpreter(challenge_yaml_str)
    chall_test = test_intepret_challenge == test_Challenge
    return diff_test