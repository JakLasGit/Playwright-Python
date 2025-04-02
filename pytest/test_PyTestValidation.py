#Fixtures
import pytest

# (scope="function") - fixture uruchomi sie przed każdym testem, który ma w argumentach nazwe fixtura
# (score="module") - fixture uruchomi sie raz na plik
# (score="session") - fixture uruchomi sie raz na jedną egzekucję
# "pytest" - w terminalu odpala wszystkie testy w plikach co zaczynają sie na test_
# pytest *nazwa pliku* odpala testy w danym pliku
# pytest *nazwa pliku*::*nazwa testu* odpala dany test w danym pliku            - s  odpala z logami
# użycie yield pozwala wykonać najpierw setup fixture, potem test, a po teście reszte ktora jest za yield
# @pytest.mark.skip - po tym wszystkie testy będą skipnięte
# @pytest.mark.smoke ---  pytest -m smoke - odpala tylko testy z markiem smoke

@pytest.fixture(scope="module")
def preWork():
    print("I setup browser instance")
    return "pass"

@pytest.fixture(scope="function")
def secondPreWork():
    print("I setup secondPreWork instance")
    yield #pause
    print("tear down validation")

def test_initialCheck(preWork, secondPreWork):
    print("This is first test!")
    assert preWork == "pass"

def test_secondCheck(preWork, secondPreWork):
    print("This is second test!")