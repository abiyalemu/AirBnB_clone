0x00. AirBnB Clone - The Console

The console is one segement project of the AirBnB project at alx school that cover  collectively cover fundamental concepts of higher level programming.The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

Function of this command interpreter
 Create a new object (ex: a new User or a new Place)
 Retrieve an object from a file, a database etc...
 Update attributes of an object
 Destroy an object
 Do operations on objects (count, compute stats, etc...)

Domain

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).

Installing

Clone this repository: git clone "https://github.com/abiyalemu/AirBnB_clone.git"
Entering AirBnb directory: cd AirBnB_clone

Run hbnb(interactively): ./console and enter command

Run hbnb(non-interactively): echo "<command>" | ./console.py


File Descriptions

console.py - the console contains the entry point of the command interpreter. List of commands this console current supports:

EOF - exits console
quit - exits console
<emptyline> - overwrites default emptyline method and does nothing
create - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
show - Prints the string representation of an instance based on the class name and id.
all - Prints all string representation of all instances based or not on the class name.
update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

models/ directory contains a class for this project

base_model.py - The BaseModel class from which future classes will be derived
def __init__(self, *args,**kwargs) - base model intialization
def __str__(self) - Basemodel class string represenation
def save(self) - updates the attribute update_at with current date time
def to_dict(self) - returns a dictionary containing all keys/values of the instance

class inherited from base model:
amenity .py
city.py
place.py
review.py
state.py
user.py
/models/engine directory contains file storage class

fil_storage.py - serialization instances and deserializes back to instances
def all(self) _returns the dictionary__objects
def new(self, obj) - sets in__ objects the obj with key .id
def save(self) _serializes __objects
def reload(self) -deserializes
/tests directory cantains all unit test case for this project:
/test_models/test_base_model.py - Contains the TestBaseModel and TestBaseModelDocs classes TestBaseModelDocs class:
def setUpClass(cls)- Set up for the doc tests
def test_pep8_conformance_base_model(self) - Test that models/base_model.py conforms to PEP8
def test_bm_module_docstring(self) - Test for the base_model.py module docstring
def test_bm_class_docstring(self) - Test for the BaseModel class docstring
def test_bm_func_docstrings(self) - Test for the presence of docstrings in BaseModel methods
TestBaseModel class:
def test_is_base_model(self) - Test that the instatiation of a BaseModel works
def test_created_at_instantiation(self) - Test created_at is a pub. instance attribute of type datetime
def test_updated_at_instantiation(self) - Test updated_at is a pub. instance attribute of type datetime
def test_diff_datetime_objs(self) - Test that two BaseModel instances have different datetime objects
/test_models/test_amenity.py - Contains the TestAmenityDocs class:
def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_amenity(self) - Test that models/amenity.py conforms to PEP8
def test_pep8_conformance_test_amenity(self) - Test that tests/test_models/test_amenity.py conforms to PEP8
def test_amenity_module_docstring(self) - Test for the amenity.py module docstring
def test_amenity_class_docstring(self) - Test for the Amenity class docstring
/test_models/test_city.py - Contains the TestCityDocs class:
def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_city(self) - Test that models/city.py conforms to PEP8
def test_pep8_conformance_test_city(self) - Test that tests/test_models/test_city.py conforms to PEP8
def test_city_module_docstring(self) - Test for the city.py module docstring
def test_city_class_docstring(self) - Test for the City class docstring
/test_models/test_file_storage.py - Contains the TestFileStorageDocs class:
def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_file_storage(self) - Test that models/file_storage.py conforms to PEP8
def test_pep8_conformance_test_file_storage(self) - Test that tests/test_models/test_file_storage.py conforms to PEP8
def test_file_storage_module_docstring(self) - Test for the file_storage.py module docstring
def test_file_storage_class_docstring(self) - Test for the FileStorage class docstring
/test_models/test_place.py - Contains the TestPlaceDoc class
def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_place(self) - Test that models/place.py conforms to PEP8.
def test_pep8_conformance_test_place(self) - Test that tests/test_models/test_place.py conforms to PEP8.
def test_place_module_docstring(self) - Test for the place.py module docstring
def test_place_class_docstring(self) - Test for the Place class docstring
/test_models/test_review.py - Contains the TestReviewDocs class:
def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_review(self) - Test that models/review.py conforms to PEP8
def test_pep8_conformance_test_review(self) - Test that tests/test_models/test_review.py conforms to PEP8
def test_review_module_docstring(self) - Test for the review.py module docstring
def test_review_class_docstring(self) - Test for the Review class docstring
/test_models/state.py - Contains the TestStateDocs class:
def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_state(self) - Test that models/state.py conforms to PEP8
def test_pep8_conformance_test_state(self) - Test that tests/test_models/test_state.py conforms to PEP8
def test_state_module_docstring(self) - Test for the state.py module docstring
def test_state_class_docstring(self) - Test for the State class docstring
/test_models/user.py - Contains the TestUserDocs class:

def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_user(self) - Test that models/user.py conforms to PEP8
def test_pep8_conformance_test_user(self) - Test that tests/test_models/test_user.py conforms to PEP8
def test_user_module_docstring(self) - Test for the user.py module docstring
def test_user_class_docstring(self) - Test for the User class docstring
example
root@12b56d6a042c:~/AirBnB_clone# ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
