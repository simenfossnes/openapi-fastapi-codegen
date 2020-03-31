#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yaml Interpreter -> Python Model 

Created on Fri Feb  7 15:59:02 2020

@author: jacobalexander

Takes in an oas.yaml file and generates a FastAPI directory stub 
with models, routes, and Dockerfile that can be used to create a service. 

Intention is that it builds the basics (server stubs) and that you from there 
complete the logic and the "actual" implementiaton of the services, so that 
you do not have to make every little bit yourself.

"""
import yaml 
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce

import os # for mkdir etc. 
from shutil import copyfile
from pathlib import Path,PosixPath

from collections import defaultdict

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
    

def Top_Order(graph_dictionary):
    """
    Take in a Directed graph described in a dictionary, and returns a list 
    of the elements in a topological order. 
    e.g. 
    a : [b,c]
    b : [d]
    c : [d]
    => [a,b,c,d] or [a,c,b,d] are valid 
    """
    #Note, using defaultdict gives us default-values i.e. [] or False here: 
    graph = defaultdict(list)
    visited=defaultdict(bool)
    
    for k,vals in graph_dictionary.items():
        graph[k] = vals
            
    def visit(s,visited,sorted_list):
        visited[s] = True
        for i in graph[s]:
            if not visited[i]:
                visit(i,visited,sorted_list)
        sorted_list.insert(0,s)
        
    sortlist=[]
    # Have to iterate over the original graph-dictionary out here, 
    # as it seems the program is apt to "change the size" of the graph, 
    # (note: it should not, but it complains...)
    for v in graph_dictionary:
        print(v)
        if not visited[v]:
            visit(v,visited,sortlist)
            
    return list(reversed(sortlist))
    
        

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
    def __init__(self,path=''): 
        "Currently just setting up containers for sorting."
        # Note: need to sort the models in order of dependencies. 
        # This means that we'll have to store a map 
        
        self.path = path # main path of 
        # ext_source = '../rel-location/file.yaml#' : read_yaml(source)
        self.ext_sources = defaultdict(dict) #read once.
        # ext_schema = 'parent#/definitions/somename' : str of schema
        self.header_yaml = r'''#!/usr/bin/env python3
"""
#TODO: Come up with proper statement etc. here. 
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple,NewType
from functools import reduce

def doc_handler(docstring):
    "for resolving documentation of functions and classes"
    return docstring.strip('\n').strip()
    
'''
       # Model = Schema, Type = Enum, et.c. 
        self.models = {} # Name: string-interpretation (raw-str)
        self.types = {} # Name: string-interpretation (raw-str), 
        self.namespace = {} # Name : 'Types'/'Models' 
        # ^on the name-space, this is used for refs. so storing them 
        #  currently only by their 
        self.model_refs = defaultdict(list) # name : name 
        self.unions = defaultdict(str)
        
        # references are from models to models, or types to models
        self.name = "<name of yaml + loc>"
        
    def resolve_external_source(self,location):
        "Imports any referenced yaml-files to include the schemas from there"
        print('resolving external location:\n')
        print(self.path, location)
        rel_loc = os.path.join(self.path,location)
        self.ext_sources[location] = read_yaml(rel_loc)
        
    def resolve_external_schema(self,location,schema):
        "schemas imported from external sources <source>#<schema>"
        schema_split = schema.split('/')[1:]
        
        title = schema_split[-1]
        if title in self.models.keys() or title in self.types.keys():
            pass
        else:
            if location in self.ext_sources.keys():
                pass
            else: 
                self.resolve_external_source(location)
            # Find the target schema, and resolve the interpretation.
            target_schema = reduce(lambda x,y: x[y], schema_split, self.ext_sources[location])
            self.schema_interpreter(target_schema,title,location)
        
    def export_yaml(self):
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

        '''.format( self.header_yaml, 
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y), self.types.values()),
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y), non_dependent ) if non_dependent else '', 
                    reduce(lambda x,y: '{}\n\n{}'.format(x,y),dependent) if dependent else '')
        return output
    
    def export_as_filetree(self):
        "exports the content as individual files or as a filetree-like structure"
        #TODO: Fix this 
        
    def ref_interpret(self,yaml_input,location=''):
        "For each case of $ref we need to store a pointer in the model_maps\
        that tells us the order we wish to declare these in. "
        dirname,name = yaml_input['$ref'].split('#') # Will only be two. 
        dirname = location+dirname
        
    
        ref = name.split('/')[-1] #assuming it's at an end
        if ref in self.models.keys() or ref in self.types.keys():
            pass
        else: #need to ensure it's made. 
            if dirname != '':
                print('ref-debug:')
                print(name)
                print(dirname, name)
                # external location, need to resolve. 
                self.resolve_external_schema(dirname,name)
        return ref
       
        
        
        
    
    def enum_interpret(self,yaml_input,name,location=''):
        "for cases where we have enums, we need to extract these, and build them \
        as their own BaseModel-cases. "
        descr = yaml_input['description'] if 'description' in yaml_input.keys() else '...Generic description...'
        title = name #if name[0].isupper() else name.capitalize() #yaml_input['title'] if 'title' in yaml_input.keys() else name
        typ = self.type_interpret(yaml_input['type'],yaml_input,title,location) if 'type' in yaml_input.keys() else str
        
        enum_lines = [r"{0} = '{1}'".format(string_convert(cont.lower()),cont) for cont in yaml_input['enum']]
        print('enum:',name,enum_lines)
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
    
    def type_interpret(self,type_string,yaml_input,body_of,location=''):
        "interpret and translate types to admissible ones.\
        need to specify subtypes for the arrays etc."
        
        types = {'string': 'str', 
                 'int':'int',
                 'number':'int',
                 'object':'object',
                 'boolean' : 'bool'}
        if type_string == 'array':
            #print(yaml_input)
            return "List[{}]".format(self.item_interpret(yaml_input['items'],body_of,location) if 'items' in yaml_input.keys() else 'str')
        elif 'allOf' in yaml_input.keys():
            interpreted= self.ref_interpret(yaml_input['allOf'][0],location)
            self.model_refs[body_of].append(interpreted)
            return interpreted
        elif 'oneOf' in yaml_input.keys():
            union_list = []
            for el in yaml_input['oneOf']:
                interpreted= self.ref_interpret(el,location)
                self.model_refs[body_of].append(interpreted)
                union_list.append(interpreted)
            #Create Union
            return "Union[{}]".format(reduce(lambda x,y: "{},{}".format(x,y), union_list))
            
        elif type_string in types.keys():
            return types[type_string]
    
    def item_interpret(self,items,body_of=None,location=''):
        "for items in an array. "
        for key,val in items.items():
            if key == '$ref':
                interpreted= self.ref_interpret(items,location)
                self.model_refs[body_of].append(interpreted)
                return interpreted
            elif key == 'anyOf' or key=='oneOf':
                refs = [self.ref_interpret(item,location) for item in val]
                for ref in refs:
                    self.model_refs[body_of].append(ref)
                return "Union[{}]".format(reduce(lambda x,y: "{},{}".format(x,y), refs))
                
            elif type(val) == list: 
                str
            else: 
                return self.type_interpret(items['type'],items,body_of,location)
        
    
    def prop_interpret(self,yaml_input,name,required,body_of,location=''):
        "Interpret properties-field (smaller dictionary)"
        #TODO: Catch prop with $ref into ref_interpreter ?
        title = name #yaml_input['title'] if 'title' in yaml_input.keys() else name
        req = '...' if required else None
        #TODO: Make more elegant if-elif thingy 
        if 'enum' in yaml_input.keys():
            typ_ = self.enum_interpret(yaml_input,name,location)
        elif '$ref' in yaml_input.keys():
            typ_ = self.ref_interpret(yaml_input,location)
            self.model_refs[body_of].append(typ_)
        elif 'allOf' in yaml_input.keys():
            typ_ = self.ref_interpret(yaml_input['allOf'][0],location)
        else:
            typ_= self.type_interpret(yaml_input['type'],yaml_input,title,location) if 'type' in yaml_input.keys() else 'None'
        descr_string = yaml_input['description'] if 'description' in yaml_input.keys() else None
        description = '"{}"'.format(descr_string.replace('\n',' ')) if descr_string else 'doc_handler({})'.format(typ_)
        return r"""{0}: {1} = Field({2}, description={3})""".format(string_convert(title).lower(),typ_,req,description)
        
    
    def schema_interpreter(self,yaml_input,name,location=''):
        "Take in a single schema and unpack it."
        #TODO: Make handling of writeOnly/readOnly-keywords to generate 
        #      duplicate models for request-/response-models
        # e.g. if writeOnly => only in request schema
        #      if readOnly => only in response schema
        # Need to also explicitly resolve the location to handle external schemas
        #print(name)
        #print(yaml_input.keys())
        title = name#yaml_input['title'] if 'title' in yaml_input.keys() else name #0
        typ_ = self.type_interpret(yaml_input['type'],yaml_input,title,location) if 'type' in yaml_input.keys() else 'None'
        description = yaml_input['description'] if 'description' in yaml_input.keys() else '%s has no description'%title# 1
        # Below we get pass the tuple of property and required-boolean
        properties = None
        extends = 'BaseModel'
        if 'allOf' in yaml_input.keys():
            print('in allOf', title)
            subdicts = yaml_input['allOf']
            subseq = {}
            ref = {}
            for item in subdicts: 
                if '$ref' in item.keys():
                    ref.update(item) #string concat.
                else: 
                    subseq.update(item)
            #print('refs:',name,ref)
            #ref = {**subdict for subdict in subdicts if '$ref' in subdict.keys()}
            #subseq = {}.update([subdict for subdict in subdicts if '$ref' not in subdict.keys()])
            required = subseq['required'] if 'required' in subseq.keys() else []
            properties =  [self.prop_interpret(val,key,key in required,title,location) for key,val in subseq['properties'].items()] \
                           if 'properties' in subseq.keys() else None#3
            parent = self.ref_interpret(ref,location)
            self.model_refs[title].append(parent)
            
        elif 'oneOf' in yaml_input.keys():
            #TODO: make Union object. 
            refs_to = [self.ref_interpret(ref,location) for ref in yaml_input['oneOf'] ]
            refs_string = reduce(lambda x,y: "{},{}".format(x,y), refs_to)
            typ_ = "Union[{}]".format(refs_string)
            for ref in refs_to:
                self.model_refs[title].append(ref)
            
        elif 'anyOf' in yaml_input.keys():
            refs_to = [self.ref_interpret(ref,location) for ref in yaml_input['allOf'] ]
            # reduce to single string: 
            refs_string = reduce(lambda x,y: "{},{}".format(x,y), refs_to)
            typ_ = "Union[{}]".format(refs_string)
            for ref in refs_to:
                self.model_refs[title].append(ref)
            

        #    pass
        #elif 'properties' not in yaml_input.keys():
            # just a description and a type assumed 
            # Store this as a 
         #   pass
            
        else: 
            required = yaml_input['required'] if 'required' in yaml_input.keys() else []
            parent = 'BaseModel'
            properties = [self.prop_interpret(val,key,key in required,title,location) for key,val in yaml_input['properties'].items()] \
                          if 'properties' in yaml_input.keys() else None#3
        
        #tpe = yaml_input['type'] #2
        # Add in interpretation of inherited #allOf etc. 
        if properties: 
            content= r"""
class {title}({extends}):
    '''
    {description}
    '''
    {root}{props}""".format(title=string_convert(title),
                    description=description,
                    extends = extends,
                    root="__root__: %s\n    "% parent if not parent == "BaseModel" else "",
                    props= reduce(lambda x,y: "{}\n    {}".format(x,y), properties) if properties else "pass",
                    )
            self.models[title] = content
            self.namespace[title] = 'Models'
        else: 
            content= r"""
{title} = NewType("{title}",{typ})
{title}.__doc__ = "{description}"
""".format(title=string_convert(title),typ=typ_,description=description.strip('\n').strip())
            self.types[title] = content
            self.namespace[title] = 'Types'
        
        
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
        
        #TODO: remove formatting-variable ? 
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
    def __init__(self, yaml_input,path=''):
        
        self.path = path
        Interpreter.__init__(self,path) # inhertining lots of stuff
        self.functions = {} # following same pattern
        self.responses = {}
        #self.tags = yaml_input['tags'] #name, descript
        #Note, inheriting header from Interpreter, but overwriting it here. 
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
from functools import reduce
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from starlette.responses import JSONResponse
#from DataModel import * # DockerFile places this in app-directory but not really necessary ? 

# Relative imports within the src-material but not from top-layer here. 
from src import *
app = FastAPI()


'''.format(info=self.unpack_info(yaml_input),
           openapi=yaml_input['openapi'],
           title=yaml_input['info']['title'],
           tags=yaml_input['tags'])
        

    def export_oas(self):
        "export function, similar to interpreter-export" 
        
        types_and_models =defaultdict(str)
        types_and_models.update(self.types)
        types_and_models.update(self.models)
        types_and_models = self.sorting_algo(types_and_models,self.model_refs)
        #print(non_dependent)
        #print('going out:\n',types_and_models)
        functions = [func_val for func_name,func_val in self.functions.items()]
        #quickfix: nixed {models} from below. 
        output = r'''{header}
## Imports should be handled,
## In testing phase now. 
from . import * # this is sorta blind import of everything from the main-init...

{functions}


        '''.format( header=self.header, 
                    types=reduce(lambda x,y: '{}\n\n{}'.format(x,y), self.types.values(),''),
                    responses=reduce(lambda x,y: '{}\n\n{}'.format(x,y),self.responses.values(),''),
                    #models=reduce(lambda x,y: '{}\n\n{}'.format(x,y), types_and_models,'') , 
                    functions=reduce(lambda x,y: '{}\n\n{}'.format(x,y),functions,'') )
        
        return output
        
        #        return r'''{header}
        #{components}
        #{functions}'''.format(header=self.header,
        #                      components=self.models)
        
    def export_as_filetree(self):
        #TODO: Write this (builds on top of interpreter.export_as... ? )
        #TODO: Generalize this to take in a specified build-template, and resolve the 
        #      formatting of components dependent on that resolution logic. 
        src_init = r'''
from .Models import * 
from .Logic import * 
from .Routes import *'''
        #Note: main_init not correctly resolvable. 
        main_init = r'''#Note, not sure if this one is needed. 
from .src import *
from .dist import *'''
        types_and_models =defaultdict(str)
        types_and_models.update(self.types)
        types_and_models.update(self.models)
        types_and_models = self.sorting_algo(types_and_models,self.model_refs)

        filetree = {'src': {'':[('__init__.py',src_init)],
                            'Logic':{'':[('__init__.py','#Append with\n#from .package import *\n')]},
                            'Routes':{'':[('__init__.py','#Append with\n#from .package import *\n#from .routes import *\n#from .responses import *\n'),
                                           ('responses.py',"#Dummy content for now\n"),
                                           ('routes.py', "#Nothing for now.\n")
                                           ]},
                            'Models':{'':[('models.py',self.file_formatting(types_and_models)),
                                          
                                          ('__init__.py','#Append with\n#from .package import *\nfrom .models import *\n')
                                           ]}},
                    'dist':{'':[('README.md', '##<TODO>: build to dist-folder')]},
                    '':[Path('data/Dockerfile'), #copy from data/Dockerfile. 
                        ('main.py', self.export_oas())]
                        #('__init__.py',main_init)]
                    }
        return filetree
            
                    
    def file_formatting(self,content):
        "Wrap the content in header etc, +imports "
        
        return reduce(lambda x,y: '{}\n{}'.format(x,y),content,self.header_yaml)
    
    def sorting_algo(self,types_and_models,order_graph):
        "Will just default sort the types and models into a single list"
        #TODO: bump to Interpreter. 
        
        # Sort the order-graph: 
        sortlist = Top_Order(order_graph)
        #start with unsorted portion,
        full_list = [key for key in types_and_models if key not in sortlist]
        full_list.extend(sortlist)
        content = [types_and_models[el] for el in full_list]
        #print('types_and_models: \n',content)
        
        return content
        
    def unpack_info(self,yaml_input):
        "information-unpack , including open-api versioning. "
        #TODO: Pull format of info from external spec. 
        info = yaml_input['info']
        #TODO: assume existence of keys, and concatenate in 
        #      a lambda-reduce thingy. with default vals in format-template 
        formatting = r"""```{title}```
version: {version}
contact: {contact}
description: {description}
license: {license_}
        """.format(title=info['title'],
                   version=info['version'],
                   contact=info['contact'],
                   description = info['description'],
                   license_= info['license'])
        return formatting
    
    def interpret_paths(self,yaml_input):
        "extract paths based on the list available in input-yaml(oas)"
        paths = yaml_input['paths']  
        #self.functions = [] # initialize a location to store functions-strings
        for path,requests in paths.items(): 
            self.unpack_path(requests,path)
        
    def unpack_path(self,yaml_input,path):
        "extract a path"
        #print(path, yaml_input)
        request_parameters = yaml_input['parameters'] if 'parameters' in yaml_input.keys() else {}
        for request_type,request in yaml_input.items(): 
            if not request_type == 'parameters':
                self.make_request(request,request_type,request_parameters, path)
            
    def make_request(self, yaml_input, request_type ,parameters,path='/'):
        "make request"
        
        params_list= r'"{path}"'.format(path=path) #++        
        #responses= #to pad param-list
        
        func_name= request_type +"_"+ string_convert(path)
        #request_parameters = self.make_request_params(parameters)
        #responses = [self.make_response(response_item) for response_item in yaml_input['responses'].items()] if 'responses' in yaml_input.keys() else []
        request_body = self.make_request_body(yaml_input['requestBody']) if 'requestBody' in yaml_input.keys() else ''
        #request_body=''
        request_string=r'@app.{request}({params})'.format(request=request_type,params=params_list)
        template = r'''{request}
async def {func_name}({request_body}):
    """
    {documentation}
    """
    return None
        '''.format(func_name=func_name,
                   documentation='none',
                   request_body=request_body,
                   request=request_string)
        self.functions[func_name] = template
        
    def make_request_body(self,yaml_input):
        # Assuming 'content' / application /schema => component. 
        #TODO: this is inflexible, needs fix for cases, or extensios ?
        
        content = yaml_input['content']
        content_sub= [val for val in content.values()][0]
        ref = content_sub['schema']
        #TODO: need to make this a Query-generation i.e. 
        # param: ParamType = Query(<required>, description...)
        return self.ref_interpret(ref)
    
    def make_response(self,response_code, yaml_input):
        "responses nests inside paths, so while expanding these the responses are generated"
        #response_code, 
        
    def make_request_params(self,yaml_input,name, required=False):
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
            typ_= self.type_interpret(yaml_input['type'],yaml_input,title) if 'type' in yaml_input.keys() else 'None'
        descr_string = yaml_input['description'] if 'description' in yaml_input.keys() else 'no description'
        description = '"{}"'.format(descr_string.replace('\n',' ')) if descr_string else '"no description"'
        return r"""{0}: {1} = Query({2}, description={3})""".format(string_convert(title).lower(),typ_,req,description)
        
    
    def make_components(self,yaml_input):
        "basically pad with same as model-interpreting"
        components_yaml = yaml_input['components']
        definition_models = self.yaml_interpret(components_yaml['schemas'])
        
        formatting = r"""
{0}""".format(reduce(lambda x,y: "{}\n    {}".format(x,y), definition_models))
        return formatting
        
        
    def build_oas(self,yaml_input):
        "Run the stack of modules"
        self.make_components(yaml_input)
        self.interpret_paths(yaml_input)
    
        
    

#%% Run-utils 
        
def build_directories(filetree=None,root_dir="test"):
    "build directories/folder struture"
    # src / {logic,models,routes}
    # dist / #build directory for service. 
    # main.py #<< write main composition here. 
    # DockerFile # 
    # README.md #< default values. 
    # Note '': is the directory itself, and assigns 
    # any files to be written. 
    if not filetree:
        filetree = {'src':{'Logic':{'':[] }, 
                           'Routes':{'':[] },
                           'Models':{'':[]},
                                 '':[]},
                    'dist':{'':[]},
                    '':[Path('data/Dockerfile')]}
    #Solve using recursion: 
    def recursion(folder_structure, parents):
        for sub,content in folder_structure.items():
            current_dir = os.path.join(parents,sub)
            if sub == '':
                for item in content: 
                    if type(item) == PosixPath:
                        if item.exists():
                            copyfile('{}'.format(item), os.path.join(current_dir,os.path.basename(item)))
                        else: 
                            print('File does not exist: ', item)
                            
                    else: 
                        #assuming case of save-to-file (tuple of filename and content ? )
                        write_to_py(item[1],filename=os.path.join(current_dir,item[0]))
            else:
                Path(current_dir).mkdir(parents=True,exist_ok=True)
                recursion(content,current_dir)
    Path(root_dir).mkdir(parents=True,exist_ok=True)
    recursion(filetree,root_dir)
    

def write_to_py(content,filename='yaml_test.py'):
    with open(filename,'w') as f:
        f.write(content)    

def Build_From_Yaml(filename,asname='test/yaml_test.py'):
    "Generic function to build from a yaml-filename"
    build_directories(os.path.join(asname.split('/')[:-1]))
    yaml_from_file = read_yaml(filename)
    test = Interpreter() 
    test.definitions_interpreter(yaml_from_file)
    
    write_to_py(test.export_yaml(),asname)

def Build_OAS(filename,asname='test/main.py'):
    #TODO: proper parent-build
    workdir= os.path.dirname(filename)
    print(workdir)
    yaml_from_file = read_yaml(filename)
    #build_directories(reduce(lambda x,y: os.path.join(x,y),asname.split('/')[:-1]))
    test = OAS(yaml_from_file,workdir)
    test.build_oas(yaml_from_file)
    #write_to_py(test.export_as_filetree(),asname)
    export_ready= test.export_as_filetree()
    #print('this',export_ready)
    build_directories(export_ready,'test')

    
#%% Magic. 

       

if __name__ == '__main__':
    """
    If you want to execute this, run: 
    > python thisfile.py yaml-source target-app-name
    Path-resolution in case meeting any outwards dependencies 
    #TODO: 
    - args : target folder. 
    """
    yaml_file = sys.argv[1]
    # if OAS run build-oas 
    
    # else: run yaml-build. 
    
    # 
    