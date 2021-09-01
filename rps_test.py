"""Used to test rock_paper_scissors.py and it's functions"""
import pytest

from rock_paper_scissors import (
    checkBestToInput,
    getBestTo
)

def test_testing():
    assert(True == True)

def test_checBestInput():
    assert checkBestToInput("3") == True
    assert checkBestToInput("5") == True
    assert checkBestToInput("8") == True

def test_invalid_checkBestInput():
    assert checkBestToInput("0") == False
    assert checkBestToInput("globawobblelobble") == False
    assert checkBestToInput("Lord") == False
    assert checkBestToInput("33") == False
    assert checkBestToInput("555") == False
    assert checkBestToInput("888") == False



