import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

@pytest.mark.eval
def test_case():

    with open('ollama_output.txt', 'r+') as file:
        actual_output= file.read()

    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5,
    )

    test_case = LLMTestCase(
        input="Why is math so hard for so many students?",
        actual_output=actual_output,
        expected_output="Its not a straighforward answer and multiple layers to it",
    )

    assert_test(test_case, [correctness_metric])
    print("Test finished successfully!")