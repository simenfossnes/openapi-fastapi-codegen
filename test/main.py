#!/usr/bin/env python3

"""
Project: User Grouping Service
OpenAPI: 3.0.2
----
```User Grouping Service```
version: 0.1.0
contact: {'name': 'Developer @Sci-Code', 'url': 'https://sci-code.com', 'email': 'developer@sci-code.com'}
description: User Grouping is about dividing users into a number
of groups such that users in the same groups are more similar
to other users in the same group than those in other groups.
In simple words, the aim is to groups users that share certain traits
into clusters.

# Introduction

The User Grouping service allows us to group users in various
ways, using different techniques. We can assign users to certain
data structures, or we can group them algoritmically using various
clustering algorithms.

# Authentication

This API supports OAuth2, and more specifically, the implicit flow.
license: {'name': 'Copyright © Sci-Code Inc. All Rights Reserved', 'url': 'https://sci-code.com'}
        
----
[{'name': 'Organizations', 'description': "The ```Organizations``` object holds information about an Organization\nand it's members. It is one of the core groups that users on the platfrom \ncan be a part of. We have different types of organizations; everything from \ncompanies to NGOs to government agencies.\n"}]
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



## Imports should be handled,
## In testing phase now. 
from . import * # this is sorta blind import of everything from the main-init...



@app.post("/organizations")
async def post_organizations(OrganizationDTO):
    """
    none
    """
    return None
        

@app.get("/organizations")
async def get_organizations():
    """
    none
    """
    return None
        

@app.get("/organizations/{id}")
async def get_organizationsid():
    """
    none
    """
    return None
        

@app.put("/organizations/{id}")
async def put_organizationsid(OrganizationDTO):
    """
    none
    """
    return None
        
        
        
        