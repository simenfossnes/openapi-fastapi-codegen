#!/usr/bin/env python3

"""
#TODO: Come up with proper statement etc. here. 
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple,NewType
from functools import reduce

class type(str,Enum):
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    file = 'file'
class fileFormat(str,Enum):
    """
    The specific information encoding method used.
    """
    jpg = 'jpg'
    png = 'png'


fileUpload = NewType("fileUpload",str)            


class OrganizationBranding(BaseModel):
    '''
    The branding associated with the organization.
    '''
    icon: File = Field(None, description="An icon for the organization. Must be square and at least 128px x 128px.")
    logo: File = Field(None, description="A logo for the organization that will be used in on pages. Must be at least 128px x 128px.")
    primarycolor: str = Field(None, description="A CSS hex color value representing the primary branding color for this organization.")


OrganizationType = NewType("OrganizationType",str)            


class Organization(BaseModel):
    '''
    An organized group of people with a particular purpose, such as a business, government agency, non-profit, etc.
    '''
    id: id = Field(..., description="no description")
    name: str = Field(..., description="The name of the orgnization.")
    organizationnumber: str = Field(None, description="The number issued by the government, proving that the organization exists.")
    visionstatement: str = Field(None, description="A short, descriptive text of what future the organization aims to bring about.")
    type: OrganizationType = Field(..., description="no description")
    organizationbranding: OrganizationBranding = Field(None, description="no description")
    icon: fileUpload = Field(None, description="File upload. An icon for the organization. Must be square and at least 128px x 128px.")
    logo: fileUpload = Field(None, description="File Upload. A logo for the organization that will be used in on pages. Must be at least 128px x 128px.")


id = NewType("id",str)            



timestamp = NewType("timestamp",None)            


class File(BaseModel):
    '''
    An object with information about a file.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    title: str = Field(None, description="A user friendly title for the file.")
    filename: str = Field(None, description="A filename for the file, suitable for saving to a filesystem.")
    type: type = Field(..., description="String representing the object's type. Objects of the same type share the same value.")
    size: None = Field(..., description="The size in bytes of the file object.")
    fileformat: fileFormat = Field(None, description="The specific information encoding method used.")
    url: str = Field(..., description="The URL from which the file can be downloaded using your live secret API key.")


OrganizationDTO = NewType("OrganizationDTO",None)            
