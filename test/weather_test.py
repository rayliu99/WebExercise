
import os
import pytest

from app.weather_service import get_hourly_forecasts, DEGREE_SIGN, format_hour

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_hourly_forecasts():
    # with valid geography, returns the city name and forecast info:
    results = get_hourly_forecasts(country_code="US", zip_code="20057")
    assert results["city_name"] == "Washington, DC"
    assert len(results["hourly_forecasts"]) == 24
    forecast = results["hourly_forecasts"][0]
    assert sorted(list(forecast.keys())) == ["conditions", "image_url", "temp", "timestamp"]
    assert forecast["timestamp"].endswith(":00")
    assert f"{DEGREE_SIGN}F" in forecast["temp"]

    # with invalid geography, fails gracefully and returns nothing:
    invalid_results = get_hourly_forecasts(country_code="US", zip_code="OOPS")
    assert invalid_results == None

def test_hour_formatting():
    assert format_hour("2021-03-29T21:00:00-04:00") == "21:00"
