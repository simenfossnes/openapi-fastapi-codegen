


#!/usr/bin/env python3
"""
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce

class _title(str,Enum):
    """
    A description of how you like to receive feedback. This is different from person to person.
    """
    clear, to the point - no fluff = 'clear, to the point - no fluff'
    positive & constructive = 'positive & constructive'

class Jobseekerstatus(str,Enum):
    """
    the current job status of the user
    """
    actively seeking = 'Actively Seeking'
    not available = 'Not available'
    open to offers = 'Open to Offers'

class Visibility(str,Enum):
    """
    Whether or not to show the test case.
    """
    fully hidden = 'Fully Hidden'
    partially hidden = 'Partially Hidden'
    visible = 'Visible'

class Difficulty(str,Enum):
    """
    The difficulty level of the challenge.
    """
    advanced = 'Advanced'
    beginner = 'Beginner'
    intermediate = 'Intermediate'

class Type(str,Enum):
    """
    The type of challenge.
    """
    live quiz = 'Live Quiz'
    online project = 'Online Project'

class Id(BaseModel):
    '''
    Unique identifier for the object.
    '''
    pass


class Userid(BaseModel):
    '''
    Unique identifier for a user.
    '''
    pass


class Timestamp(BaseModel):
    '''
    Date and Time at which the object was created. Measured in seconds since the Unix epoch.
    '''
    pass


class Currency(BaseModel):
    '''
    A three-letter [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, in lowercase. We currently support `nok`, `eur` and `usd` only.
    '''
    pass


class Object(BaseModel):
    '''
    String representing the object’s type. Objects of the same type share the same value.
    '''
    pass


class Country(BaseModel):
    '''
    A two-letter ISO code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), representing the country.
    '''
    pass


class Language(BaseModel):
    '''
    A two-letter ISO code ([ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3)), representing the language.
    '''
    pass


class Url(BaseModel):
    '''
    A universal resource identifier (URI), according to the [RFC3986](https://tools.ietf.org/html/rfc3986) standard.
    '''
    pass


class Price(BaseModel):
    '''
    The cost of something in a certain currency.
    '''
    amount: int = Field(None, description="A positive integer in the smallest currency unit (that is,  100 cents for $1.00, or 1 for ¥1, Japanese Yen being a  zero-decimal currency)")
    currency: None = Field(None, description="no description")


class Address(BaseModel):
    '''
    Details about where someone or something is situated.
    '''
    city: str = Field(None, description="City, district, suburb, town, or village.")
    country: None = Field(None, description="no description")
    line1: str = Field(None, description="Address line 1 (e.g., street, PO Box, or company name).")
    line2: str = Field(None, description="Address line 2 (e.g., apartment, suite, unit, or building).")
    postal_code: str = Field(None, description="ZIP or postal code.")
    state: str = Field(None, description="State, county, province, or region.")


class Metadata(BaseModel):
    '''
    Set of key-value pairs that you can attach to an object. This 
can be useful for storing additional information about the 
object in a structured format.
    '''
    pass


class Language(BaseModel):
    '''
    no description
    '''
    languageCode: str = Field(..., description="Unique identifier for the language")
    nativeName: str = Field(..., description="The name in navige tongue")
    englishName: str = Field(..., description="The name of the language in")
    flagSrc: str = Field(..., description="A link to a flag image representing that language")


class Programminglanguage(BaseModel):
    '''
    A structure of the programming langague
    '''
    name: str = Field(..., description="The name of the programming language.")
    logoUrl: str = Field(..., description="A url to the logo of the language.")


class User(BaseModel):
    '''
    The basic data structure given by Auth0.
    '''
    user_id: str = Field(..., description="ID of the user which can be used when interacting with other APIs.")
    email: str = Field(..., description="Email address of this user.")
    email_verified: bool = Field(..., description="Whether this email address is verified (true) or unverified (false).")
    username: str = Field(..., description="Username of this user.")
    phone_number: str = Field(..., description="Phone number for this user when using SMS connections. Follows the E.164 recommendation.")
    phone_verified: bool = Field(..., description="Whether this phone number has been verified (true) or not (false).")
    created_at: str = Field(..., description="Date and time when this user was created (ISO_8601 format).")
    updated_at: str = Field(..., description="Date and time when this user was last updated/modified (ISO_8601 format).")
    identities: List[str] = Field(..., description="Array of user identity objects when accounts are linked.")
    app_metadata: None = Field(..., description="Stores user attributes such as preferences that do not impact a user's core functionality.")
    user_metadata: None = Field(..., description="Stores information (such as, support plan subscriptions, security roles, or access control groups) that can impact a user's core functionality.")
    picture: str = Field(..., description="URL to picture, photo, or avatar of this user.")
    name: str = Field(..., description="Name of this user.")
    nickname: str = Field(..., description="Preferred nickname or alias of this user.")
    multifactor: List[str] = Field(..., description="List of multi-factor authentication providers with which this user has enrolled.")
    last_ip: str = Field(..., description="Last IP address from which this user logged in.")
    last_login: str = Field(..., description="Last date and time this user logged in (ISO_8601 format).")
    logins_count: int = Field(..., description="Total number of logins this user has performed.")
    blocked: bool = Field(..., description="Whether this user was blocked by an administrator (true) or is not (false).")
    given_name: str = Field(..., description="Given name/first name/forename of this user.")
    family_name: str = Field(..., description="Family name/last name/surname of this user.")


class Usermetadata(BaseModel):
    '''
    Stores user attributes such as preferences that do not impact a user's
core functionality.
    '''
    skills: List[str] = Field(..., description="a set of tags meant to reperesent skills")
    feedbackPreference: _title = Field(None, description="A description of how you like to receive feedback. This is different from person to person.")
    jobSeekerStatus: Jobseekerstatus = Field(..., description="the current job status of the user")
    programmingLangauges: List[str] = Field(..., description="the current job status of the user")


class Appmetadata(BaseModel):
    '''
    Stores information (such as, support plan subscriptions, security roles,
or access control groups) that can impact a user's core functionality.
    '''
    plan: str = Field(..., description="no description")


class Identity(BaseModel):
    '''
    no description
    '''
    connection: str = Field(..., description="no description")
    user_id: str = Field(..., description="no description")
    provider: str = Field(..., description="no description")
    isSocial: bool = Field(..., description="no description")


class Organization(BaseModel):
    '''
    An organized group of people with a particular purpose, such as a business, government agency, non-profit, etc.
    '''
    id: None = Field(..., description="no description")
    name: str = Field(..., description="The name of the orgnization.")
    extra info: str = Field(None, description="The number given, proving that the organization exists.")
    visionStatement: str = Field(None, description="A short, descriptive text of what future the organization aims to bring about.")
    type: None = Field(..., description="no description")
    logoUrl: None = Field(..., description="no description")


class Type(BaseModel):
    '''
    The type of challenge.
    '''
    pass


class Expression(BaseModel):
    '''
    An expression is a captured moment of menaingful communication - in a speficic medium and/or form.
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    type: None = Field(..., description="no description")


class Text expression(BaseModel):
    '''
    Expressions captured in rich text.
    '''
    pass


class Math expression(BaseModel):
    '''
    Expressions captured in mathematical notation.
    '''
    pass


class Code expression(BaseModel):
    '''
    Expressions captured in various coding languages.
    '''
    pass


class Image expression(BaseModel):
    '''
    Expressions captured in image form.
    '''
    pass


class Audio expression(BaseModel):
    '''
    Expressions captured in the form of sound.
    '''
    pass


class Animation expression(BaseModel):
    '''
    Expressions captured in image sequence form; without sound.
    '''
    pass


class Video expression(BaseModel):
    '''
    Expressions captured in video form.
    '''
    pass


class Exercise(BaseModel):
    '''
    An exercise introduces you to, and invites you to complete, a specific activity.
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    promoImage: None = Field(None, description="no description")
    description: List[str] = Field(..., description="A set of expressions combined to form a rich description of the activity requested.")
    type: None = Field(..., description="no description")


class Free form exercise(BaseModel):
    '''
    An exercise expecting a free-form text answer.
    '''
    pass


class Multiple choice exercise(BaseModel):
    '''
    An exercise providing multiple choices, of which one or more is correct.
    '''
    pass


class Fill in the blank exercise(BaseModel):
    '''
    An exercise providing text with blnak fields to fill in.
    '''
    pass


class Command line exercise(BaseModel):
    '''
    An exercise where your write a command in the command line.
    '''
    pass


class Code snippet exercise(BaseModel):
    '''
    An exercise expecting a single file of code (a snippet, aka. gist) as the answer.
    '''
    pass


class Codebase exercise(BaseModel):
    '''
    An exercise expecting an entire codebase (multiple files and folders) as the answer.
    '''
    pass


class Database exercise(BaseModel):
    '''
    An exercise where you perform various database operations such as a query.
    '''
    pass


class Code review exercise(BaseModel):
    '''
    An exercise where you review some code, leave comments, etc.
    '''
    pass


class Answer(BaseModel):
    '''
    An answer provides a potential solution produced in response to interpreting 
an exercise. In other words, it's a response that attempts to answer the 
problem stated in the exercise description.

    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    status: str = Field(..., description="Correction/validation stage, going by whether the answer has been.")
    type: None = Field(..., description="no description")


class Answertypes(BaseModel):
    '''
    no description
    '''
    pass


class Codebase answer(BaseModel):
    '''
    Files and folders (filesystem) constituting an answer to a `Codebase Exercise`.
    '''
    pass


class Correctionblueprint(BaseModel):
    '''
    The blueprint for how to correct an answer to an exercise.
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    type: None = Field(..., description="no description")
    allowAutomaticCorrection: bool = Field(None, description="Whether to allow automatic correction or not.")
    allowManualCorrection: bool = Field(None, description="Whether to allow manual correction or not.")
    allowAICorrection: bool = Field(None, description="Whether to allow artificial intelligence correction or not.")
    requirements: List[str] = Field(..., description="A list of requirements to be corrected for")


class Requirement(BaseModel):
    '''
    <comment placeholder>
    '''
    id: None = Field(..., description="no description")
    title: str = Field(..., description="A indicative text for the requirement.")
    description: str = Field(None, description="A text with more detailed information about the requirement.")
    weight: int = Field(None, description="A number signifying the importance of the")
    automaticTests: List[str] = Field(None, description="The automatic test cases to run to correct for the requirement.")
    failureResponses: List[str] = Field(..., description="A set of potential feedback objects to display to students upon failing requirement.")


class Testcase(BaseModel):
    '''
    The tests used to automaticaly correct the requirements
    '''
    id: None = Field(..., description="no description")
    type: None = Field(..., description="no description")
    visibility: Visibility = Field(..., description="Whether or not to show the test case.")
    explainCommonErrors: bool = Field(..., description="Whether or not to explain universal and common errors.")
    studentDebuggingInfo: None = Field(..., description="no description")
    successThreshold: int = Field(..., description="The percentage required to consider the test case passed.")


class Test case types(BaseModel):
    '''
    the typue of test case
    '''
    pass


class Iotestcase(BaseModel):
    '''
    A test case definition for performing I/O testing. These are langauge agnostic.
    '''
    pass


class Unittestcase(BaseModel):
    '''
    A test case definition for performing unit testing. All the code should be imported to allow for running the unit test on any piece of the codebase.
    '''
    pass


class Customtestcase(BaseModel):
    '''
    A test case definition for performing custom testing
    '''
    pass


class Codequalitytestcase(BaseModel):
    '''
    More general test case definition for code quality
    '''
    pass


class Debugging info(BaseModel):
    '''
    The tests used to automaticaly correct the requirements
    '''
    showTestCaseInput: bool = Field(..., description="Whether to show the input to the student or not.")
    showCompilerStackTrace: bool = Field(..., description="Whether to show the compiler/debug output to the student or not.")
    showExercutionStackTrace: bool = Field(..., description="Whether to show the exercution output to the student or not.")
    showStudentSolutionOutput: bool = Field(..., description="Whether to show the output of the student's code to the student or not.")
    showExpectedSolutionOutput: bool = Field(..., description="Whether to show the expected output to the student or not.")
    showOutputDifference: bool = Field(..., description="Whether to show the difference between the supplied and expected output to the student or not.")


class Correction history(BaseModel):
    '''
    The object containing the history of users's exercise answer corrections
    '''
    exerciseId: None = Field(..., description="no description")
    userId: None = Field(..., description="no description")
    corrections: List[str] = Field(..., description="A collection of performed corrections.")


class Correctionrecord(BaseModel):
    '''
    The model for a recorded correction result.
    '''
    id: None = Field(..., description="no description")
    type: None = Field(..., description="no description")


class Correction record type(BaseModel):
    '''
    the typue of test case
    '''
    pass


class Autmaticcorrectionrecord(BaseModel):
    '''
    The model for recorded automatic correction results.
    '''
    pass


class Manual correction record(BaseModel):
    '''
    The model for a recorded manual correction results.
    '''
    pass


class Ai correction record(BaseModel):
    '''
    The model for a recorded AI correction results.
    '''
    pass


class Feedback(BaseModel):
    '''
    Content and emotion produced in reaction to something. The materialization of something felt or thought in response to a situation or event. It can be affirmative, constructive, etc.
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    emoji: str = Field(None, description="A representation of the emotional state associated with the feedback message.")
    description: List[str] = Field(..., description="A set of expressions combined to form a rich feedback message.")


class Challenge(BaseModel):
    '''
    Basically a set of exercises combined for the purpose of testing skills.
    '''
    id: None = Field(..., description="no description")
    object: None = Field(None, description="no description")
    type: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    title: str = Field(..., description="A short text describing the challenge.")
    tagline: str = Field(..., description="A short add-on text, adding more details to the title.")
    description: List[str] = Field(None, description="A in-depth text describing the challenge.")
    description: List[str] = Field(None, description="A set of keywords related to the challenge.")
    promoImage: str = Field(..., description="A visual description of the challenge.")
    promoVideo: str = Field(None, description="In-depth stimulating descrpitionof the challenge.")
    duration: int = Field(None, description="Total time, measured in seconds")
    difficulty: Difficulty = Field(None, description="The difficulty level of the challenge.")
    langauges: List[str] = Field(None, description="The supported languages for this challenge.")
    exercises: List[str] = Field(None, description="The exercises making up the challenge.")
    organizers: List[str] = Field(..., description="The organization(s) hosting the challenge")


class Challengedescriptionsection(BaseModel):
    '''
    no description
    '''
    headline: str = Field(None, description="The headline of the section.")
    bodycopy: str = Field(None, description="Approximately a paragraph of text describing the section.")
    label: str = Field(None, description="A piece of text describing the section.")
    featuredExpression: None = Field(None, description="no description")


class Onlineproject_challenge(BaseModel):
    '''
    Online project challenge.
    '''
    id: str = Field(..., description="Unique identifier for the object.")
    created: str = Field(..., description="Date and Time at which the object was created. Measured in seconds since the Unix epoch.")
    title: str = Field(..., description="A short text describing the challenge.")
    tagline: str = Field(..., description="A short add-on text, adding more details to the title.")
    description: str = Field(None, description="A in-depth text describing the challenge.")
    promoImage: str = Field(..., description="A visual description of the challenge.")
    promoVideo: str = Field(None, description="In-depth stimulating descrpitionof the challenge.")
    duration: int = Field(None, description="Total time, measured in seconds")
    difficulty: Difficulty = Field(None, description="The difficulty level of the challenge.")
    langauges: List[str] = Field(None, description="The supported languages for this challenge.")
    type: Type = Field(..., description="The type of challenge.")
    organizers: List[str] = Field(..., description="The organization(s) hosting the challenge")


class Livequiz_challenge(BaseModel):
    '''
    Live quiz challenge
    '''
    id: str = Field(..., description="Unique identifier for the object.")
    created: str = Field(..., description="Date and Time at which the object was created. Measured in seconds since the Unix epoch.")
    title: str = Field(..., description="A short text describing the challenge.")
    tagline: str = Field(..., description="A short add-on text, adding more details to the title.")
    description: str = Field(None, description="A in-depth text describing the challenge.")
    promoImage: str = Field(..., description="A visual description of the challenge.")
    promoVideo: str = Field(None, description="In-depth stimulating descrpitionof the challenge.")
    duration: int = Field(None, description="Total time, measured in seconds")
    difficulty: Difficulty = Field(None, description="The difficulty level of the challenge.")
    langauges: List[str] = Field(None, description="The supported languages for this challenge.")
    type: Type = Field(..., description="The type of challenge.")
    organizers: List[str] = Field(..., description="The organization(s) hosting the challenge")


class Course(BaseModel):
    '''
    a collection of expressions and exercises combined for the purpose of teaching something.
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    type: None = Field(..., description="no description")
    title: str = Field(..., description="The title of the course")
    tagline: str = Field(..., description=no description)
    description: List[str] = Field(..., description="A rich description of the course using an array of expressions")
    promoVideo: str = Field(None, description="A promo video to introduce the course.")
    promoImage: str = Field(None, description="A promo image to make people interested in the course.")


class Course types(BaseModel):
    '''
    Different types of courses.
    '''
    pass


class Book(BaseModel):
    '''
    Uhm... a book. That's what this represents.
    '''
    pass


class Chapter(BaseModel):
    '''
    no description
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    title: str = Field(..., description="The title of the chapter")
    parent: str = Field(..., description="The id of the parent chapeter.")
    treeIndex: str = Field(..., description="The placement in the chapter hieararchy.")
    contentAdapters: List[str] = Field(..., description="The content found inside the chapter.")


class Project(BaseModel):
    '''
    A project is a practically-oriented course.
    '''
    pass


class Iteration(BaseModel):
    '''
    <comment placeholder>
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    title: str = Field(..., description="The title of the iteration.")
    description: str = Field(..., description="A description of the iteration.")
    promoVideo: str = Field(..., description="A video showing how the product should look after the iteration.")
    exercise: None = Field(..., description="no description")


class Contentadapter(BaseModel):
    '''
    no description
    '''
    id: None = Field(..., description="no description")
    created: None = Field(..., description="no description")
    expression: None = Field(..., description="The main part of the content adapter; an expression.")
    exercises: List[str] = Field(..., description="The exercises connected to the expression, through the content adapter.")      

        