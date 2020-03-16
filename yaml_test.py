#!/usr/bin/env python3

"""
#TODO: Come up with proper statement etc. here. 
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

class format(str,Enum):
    """
    The mathematical notation format.
    """
    katex = 'katex'
    tex = 'tex'

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

class commandLanguage(str,Enum):
    """
    The interpreter used for the command line (full list: https://en.wikipedia.org/wiki/List_of_command-line_interpreters)
    """
    bash = 'Bash'
    powershell = 'PowerShell'

class archiveFormat(str,Enum):
    """
    The type of archive. Currently only supporting zip files.
    """
    zip = 'zip'

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

class expectedOutputFormat(str,Enum):
    """
    The formatting of the expected output.
    """
    regex = 'regex'
    string_literal = 'string literal'

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
    beginner = 'beginner'
    intermediate = 'intermediate'
    advanced = 'advanced'

class ChallengeTypes(str,Enum):
    """
    The type of challenge.
    """
    onlineproject = 'online_project'
    livequiz = 'live_quiz'

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
    A three-letter ISO code ([ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3)), representing the language.
    '''
    pass


class url(BaseModel):
    '''
    A universal resource identifier (URI), according to the [RFC3986](https://tools.ietf.org/html/rfc3986) standard.
    '''
    pass


class fileUpload(BaseModel):
    '''
    no description
    '''
    pass


class public(BaseModel):
    '''
    If true, this object will be available for all active users.
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
    id: id = Field(..., description="no description")
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
    organizationnumber: str = Field(None, description="The number issued by the government, proving that the organization exists.")
    visionstatement: str = Field(None, description="A short, descriptive text of what future the organization aims to bring about.")
    type: OrganizationType = Field(..., description="no description")
    organizationbranding: OrganizationBranding = Field(None, description="no description")
    icon: fileUpload = Field(None, description="File upload. An icon for the organization. Must be square and at least 128px x 128px.")
    logo: fileUpload = Field(None, description="File Upload. A logo for the organization that will be used in on pages. Must be at least 128px x 128px.")


class OrganizationBranding(BaseModel):
    '''
    The branding associated with the organization.
    '''
    icon: File = Field(None, description="An icon for the organization. Must be square and at least 128px x 128px.")
    logo: File = Field(None, description="A logo for the organization that will be used in on pages. Must be at least 128px x 128px.")
    primarycolor: str = Field(None, description="A CSS hex color value representing the primary branding color for this organization.")


class Expression(BaseModel):
    '''
    An expression is a captured moment of menaingful communication - in a speficic medium and/or form.
    '''
    id: id = Field(None, description="no description")
    created: timestamp = Field(None, description="no description")
    creator: userId = Field(None, description="no description")
    type: ExpressionTypes = Field(..., description="no description")


class BlobExpressions(BaseModel):
    '''
    Common properties for Expressions holding binary large objects.
    '''
    src: File = Field(None, description="no description")
    file: fileUpload = Field(None, description="no description")


class TextExpression(Expression):
    '''
    Expressions captured in rich text.
    '''
    content: str = Field(..., description="The content in ready-to-go cleartext format.")
    language: language = Field(..., description="no description")
    format: format = Field(..., description="The text format.")
    type: ExpressionTypes = Field(None, description="no description")


class MathExpression(Expression):
    '''
    Expressions captured in mathematical notation.
    '''
    content: str = Field(..., description="The mathematics content.")
    format: format = Field(..., description="The mathematical notation format.")
    type: ExpressionTypes = Field(None, description="no description")


class CodeExpression(Expression):
    '''
    Expressions captured in various coding languages.
    '''
    content: str = Field(..., description="The code content.")
    programminglanguage: ProgrammingLanguage = Field(..., description="no description")
    type: ExpressionTypes = Field(None, description="no description")


class ImageExpression(BlobExpressions):
    '''
    Expressions captured in image form.
    '''
    type: ExpressionTypes = Field(None, description="no description")


class AudioExpression(BlobExpressions):
    '''
    Expressions captured in the form of sound.
    '''
    type: ExpressionTypes = Field(None, description="no description")


class AnimationExpression(BlobExpressions):
    '''
    Expressions captured in image sequence form; without sound.
    '''
    type: ExpressionTypes = Field(None, description="no description")


class VideoExpression(BlobExpressions):
    '''
    Expressions captured in video form.
    '''
    type: ExpressionTypes = Field(None, description="no description")


class Exercise(BaseModel):
    '''
    An exercise introduces you to, and invites you to complete, a specific activity.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    creator: userId = Field(None, description="no description")
    promoimage: fileUpload = Field(None, description="File upload. An image used to promote the exercise.")
    displayinfo: object = Field(None, description="Information related to how the exercise will be displayed.")
    description: List[None] = Field(..., description="A set of expressions combined to form a rich description of the activity requested.")
    type: ExerciseTypes = Field(..., description="no description")


class FreeFormExercise(Exercise):
    '''
    An exercise expecting a free-form text answer.
    '''
    type: ExerciseTypes = Field(None, description="no description")


class MultipleChoiceExercise(Exercise):
    '''
    An exercise providing multiple choices, of which one or more is correct.
    '''
    options: List[object] = Field(..., description="An array of different multiple choice options")
    type: ExerciseTypes = Field(None, description="no description")


class FillInTheBlankExercise(Exercise):
    '''
    An exercise providing text with blnak fields to fill in.
    '''
    blankfieldtext: str = Field(..., description="A text string containing blank fields.")
    type: ExerciseTypes = Field(None, description="no description")


class CommandLineExercise(Exercise):
    '''
    An exercise where your write a command in the command line.
    '''
    commandlanguage: commandLanguage = Field(..., description="The interpreter used for the command line (full list: https://en.wikipedia.org/wiki/List_of_command-line_interpreters)")
    type: ExerciseTypes = Field(None, description="no description")


class CodeSnippetExercise(Exercise):
    '''
    An exercise expecting a single file of code (a snippet, aka. gist) as the answer.
    '''
    startercode: str = Field(..., description="The initial code to be shown upon starting the exercise.")
    type: ExerciseTypes = Field(..., description="no description")


class CodebaseExercise(Exercise):
    '''
    An exercise expecting an entire codebase (multiple files and folders) as the answer.
    '''
    type: ExerciseTypes = Field(None, description="no description")
    startercode: str = Field(..., description="The initial code to be shown upon starting the exercise.")


class DatabaseExercise(Exercise):
    '''
    An exercise where you perform various database operations such as a query.
    '''
    type: ExerciseTypes = Field(None, description="no description")


class CodeReviewExercise(Exercise):
    '''
    An exercise where you review some code, leave comments, etc.
    '''
    type: ExerciseTypes = Field(None, description="no description")


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


class AnswerTypes(ExerciseTypes):
    '''
    The shape of an answer is based on the type of exercise (and, potentially at some point, a choice of expression selected by the user).
    '''
    pass


class FreeFormAnswer(Answer):
    '''
    ... constituting an answer to a `Free Form Exercise`.
    '''
    pass


class MultipleChoiceAnswer(Answer):
    '''
    ... constituting an answer to a `Multiple Choice Exercise`.
    '''
    pass


class FillInTheBlankAnswer(Answer):
    '''
    ... constituting an answer to a `Fill In The Blank Exercise`.
    '''
    pass


class CommandLineAnswer(Answer):
    '''
    ... constituting an answer to a `Command Line Exercise`.
    '''
    pass


class CodeSnippetAnswer(Answer):
    '''
    ... constituting an answer to a `Code Snippet Exercise`.
    '''
    pass


class CodebaseAnswer(Answer):
    '''
    Files and folders (filesystem) constituting an answer to a `Codebase Exercise`.
    '''
    archive: str = Field(..., description="The answer in the form of an archived file system.")
    archiveformat: archiveFormat = Field(..., description="The type of archive. Currently only supporting zip files.")


class DatabaseAnswer(Answer):
    '''
    ... constituting an answer to a `Database Exercise`.
    '''
    pass


class CodeReviewAnswer(Answer):
    '''
    ... constituting an answer to a `Code Review Exercise`.
    '''
    pass


class CorrectionBlueprint(BaseModel):
    '''
    The blueprint for how to correct an answer to an exercise.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    creator: userId = Field(None, description="no description")
    type: ExerciseTypes = Field(..., description="no description")
    allowautomaticcorrection: bool = Field(None, description="Whether to allow automatic correction or not.")
    allowmanualcorrection: bool = Field(None, description="Whether to allow manual correction or not.")
    allowaicorrection: bool = Field(None, description="Whether to allow artificial intelligence correction or not.")
    requirements: List[Requirement] = Field(..., description="A list of requirements to be corrected for")


class Requirement(BaseModel):
    '''
    A specific element you expect to be part of a correct solution. A 
requirement is like an interface - it defines what should be tested, 
but it is not the implementation of the test itself. This allows us to 
apply different approaches to testing the same set of things (e.g. 
manual correction, automatic correction, ai correction, etc.), and to 
compare these approaches and implementations with each other.
    '''
    id: id = Field(..., description="no description")
    title: str = Field(..., description="A indicative text for the requirement.")
    description: str = Field(None, description="A text with more detailed information about the requirement.")
    weight: int = Field(None, description="A number signifying the importance of the")
    automatictests: List[TestCase] = Field(None, description="The automatic test cases to run to correct for the requirement.")
    failureresponses: List[Feedback] = Field(..., description="A set of potential feedback objects to display to students upon failing requirement.")


class AutomaticCorrectionImplementation(BaseModel):
    '''
    The automatic correction implementation contains a bundle of test cases that provide a possible implementation to the correction blueprint proposed by the correction blueprint creator.
    '''
    id: id = Field(None, description="no description")
    created: timestamp = Field(None, description="no description")
    creator: userId = Field(None, description="no description")
    model: str = Field(None, description="The key is an requirement id from the correction blueprint, and the value is a set of test cases.")


class TestCase(BaseModel):
    '''
    The tests used to automaticaly correct the requirements. The test 
case is like the implementation of the interface defined in a 
requirement. More specifically, a test case provides an implementation 
in the realm of automatic correction. Since test cases are very specific 
they don't need much contextual information in order to be executed.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(None, description="no description")
    creator: userId = Field(None, description="no description")
    type: TestCaseTypes = Field(..., description="no description")
    visibility: visibility = Field(..., description="Whether or not to show the test case.")
    explaincommonerrors: bool = Field(..., description="Whether or not to explain universal and common errors.")
    studentdebugginginfo: DebuggingInfo = Field(..., description="no description")
    successthreshold: int = Field(..., description="The percentage required to consider the test case passed.")


class IOTestCase(TestCase):
    '''
    A test case definition for performing I/O testing. These are langauge agnostic.
    '''
    mainfilepath: str = Field(..., description="The path to the main file, where the program exercution starts.")
    input: str = Field(..., description="the input provided through standard input.")
    expectedoutput: str = Field(..., description="the output provided through standard output. Can also be in regex format.")
    expectedoutputformat: expectedOutputFormat = Field(..., description="The formatting of the expected output.")
    strictwhitespace: str = Field(..., description="Whether to use strict whitespace or not.")
    files: str = Field(..., description="Additional files added to the solution for testing purposes (as a zip file)")
    commandlinearguments: List[str] = Field(..., description="Any additional arguments for the run command.")
    maxruntime: int = Field(..., description="The max allowed execution time in milliseconds.")
    type: TestCaseTypes = Field(None, description="no description")


class UnitTestCase(TestCase):
    '''
    A test case definition for performing unit testing. All the code should be imported to allow for running the unit test on any piece of the codebase.
    '''
    programminglanguage: ProgrammingLanguage = Field(..., description="no description")
    testcasecode: str = Field(..., description="The code holding the unit test case.")
    type: TestCaseTypes = Field(None, description="no description")


class CustomTestCase(TestCase):
    '''
    A test case definition for performing custom testing
    '''
    testcasebashscript: str = Field(..., description="A bash script running anything you want, printing out the result at the last line of the output.")
    type: TestCaseTypes = Field(None, description="no description")


class LintingTestCase(TestCase):
    '''
    More general test case definition for code quality
    '''
    lintersettings: str = Field(..., description="A file holding the linter information used to check code formatting.")
    type: TestCaseTypes = Field(None, description="no description")


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
    created: timestamp = Field(None, description="no description")
    type: CorrectionRecordType = Field(..., description="no description")


class AutmaticCorrectionRecord(CorrectionRecord):
    '''
    The model for recorded automatic correction results.
    '''
    type: CorrectionRecordType = Field(None, description="no description")
    testcaseinput: str = Field(..., description="The input of the test case.")
    compilerstacktrace: str = Field(..., description="Whether to show the compiler/debug output to the student or not.")
    exercutionstacktrace: str = Field(..., description="Whether to show the exercution output to the student or not.")
    studentsolutionoutput: str = Field(..., description="Whether to show the output of the student's code to the student or not.")
    expectedsolutionoutput: str = Field(..., description="Whether to show the expected output to the student or not.")
    outputdifference: str = Field(..., description="Whether to show the difference between the supplied and expected output to the student or not.")


class ManualCorrectionRecord(CorrectionRecord):
    '''
    The model for a recorded manual correction results.
    '''
    something: str = Field(..., description="some value required")
    type: CorrectionRecordType = Field(None, description="no description")


class AICorrectionRecord(CorrectionRecord):
    '''
    The model for a recorded AI correction results.
    '''
    something: str = Field(..., description="some value required")
    type: CorrectionRecordType = Field(None, description="no description")


class ClientCorrectionBundle(BaseModel):
    '''
    An object containing mainly key-value pairs of answer hashes and feedback.
    '''
    id: id = Field(None, description="no description")
    model: object = Field(None, description="The object containing mainly key-value pairs of answer hashes and feedback.")


class Feedback(BaseModel):
    '''
    Content and emotion produced in reaction to something. The materialization of something felt or thought in response to a situation or event. It can be affirmative, constructive, etc.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    creator: userId = Field(None, description="no description")
    emoji: str = Field(None, description="A representation of the emotional state associated with the feedback message.")
    description: List[Expression] = Field(..., description="A set of expressions combined to form a rich feedback message.")


class Challenge(BaseModel):
    '''
    Basically a set of exercises combined for the purpose of testing skills.
    '''
    id: id = Field(..., description="no description")
    object: object = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    creator: userId = Field(None, description="no description")
    title: str = Field(None, description="A short text describing the challenge.")
    tagline: str = Field(None, description="A short add-on text, adding more details to the title.")
    description: List[object] = Field(None, description="A in-depth text describing the challenge.")
    tags: List[str] = Field(None, description="A set of keywords related to the challenge.")
    promoimage: str = Field(None, description="A visual description of the challenge.")
    promovideo: str = Field(None, description="In-depth stimulating descrpition of the challenge.")
    availabilityranges: List[object] = Field(None, description="The durations where people will be able to take the challenge.")
    difficulty: difficulty = Field(None, description="The difficulty level of the challenge.")
    langauges: List[language] = Field(None, description="The supported languages for this challenge.")
    exercises: List[Exercise] = Field(None, description="The exercises making up the challenge.")
    organizers: List[Organization] = Field(None, description="The organization(s) hosting the challenge")
    published: bool = Field(None, description="If the challenge is published, it'll be listed in the public challenge catalog. If not, only the ones with the right link will be able to access it. This meets the need for recruiters to prevent solicitation of pre-vetted candidates.")


class OnlineProjectChallenge(Challenge):
    '''
    Online project challenge.
    '''
    type: ChallengeTypes = Field(None, description="no description")


class LiveQuizChallenge(Challenge):
    '''
    Live quiz challenge
    '''
    type: ChallengeTypes = Field(None, description="no description")


class Course(BaseModel):
    '''
    a collection of expressions and exercises combined for the purpose of teaching something.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    creator: userId = Field(None, description="no description")
    type: CourseTypes = Field(..., description="no description")
    title: str = Field(..., description="The title of the course")
    tagline: str = Field(..., description="no description")
    description: List[Expression] = Field(..., description="A rich description of the course using an array of expressions")
    promovideo: str = Field(None, description="A promo video to introduce the course.")
    promoimage: str = Field(None, description="A promo image to make people interested in the course.")


class BookCourse(Course):
    '''
    Uhm... a book. That's what this represents.
    '''
    coverphoto: url = Field(None, description="no description")
    spinephoto: url = Field(None, description="no description")
    backphoto: url = Field(None, description="no description")
    chapters: List[Chapter] = Field(..., description="The chapters found in the book")
    type: CourseTypes = Field(..., description="no description")


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


class ProjectCourse(Course):
    '''
    A project is a practically-oriented course.
    '''
    iterations: List[Iteration] = Field(..., description="The steps involved in doing the project.")
    type: CourseTypes = Field(None, description="no description")


class Iteration(BaseModel):
    '''
    A single step, a working version, of the project.
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    title: str = Field(..., description="The title of the iteration.")
    description: str = Field(..., description="A description of the iteration.")
    promovideo: str = Field(..., description="A video showing how the product should look after the iteration.")
    exercise: Exercise = Field(..., description="no description")


class ContentAdapter(BaseModel):
    '''
    no description
    '''
    id: id = Field(..., description="no description")
    created: timestamp = Field(..., description="no description")
    expression: Expression = Field(..., description="The main part of the content adapter; an expression.")
    exercises: List[Exercise] = Field(..., description="The exercises connected to the expression, through the content adapter.")


class Report(BaseModel):
    '''
    a filtered set of data points required to present a report. for the purpose of teaching something.
    '''
    challengeid: id = Field(None, description="no description")
    userid: userId = Field(None, description="no description")
    totalscore: None = Field(None, description="The total score achieved by the user for the given challenge.")
    totaltime: None = Field(None, description="The total time in seconds spent by the user for the given challenge.")
    challengeinfo: Challenge = Field(None, description="no description")
    finalanswer: Answer = Field(None, description="A reference to the final answer provided by the user to the given challenge.")
    bestfinalanswer: Answer = Field(None, description="The best answer in terms of overall quality, structure and simplicity.")
    exerciseresults: List[object] = Field(None, description="no description")


class ChallengeReport(Report):
    '''
    a filtered set of data points required to present a challenge report.
    '''
    challengeid: id = Field(None, description="no description")


class RecruiterChallengeReport(ChallengeReport):
    '''
    a filtered set of data points, optimized to meet the needs of a recruiter, that forms the basis for displaying a report.
    '''
    recruitervalue: str = Field(None, description="no description")


class JobSeekerChallengeReport(ChallengeReport):
    '''
    a filtered set of data points, optimized to meet the needs of a job seeker, that forms the basis for displaying a report.
    '''
    jobseekervalue: str = Field(None, description="no description")


class OrganizationChallengeReport(ChallengeReport):
    '''
    a filtered set of data points, optimized to meet the needs of a job seeker, that forms the basis for displaying a report.
    '''
    jobseekervalue: str = Field(None, description="no description")      

        
        