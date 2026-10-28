from backend.services.list_vehicles import list_vehicles


def test_list_vehicle_returns_list() -> None:
    result = list_vehicles()

    assert isinstance(result, list)
    assert len(result) > 0


def test_list_vehicle_contains_dictionaries() -> None:
    result = list_vehicles()

    assert all(isinstance(vehicle, dict) for vehicle in result)


def test_list_vehicle_contains_expected_fields() -> None:
    result = list_vehicles()

    expected_fields = {
        "id",
        "manufacturer",
        "model",
        "license_plate",
        "year",
        "mileage",
        "status",
    }

    assert expected_fields.issubset(result[0].keys())


def test_list_vehicle_have_correct_types() -> None:
    result = list_vehicles()
    vehicle = result[0]

    assert isinstance(vehicle["id"], int)
    assert isinstance(vehicle["manufacturer"], str)
    assert isinstance(vehicle["model"], str)
    assert isinstance(vehicle["model"], str)
    assert isinstance(vehicle["model"], str)
    assert isinstance(vehicle["year"], int)
    assert isinstance(vehicle["mileage"], int)
    assert isinstance(vehicle["status"], str)


def test_vehicle_status_is_valid() -> None:
    result = list_vehicles()
    valid_statuses = {"available", "maintenance"}

    assert all(vehicle["status"] in valid_statuses for vehicle in result)


def test_list_vehicle_ids_are_unique() -> None:
    result = list_vehicles()
    ids = [vehicle["id"] for vehicle in result]

    assert len(ids) == len(set(ids))
