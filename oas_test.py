#!/usr/bin/env python3

"""
Project: Answer Service
OpenAPI: 3.0.2
----
```Answer Service```
version: 0.1.0
contact: {'name': 'Developer @Sci-Code', 'url': 'https://sci-code.com', 'email': 'developer@sci-code.com'}
description: Answers are responses to exercises. Some of them are correct, some of them not.
The Answer Service deals with everything that's necessary to keep track of 
answers to exercises over time. 

# Introduction

The answers service handles some advanced processing of certain answers. For example, an 
answer to the popular codebase exercise type requires processing of archived files usually
in a zip file, and then a translation into multiple post requests for each file that has 
changed since the last posted answer to the same exercise.

# Answer Types

The structure of answers depends on the exercise types they answer. The exercise 
types which form the basis for answer types can be seen below.

<p align="center">
  <img alt="exercise types" src="/spec-assets/exercise-types.svg" />
</p>

# Authentication

This API supports OAuth2, and more specifically, the implicit flow.

license: {'name': 'Copyright © Sci-Code Inc. All Rights Reserved', 'url': 'https://sci-code.com'}
        
----
[{'name': 'Answers', 'description': 'An answer to an exercise. Exercises can sometimes\ncombine together to form more advanced structures.\n\nE.g. Many codebase exercises combined in sequence \nform a project. Projects can be used \n(and useful) both for teaching and assessment.\n'}]
"""
from enum import Enum
from functools import reduce
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from starlette.responses import JSONResponse
#from DataModel import * # DockerFile places this in app-directory but not really necessary ? 

app = FastAPI()


from src import *
############
# Requests #
############   

@app.post("/answers")
async def post_answers(AnswerDTO):
    """
    none
    """
    
    return SomeRoute(AnswerDTO)
        

@app.get("/answers")
async def get_answers():
    """
    none
    """
    return None
        

@app.get("/answers/{id}")
async def get_answersid():
    """
    none
    """
    return None
        
        
        
        