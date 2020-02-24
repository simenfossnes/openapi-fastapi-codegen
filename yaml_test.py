


#!/usr/bin/env python3
"""
Generic Statement to be inserted here... 
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Tuple
from functools import reduce

###################
# Enums and Types #
###################
class currency(str,Enum):
    """
    A three-letter [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, in lowercase. We currently support `nok`, `eur` and `usd` only.
    """
    nok = 'nok'
    eur = 'eur'
    usd = 'usd'

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

class feedbackPreference(str,Enum):
    """
    A description of how you like to receive feedback. This is different from person to person.
    """
    clear_to_the_point___no_fluff = 'clear, to the point - no fluff'
    positive_and_constructive = 'positive & constructive'

class jobSeekerStatus(str,Enum):
    """
    the current job status of the user
    """
    actively_seeking = 'Actively Seeking'
    not_available = 'Not available'
    open_to_offers = 'Open to Offers'

class OrganizationType(str,Enum):
    """
    The type of organization.
    """
    company = 'company'
    ngo = 'ngo'
    igo = 'igo'
    non_profit = 'non-profit'
    governmentdepartment = 'government_department'
    governmentagency = 'government_agency'

class ExpressionTypes(str,Enum):
    """
    Different kinds of expressions.
    """
    text = 'text'
    math = 'math'
    code = 'code'
    image = 'image'
    audio = 'audio'
    animation = 'animation'
    video = 'video'

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

class visibility(str,Enum):
    """
    Whether or not to show the test case.
    """
    fully_hidden = 'Fully Hidden'
    partially_hidden = 'Partially Hidden'
    visible = 'Visible'

class TestCaseTypes(str,Enum):
    """
    the typue of test case
    """
    codequality = 'code_quality'
    custom = 'custom'
    io = 'io'
    unit = 'unit'

class CorrectionRecordType(str,Enum):
    """
    the typue of test case
    """
    automatic = 'automatic'
    manual = 'manual'
    ai = 'ai'

class difficulty(str,Enum):
    """
    The difficulty level of the challenge.
    """
    advanced = 'Advanced'
    beginner = 'Beginner'
    intermediate = 'Intermediate'

class ChallengeTypes(str,Enum):
    """
    The type of challenge.
    """
    livequiz = 'live_quiz'
    onlineproject = 'online_project'

class CourseTypes(str,Enum):
    """
    Different types of courses.
    """
    article = 'article'
    book = 'book'
    project = 'project'
    videoseries = 'video_series'
##########
# Models #
##########
# independent Models:

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


class object(BaseModel):
    '''
    String representing the object’s type. Objects of the same type share the same value.
    '''
    pass


class country(BaseModel):
    '''
    A two-letter ISO code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), representing the country.
    '''
    pass


class language(BaseModel):
    '''
    A two-letter ISO code ([ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3)), representing the language.
    '''
    pass


class url(BaseModel):
    '''
    A universal resource identifier (URI), according to the [RFC3986](https://tools.ietf.org/html/rfc3986) standard.
    '''
    pass


class Price(BaseModel):
    '''
    The cost of something in a certain currency.
    '''
    amount: int = Field(None, description="A positive integer in the smallest currency unit (that is,  100 cents for $1.00, or 1 for ¥1, Japanese Yen being a  zero-decimal currency)")
    currency: currency = Field(None, description="no description")


class Address(BaseModel):
    '''
    Details about where someone or something is situated.
    '''
    city: str = Field(None, description="City, district, suburb, town, or village.")
    country: country = Field(None, description="no description")
    line1: str = Field(None, description="Address line 1 (e.g., street, PO Box, or company name).")
    line2: str = Field(None, description="Address line 2 (e.g., apartment, suite, unit, or building).")
    postalcode: str = Field(None, description="ZIP or postal code.")
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
    languagecode: str = Field(..., description="Unique identifier for the language")
    nativename: str = Field(..., description="The name in navige tongue")
    englishname: str = Field(..., description="The name of the language in")
    flagsrc: str = Field(..., description="A link to a flag image representing that language")


class ProgrammingLanguage(BaseModel):
    '''
    A structure of the programming langague
    '''
    name: str = Field(..., description="The name of the programming language.")
    logourl: str = Field(..., description="A url to the logo of the language.")


class File(BaseModel):
    '''
    An object with information about a file.
    '''
    id: timestamp = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    title: str = Field(None, description="A user friendly title for the file.")
    filename: str = Field(None, description="A filename for the file, suitable for saving to a filesystem.")
    type: type = Field(..., description="String representing the object's type. Objects of the same type share the same value.")
    size: None = Field(..., description="The size in bytes of the file object.")
    fileformat: fileFormat = Field(None, description="The specific information encoding method used.")
    url: str = Field(..., description="The URL from which the file can be downloaded using your live secret API key.")


class User(BaseModel):
    '''
    The basic data structure given by Auth0.
    '''
    userid: str = Field(..., description="ID of the user which can be used when interacting with other APIs.")
    email: str = Field(..., description="Email address of this user.")
    emailverified: bool = Field(..., description="Whether this email address is verified (true) or unverified (false).")
    username: str = Field(..., description="Username of this user.")
    phonenumber: str = Field(..., description="Phone number for this user when using SMS connections. Follows the E.164 recommendation.")
    phoneverified: bool = Field(..., description="Whether this phone number has been verified (true) or not (false).")
    createdat: str = Field(..., description="Date and time when this user was created (ISO_8601 format).")
    updatedat: str = Field(..., description="Date and time when this user was last updated/modified (ISO_8601 format).")
    identities: List[Identity] = Field(..., description="Array of user identity objects when accounts are linked.")
    appmetadata: AppMetadata = Field(..., description="Stores user attributes such as preferences that do not impact a user's core functionality.")
    usermetadata: UserMetadata = Field(..., description="Stores information (such as, support plan subscriptions, security roles, or access control groups) that can impact a user's core functionality.")
    picture: str = Field(..., description="URL to picture, photo, or avatar of this user.")
    name: str = Field(..., description="Name of this user.")
    nickname: str = Field(..., description="Preferred nickname or alias of this user.")
    multifactor: List[str] = Field(..., description="List of multi-factor authentication providers with which this user has enrolled.")
    lastip: str = Field(..., description="Last IP address from which this user logged in.")
    lastlogin: str = Field(..., description="Last date and time this user logged in (ISO_8601 format).")
    loginscount: int = Field(..., description="Total number of logins this user has performed.")
    blocked: bool = Field(..., description="Whether this user was blocked by an administrator (true) or is not (false).")
    givenname: str = Field(..., description="Given name/first name/forename of this user.")
    familyname: str = Field(..., description="Family name/last name/surname of this user.")


class UserMetadata(BaseModel):
    '''
    Stores user attributes such as preferences that do not impact a user's
core functionality.
    '''
    skills: List[str] = Field(..., description="a set of tags meant to reperesent skills")
    feedbackpreference: feedbackPreference = Field(None, description="A description of how you like to receive feedback. This is different from person to person.")
    jobseekerstatus: jobSeekerStatus = Field(..., description="the current job status of the user")
    programminglangauges: List[ProgrammingLanguage] = Field(..., description="the current job status of the user")


class AppMetadata(BaseModel):
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
    userid: str = Field(..., description="no description")
    provider: str = Field(..., description="no description")
    issocial: bool = Field(..., description="no description")


class Organization(BaseModel):
    '''
    An organized group of people with a particular purpose, such as a business, government agency, non-profit, etc.
    '''
    id: id = Field(..., description="no description")
    name: str = Field(..., description="The name of the orgnization.")
    organizationnumber: str = Field(None, description="The number given, proving that the organization exists.")
    visionstatement: str = Field(None, description="A short, descriptive text of what future the organization aims to bring about.")
    type: OrganizationType = Field(..., description="no description")
    organizationbranding: OrganizationBranding = Field(None, description="no description")


class OrganizationBranding(BaseModel):
    '''
    The branding associated with the organization.
    '''
    icon: None = Field(None, description="An icon for the account. Must be square and at least 128px x 128px.")
    logo: None = Field(None, description="A logo for the account that will be used in on pages. Must be at least 128px x 128px.")
    primarycolor: str = Field(None, description="A CSS hex color value representing the primary branding color for this account.")


class Expression(BaseModel):
    '''
    An expression is a captured moment of menaingful communication - in a speficic medium and/or form.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    type: ExpressionTypes = Field(..., description="no description")


class TextExpression(BaseModel):
    '''
    Expressions captured in rich text.
    '''
    pass


class MathExpression(BaseModel):
    '''
    Expressions captured in mathematical notation.
    '''
    pass


class CodeExpression(BaseModel):
    '''
    Expressions captured in various coding languages.
    '''
    pass


class ImageExpression(BaseModel):
    '''
    Expressions captured in image form.
    '''
    pass


class AudioExpression(BaseModel):
    '''
    Expressions captured in the form of sound.
    '''
    pass


class AnimationExpression(BaseModel):
    '''
    Expressions captured in image sequence form; without sound.
    '''
    pass


class VideoExpression(BaseModel):
    '''
    Expressions captured in video form.
    '''
    pass


class Exercise(BaseModel):
    '''
    An exercise introduces you to, and invites you to complete, a specific activity.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    promoimage: None = Field(None, description="no description")
    description: List[None] = Field(..., description="A set of expressions combined to form a rich description of the activity requested.")
    type: ExerciseTypes = Field(..., description="no description")


class FreeFormExercise(BaseModel):
    '''
    An exercise expecting a free-form text answer.
    '''
    pass


class MultipleChoiceExercise(BaseModel):
    '''
    An exercise providing multiple choices, of which one or more is correct.
    '''
    pass


class FillInTheBlankExercise(BaseModel):
    '''
    An exercise providing text with blnak fields to fill in.
    '''
    pass


class CommandLineExercise(BaseModel):
    '''
    An exercise where your write a command in the command line.
    '''
    pass


class CodeSnippetExercise(BaseModel):
    '''
    An exercise expecting a single file of code (a snippet, aka. gist) as the answer.
    '''
    pass


class CodebaseExercise(BaseModel):
    '''
    An exercise expecting an entire codebase (multiple files and folders) as the answer.
    '''
    pass


class DatabaseExercise(BaseModel):
    '''
    An exercise where you perform various database operations such as a query.
    '''
    pass


class CodeReviewExercise(BaseModel):
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
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    status: str = Field(..., description="Correction/validation stage, going by whether the answer has been.")
    type: AnswerTypes = Field(..., description="no description")


class AnswerTypes(BaseModel):
    '''
    no description
    '''
    pass


class CodebaseAnswer(BaseModel):
    '''
    Files and folders (filesystem) constituting an answer to a `Codebase Exercise`.
    '''
    pass


class CorrectionBlueprint(BaseModel):
    '''
    The blueprint for how to correct an answer to an exercise.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    type: ExerciseTypes = Field(..., description="no description")
    allowautomaticcorrection: bool = Field(None, description="Whether to allow automatic correction or not.")
    allowmanualcorrection: bool = Field(None, description="Whether to allow manual correction or not.")
    allowaicorrection: bool = Field(None, description="Whether to allow artificial intelligence correction or not.")
    requirements: List[Requirement] = Field(..., description="A list of requirements to be corrected for")


class Requirement(BaseModel):
    '''
    A specific element you expect to be part of a correct solution.
    '''
    id: id = Field(..., description="no description")
    title: str = Field(..., description="A indicative text for the requirement.")
    description: str = Field(None, description="A text with more detailed information about the requirement.")
    weight: int = Field(None, description="A number signifying the importance of the")
    automatictests: List[TestCase] = Field(None, description="The automatic test cases to run to correct for the requirement.")
    failureresponses: List[Feedback] = Field(..., description="A set of potential feedback objects to display to students upon failing requirement.")


class TestCase(BaseModel):
    '''
    The tests used to automaticaly correct the requirements
    '''
    id: id = Field(..., description="no description")
    type: TestCaseTypes = Field(..., description="no description")
    visibility: visibility = Field(..., description="Whether or not to show the test case.")
    explaincommonerrors: bool = Field(..., description="Whether or not to explain universal and common errors.")
    studentdebugginginfo: None = Field(..., description="no description")
    successthreshold: int = Field(..., description="The percentage required to consider the test case passed.")


class IOTestCase(BaseModel):
    '''
    A test case definition for performing I/O testing. These are langauge agnostic.
    '''
    pass


class UnitTestCase(BaseModel):
    '''
    A test case definition for performing unit testing. All the code should be imported to allow for running the unit test on any piece of the codebase.
    '''
    pass


class CustomTestCase(BaseModel):
    '''
    A test case definition for performing custom testing
    '''
    pass


class CodeQualityTestCase(BaseModel):
    '''
    More general test case definition for code quality
    '''
    pass


class DebuggingInfo(BaseModel):
    '''
    The tests used to automaticaly correct the requirements
    '''
    showtestcaseinput: bool = Field(..., description="Whether to show the input to the student or not.")
    showcompilerstacktrace: bool = Field(..., description="Whether to show the compiler/debug output to the student or not.")
    showexercutionstacktrace: bool = Field(..., description="Whether to show the exercution output to the student or not.")
    showstudentsolutionoutput: bool = Field(..., description="Whether to show the output of the student's code to the student or not.")
    showexpectedsolutionoutput: bool = Field(..., description="Whether to show the expected output to the student or not.")
    showoutputdifference: bool = Field(..., description="Whether to show the difference between the supplied and expected output to the student or not.")


class CorrectionHistory(BaseModel):
    '''
    The object containing the history of users's exercise answer corrections
    '''
    exerciseid: id = Field(..., description="no description")
    userid: userId = Field(..., description="no description")
    corrections: List[CorrectionRecord] = Field(..., description="A collection of performed corrections.")


class CorrectionRecord(BaseModel):
    '''
    The model for a recorded correction result.
    '''
    id: id = Field(..., description="no description")
    type: CorrectionRecordType = Field(..., description="no description")


class AutmaticCorrectionRecord(BaseModel):
    '''
    The model for recorded automatic correction results.
    '''
    pass


class ManualCorrectionRecord(BaseModel):
    '''
    The model for a recorded manual correction results.
    '''
    pass


class AICorrectionRecord(BaseModel):
    '''
    The model for a recorded AI correction results.
    '''
    pass


class Feedback(BaseModel):
    '''
    Content and emotion produced in reaction to something. The materialization of something felt or thought in response to a situation or event. It can be affirmative, constructive, etc.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    emoji: str = Field(None, description="A representation of the emotional state associated with the feedback message.")
    description: List[Expression] = Field(..., description="A set of expressions combined to form a rich feedback message.")


class Challenge(BaseModel):
    '''
    Basically a set of exercises combined for the purpose of testing skills.
    '''
    id: id = Field(..., description="no description")
    object: None = Field(None, description="no description")
    type: ChallengeTypes = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    title: str = Field(..., description="A short text describing the challenge.")
    tagline: str = Field(..., description="A short add-on text, adding more details to the title.")
    description: List[ChallengeDescriptionSection] = Field(None, description="A in-depth text describing the challenge.")
    tags: List[str] = Field(None, description="A set of keywords related to the challenge.")
    promoimage: str = Field(..., description="A visual description of the challenge.")
    promovideo: str = Field(None, description="In-depth stimulating descrpitionof the challenge.")
    duration: int = Field(None, description="Total time, measured in seconds")
    difficulty: difficulty = Field(None, description="The difficulty level of the challenge.")
    langauges: List[Language] = Field(None, description="The supported languages for this challenge.")
    exercises: List[Exercise] = Field(None, description="The exercises making up the challenge.")
    organizers: List[Organization] = Field(..., description="The organization(s) hosting the challenge")


class ChallengeDescriptionSection(BaseModel):
    '''
    no description
    '''
    headline: str = Field(None, description="The headline of the section.")
    bodycopy: str = Field(None, description="Approximately a paragraph of text describing the section.")
    label: str = Field(None, description="A piece of text describing the section.")
    featuredexpression: Expression = Field(None, description="no description")


class OnlineProjectChallenge(BaseModel):
    '''
    Online project challenge.
    '''
    pass


class LiveQuizChallenge(BaseModel):
    '''
    Live quiz challenge
    '''
    pass


class Course(BaseModel):
    '''
    a collection of expressions and exercises combined for the purpose of teaching something.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    type: CourseTypes = Field(..., description="no description")
    title: str = Field(..., description="The title of the course")
    tagline: str = Field(..., description="no description")
    description: List[Expression] = Field(..., description="A rich description of the course using an array of expressions")
    promovideo: str = Field(None, description="A promo video to introduce the course.")
    promoimage: str = Field(None, description="A promo image to make people interested in the course.")


class BookCourse(BaseModel):
    '''
    Uhm... a book. That's what this represents.
    '''
    pass


class Chapter(BaseModel):
    '''
    no description
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    title: str = Field(..., description="The title of the chapter")
    parent: str = Field(..., description="The id of the parent chapeter.")
    treeindex: str = Field(..., description="The placement in the chapter hieararchy.")
    contentadapters: List[ContentAdapter] = Field(..., description="The content found inside the chapter.")


class ProjectCourse(BaseModel):
    '''
    A project is a practically-oriented course.
    '''
    pass


class Iteration(BaseModel):
    '''
    A single step, a working version, of the project.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    title: str = Field(..., description="The title of the iteration.")
    description: str = Field(..., description="A description of the iteration.")
    promovideo: str = Field(..., description="A video showing how the product should look after the iteration.")
    exercise: None = Field(..., description="no description")


class ContentAdapter(BaseModel):
    '''
    no description
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    expression: None = Field(..., description="The main part of the content adapter; an expression.")
    exercises: List[Exercise] = Field(..., description="The exercises connected to the expression, through the content adapter.")      

        
        