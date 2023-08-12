import sender_stand_request
import data

def get_kit_body(kit_body):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_body
    return current_kit_body


def positive_assert(kit_body):
    new_kit_body = get_kit_body(kit_body)
    kit_body_response = sender_stand_request.post_new_client_kit(new_kit_body)
    assert kit_body_response.status_code == 201
    assert kit_body_response.json()["name"] == kit_body


def negative_assert(kit_body):
    new_kit_body = get_kit_body(kit_body)
    kit_body_response = sender_stand_request.post_new_client_kit(new_kit_body)
    assert kit_body_response.status_code == 400


def negative_assert_no_kit_name(kit_body):
    new_kit_body = sender_stand_request.post_new_client_kit(kit_body)
    assert new_kit_body.status_code == 400


def test_positive_create_1_character_name_kit():
    positive_assert("a")


def test_positive_create_511_character_name_kit():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_negative_create_empty_name_kit():
    negative_assert("")


def test_negative_create_512_character_name_kit():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_positive_create_eng_characters_name_kit():
    positive_assert("QWErty")


def test_positive_create_rus_characters_name_kit():
    positive_assert("Мария")


def test_positive_create_special_characters_name_kit():
    positive_assert("№%@\",")


def test_positive_create_name_with_spaces_kit():
    positive_assert("Человек и КО ")


def test_positive_create_numbers_in_str_name_kit():
    positive_assert("123")


def test_negative_create_no_name_parameter_kit():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_kit_name(kit_body)


def test_negative_create_numbers_in_int_characters_name_kit():
    negative_assert(12)
