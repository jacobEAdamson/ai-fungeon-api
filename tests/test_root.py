import pytest

@pytest.mark.vcr
def test_index(app, client):
    """
    GIVEN a running API
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid and includes key elements from the prompt
    """

    response = client.get('/')
    assert response.status_code == 200
    assert b"Chapel Hill" in response.data
    assert b"Jacob" in response.data
    assert len(response.data) >= 100
