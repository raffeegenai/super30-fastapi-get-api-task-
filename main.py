from fastapi import FastAPI,Query
from pydantic import BaseModel,Field, EmailStr, HttpUrl

app = FastAPI(title="Super30 FastAPI GET API")


@app.get("/")
def welcome():
    return {"message": "Welcome to the Super30 FastAPI "}

@app.get("/student")
def student_details(name: str, batch: str, role: str):
    """Return the requested student details as a JSON-serializable mapping."""
    return {
        "name": name,
        "batch": batch,
        "role": role,
    }

@app.get("/course")
def course_details(
    course_name: str,
    Mentor: str,
    course_duration: str,
    topic: list[str] = Query(...)
):
    """Return the requested course details as a JSON-serializable mapping."""
    return {
        "course_name": course_name,
        "Mentor": Mentor,
        "course_duration": course_duration,
        "topics": topic
    }

@app.get("/skills")
def get_skills(skill: list[str] = Query(...)):
    """Return the requested skills as a JSON-serializable mapping."""
    return {
        "skills": skill
    }


class addition(BaseModel):
    num1: int = Field(get=0, le=100, description="First number to add")
    num2: int = Field(get=0, le=100, description="Second number to add")
    result: int = Field(get=0, le=200, description="Result of addition")


@app.get("/add/{num1}/{num2}", response_model=addition)
def add_numbers(num1: int, num2: int):
    """Return the sum of two numbers."""
    return addition(num1=num1, num2=num2, result=num1 + num2)

class result_new(BaseModel):
    result: int = Field(get=0, le=20000, description="Result of arthmetic operation")   

class add_numbers_query(BaseModel):
    num1: int = Field(get=0, le=100, description="First number to add")
    num2: int = Field(get=0, le=100, description="Second number to add")

@app.get("/add_new/{num1}/{num2}", response_model=result_new)
def add_numbers_new(num1: int, num2: int):
    """Return the sum of two numbers."""
    return result_new(result=num1 + num2) 

from fastapi import  Depends

@app.get("/add_new1", response_model=result_new)
def add_numbers_new1( numbers: add_numbers_query = Depends()):
    """Return the sum of two numbers."""
    return result_new(result=numbers.num1 + numbers.num2)

class multiply(BaseModel):
    num1: int = Field(get=0, le=100, description="First number to multiply")
    num2: int = Field(get=0, le=100, description="Second number to multiply")
   

@app.get("/multiply/{num1}/{num2}")
def multiply_numbers(numbers : multiply = Depends()):
    """Return the product of two numbers."""
    return result_new(result=numbers.num1 * numbers.num2)

class SquareInput(BaseModel):
    num1: int = Field(
        ge=0,
        le=100,
        description="Number to square"
    )


class SquareResponse(BaseModel):
    number: int
    square: int


@app.get("/square/{num1}", response_model=SquareResponse)
def square_number( data: SquareInput = Depends() ):
    return SquareResponse(number=data.num1, square=data.num1 ** 2)

class EvenoddInput(BaseModel):
    num1: int = Field(
        ge=0,
        le=100,
        description="Number to find even or odd"
    )


class EvenoddResponse(BaseModel):   
    number: int
    type: str

@app.get("/check/{num1}", response_model=EvenoddResponse)
def even_odd_number(data: EvenoddInput = Depends()):
    if data.num1 % 2 == 0:
        return EvenoddResponse(number=data.num1, type="Even")
    else:
        return EvenoddResponse(number=data.num1, type="Odd")

class AgeInput(BaseModel):
    num1: int = Field(
        ge=0,
        le=100,
        description="Number to find adult or child or senior citizen"
    )


class AgeResponse(BaseModel):
    age: int
    message: str

@app.get("/age/{num1}", response_model=AgeResponse)
def check_age(data: AgeInput = Depends()):
    if data.num1 < 18:
        return AgeResponse(age=data.num1, message="Child")
    elif data.num1 < 60:
        return AgeResponse(age=data.num1, message="Adult")
    else:
        return AgeResponse(age=data.num1, message="Senior Citizen")

class TableInput(BaseModel):
    num1: int = Field(
        ge=0,
        le=100,
        description="Number to find multiplication table"
    )

class TableResponse(BaseModel):
    number: int
    table: list[str]

@app.get("/table/{num1}", response_model=TableResponse)
def multiplication_table(data: TableInput = Depends()) -> TableResponse:
    table = [f"{data.num1} x {i} = {data.num1 * i}" for i in range(1, 11)]
    return TableResponse(number=data.num1, table=table)

class ProfileInput(BaseModel):
    name: str = Field( min_length=1,  max_length=50,description="Person name" )    
    age: int = Field(ge=1, le=100,description="Person age")

class ProfileResponse(BaseModel):
    name: str
    age: int

@app.get("/profile/{name}/{age}", response_model=ProfileResponse)
def profile_details (data: ProfileInput = Depends()) -> ProfileResponse:
    return ProfileResponse(name=data.name, age=data.age)

class NumberInput(BaseModel):
    number: int = Field(
        ge=0,
        le=1000,
        description="Number to analyze"
    )

class NumberResponse(BaseModel):
    number: int
    square: int
    cube: int
    even: bool

@app.get("/number/{number}", response_model=NumberResponse)
def number_analysis(data: NumberInput = Depends()) -> NumberResponse:
    return NumberResponse(
        number=data.number,
        square=data.number ** 2,
        cube=data.number ** 3,
        even=data.number % 2 == 0
    )