import pytest
from typing import Union
from genAI import generateList, Subject
import json
from pydantic import ValidationError

def test_genai():
        # Call the function to get the result
        test_res = json.loads(generateList("React").text)
        print(test_res)
        # assert isinstance(test_res, Subject), "res is not of Subject Type"
        # assert isinstance(test_res, Subject), "res is not Subject"
        Subject.model_validate(test_res)  
        assert check_subject(test_res), "res contains empty value"

# Subjetc object
# subject_name: name 
# topics: [ {topic_name : name, subtopics: [{subtopic_name: name, refs: [ref1,ref2]}]}, ]
@pytest.mark.skip
def recursively_check_value(val: Union[str, dict, list]) -> bool:
    # Check if value is None or empty string
    if val is None or (isinstance(val, str) and not val):
        return False
    # If it's a dictionary, check recursively all keys and values
    elif isinstance(val, dict):
        return all(recursively_check_value(v) for v in val.values())
    # If it's a list, check recursively all elements
    elif isinstance(val, list):
        if len(val) == 0:
            return False
        return all(recursively_check_value(item) for item in val)
    return True  # If it's a simple value (e.g., int, float), return True (not null)

@pytest.mark.skip          
def check_subject(subject: Subject) -> bool:
    if not recursively_check_value(subject["subject_name"]):
        return False
    for topic in subject["topics"]:
        if not recursively_check_value(topic["topic_name"]) or not recursively_check_value(topic["subtopics"]):
            return False
        for subtopic in topic["subtopics"]:
            if not recursively_check_value(subtopic["sub_topic_name"]) or not recursively_check_value(subtopic["refs"]):
                return False
    return True