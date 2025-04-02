#Ten plik jest do wrzucania Fixturów i z niego będą brały wszystkie testy globalnie
import pytest


@pytest.fixture(scope="function")
def preWork():
    print("I setup browser instance")