#!/usr/bin/env python3

"""
#TODO: Come up with proper statement etc. here. 
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce

class archiveFormat(str,Enum):
    """
    The type of archive. Currently only supporting zip files.
    """
    zip = 'zip'

class AnswerDTO(BaseModel):
    '''
    no description
    '''
    pass

class AnswerListDTO(BaseModel):
    '''
    no description
    '''
    pass

class id(BaseModel):
    '''
    Unique identifier for the object.
    '''
    pass

class userId(BaseModel):
    '''
    Unique identifier for a user.
    '''
    pass

class timestamp(BaseModel):
    '''
    Date and Time at which the object was created. Measured in seconds since the Unix epoch.
    '''
    pass
class ExerciseTypes(str,Enum):
    """
    Different kinds of exercises.
    """
    freeform = 'free_form'
    multiplechoice = 'multiple_choice'
    fillintheblank = 'fill_in_the_blank'
    commandline = 'command_line'
    codesnippet = 'code_snippet'
    codebase = 'codebase'
    database = 'database'
    codereview = 'code_review'

class AnswerTypes(BaseModel):
    '''
    The shape of an answer is based on the type of exercise (and, potentially at some point, a choice of expression selected by the user).
    '''
    __root__: ExerciseTypes
    pass

class Answer(BaseModel):
    '''
    An answer provides a potential solution produced in response to interpreting 
an exercise. In other words, it's a response that attempts to answer the 
problem stated in the exercise description.

    '''
    id: id = Field(..., description="no description")
    creator: userId = Field(None, description="no description")
    exerciseid: id = Field(None, description="no description")
    created: timestamp = Field(..., description="no description")
    status: str = Field(..., description="Correction/validation stage, going by whether the answer has been.")
    type: AnswerTypes = Field(..., description="no description")

class FreeFormAnswer(BaseModel):
    '''
    ... constituting an answer to a `Free Form Exercise`.
    '''
    __root__: Answer
    pass

class FreeFormAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: FreeFormAnswer
    pass

class MultipleChoiceAnswer(BaseModel):
    '''
    ... constituting an answer to a `Multiple Choice Exercise`.
    '''
    __root__: Answer
    pass

class MultipleChoiceAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: MultipleChoiceAnswer
    pass

class FillInTheBlankAnswer(BaseModel):
    '''
    ... constituting an answer to a `Fill In The Blank Exercise`.
    '''
    __root__: Answer
    pass

class FillInTheBlankAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: FillInTheBlankAnswer
    pass

class CommandLineAnswer(BaseModel):
    '''
    ... constituting an answer to a `Command Line Exercise`.
    '''
    __root__: Answer
    pass

class CommandLineAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: CommandLineAnswer
    pass

class CodeSnippetAnswer(BaseModel):
    '''
    ... constituting an answer to a `Code Snippet Exercise`.
    '''
    __root__: Answer
    pass

class CodeSnippetAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: CodeSnippetAnswer
    pass

class CodebaseAnswer(BaseModel):
    '''
    Files and folders (filesystem) constituting an answer to a `Codebase Exercise`.
    '''
    __root__: Answer
    archive: str = Field(..., description="The answer in the form of an archived file system.")
    archiveformat: archiveFormat = Field(..., description="The type of archive. Currently only supporting zip files.")

class CodebaseAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: CodebaseAnswer
    pass

class DatabaseAnswer(BaseModel):
    '''
    ... constituting an answer to a `Database Exercise`.
    '''
    __root__: Answer
    pass

class DatabaseAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: DatabaseAnswer
    pass

class CodeReviewAnswer(BaseModel):
    '''
    ... constituting an answer to a `Code Review Exercise`.
    '''
    __root__: Answer
    pass

class CodeReviewAnswerDTO(BaseModel):
    '''
    no description
    '''
    __root__: CodeReviewAnswer
    pass