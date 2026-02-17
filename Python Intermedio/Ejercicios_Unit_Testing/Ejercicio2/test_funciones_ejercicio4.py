from Ejercicios_Funciones import reverse_string

def test_reverse_string_big_string():
    big_string = (
    "PythonIsPowerfulAndElegant1234567890"
    "DataStructuresAndAlgorithmsAreFun0987654321"
    "TestingImprovesCodeQualityAndConfidence1122334455"
    "CleanCodeMattersForProfessionalDevelopers5566778899"
    "PracticeMakesProgressAndConsistencyBuildsMastery000111222333"
    )

    assert reverse_string(big_string) == big_string[::-1]


def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


def test_reverse_string_single_character():
    assert reverse_string("a") == "a"
