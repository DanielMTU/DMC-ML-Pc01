import pytest
from processing import remove_links,remove_hastags,remove_numbers,remove_users, perform_lemmatization,perform_stemming

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ]
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize(
        "input_text, expected_output", 
    [
        ("Testing @user123 regex 456removal", "Testing  regex removal"),
        ("No changes needed", "No changes needed"),
        ("1234567890", ""),
        ("@user1 @user2 @user3", '  '),
    ]
)
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output


#Codigo PRACTICA N°1   
    
@pytest.mark.parametrize("text, expected", [
    ("Running quickly #awesome https://example.com", "run quick"),
    ("Better solutions found at http://solutions.com", "good solut find"),
    ("Children playing in parks are joyful", "child play in park are joy"),
    ("He was fishing by the lakeside yesterday", "he be fish by the lakesid yesterday"),
    ("The geese migrate south during winter", "the goose migrat south dure winter"),
])
def test_integration_lemmatization_stemming(text, expected):
    processed_text = perform_lemmatization(perform_stemming(text))    
    assert processed_text == expected