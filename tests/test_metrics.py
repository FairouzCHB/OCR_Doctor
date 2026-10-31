import pytest

from ocr_doctor.evaluation.metrics import (
    cer,
    edit_distance,
    normalize,
    wer,
)


def test_normalize():
    assert normalize("  Hello   World\n") == "Hello World"


def test_edit_distance():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("cat", "cut") == 1


def test_cer():
    assert cer("cat", "cut") == pytest.approx(1 / 3)


def test_wer():
    assert wer("the cat sleeps", "the dog sleeps") == pytest.approx(1 / 3)


def test_empty_reference():
    assert cer("", "") == 0.0
    assert wer("", "") == 0.0
    assert cer("", "hello") == 1.0
    assert wer("", "hello") == 1.0
