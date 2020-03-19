#!/usr/bin/env python3

"""
#TODO: Come up with proper statement etc. here. 
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple,NewType
from functools import reduce



id = NewType("id",str)            



userId = NewType("userId",str)            



timestamp = NewType("timestamp",None)            



ExerciseTypes = NewType("ExerciseTypes",str)            

class archiveFormat(str,Enum):
    """
    The type of archive. Currently only supporting zip files.
    """
    zip = 'zip'



AnswerDTO = NewType("AnswerDTO",Union[c,c,c,c,c,c,c,c])            




AnswerTypes = NewType("AnswerTypes",None)            


class Answer(BaseModel):
    '''
    An answer provides a potential solution produced in response to interpreting 
an exercise. In other words, it's a response that attempts to answer the 
problem stated in the exercise description.

    '''
    id: d = Field(..., description="no description")
    creator: d = Field(None, description="no description")
    exerciseid: d = Field(None, description="no description")
    created: d = Field(..., description="no description")
    status: str = Field(..., description="Correction/validation stage, going by whether the answer has been.")
    type: d = Field(..., description="no description")


FreeFormAnswer = NewType("FreeFormAnswer",None)            



FreeFormAnswerDTO = NewType("FreeFormAnswerDTO",None)            



MultipleChoiceAnswer = NewType("MultipleChoiceAnswer",None)            



MultipleChoiceAnswerDTO = NewType("MultipleChoiceAnswerDTO",None)            



FillInTheBlankAnswer = NewType("FillInTheBlankAnswer",None)            



FillInTheBlankAnswerDTO = NewType("FillInTheBlankAnswerDTO",None)            



CommandLineAnswer = NewType("CommandLineAnswer",None)            



CommandLineAnswerDTO = NewType("CommandLineAnswerDTO",None)            



CodeSnippetAnswer = NewType("CodeSnippetAnswer",None)            



CodeSnippetAnswerDTO = NewType("CodeSnippetAnswerDTO",None)            


class CodebaseAnswer(BaseModel):
    '''
    Files and folders (filesystem) constituting an answer to a `Codebase Exercise`.
    '''
    __root__: d
    archive: str = Field(..., description="The answer in the form of an archived file system.")
    archiveformat: archiveFormat = Field(..., description="The type of archive. Currently only supporting zip files.")


CodebaseAnswerDTO = NewType("CodebaseAnswerDTO",None)            



DatabaseAnswer = NewType("DatabaseAnswer",None)            



DatabaseAnswerDTO = NewType("DatabaseAnswerDTO",None)            



CodeReviewAnswer = NewType("CodeReviewAnswer",None)            



CodeReviewAnswerDTO = NewType("CodeReviewAnswerDTO",None)            



AnswerListDTO = NewType("AnswerListDTO",List[Union[c,c,c,c,c,c,c,c]])            
