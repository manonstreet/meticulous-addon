# Test Suite Structure for Meticulous Espresso Add-on

This directory contains all tests and developer scripts for the add-on, organized by function.

## Integration Tests (`integration/`)
- End-to-end tests that validate the add-on as a whole
- Tests include API connectivity, MQTT discovery, sensor population, and state management
- Files:
  - `test_addon_integration.py` — Core integration tests
  - `test_sensor_population.py` — Sensor state initialization and updates
  - `test_pymeticulous_030_updates.py` — pyMeticulous 0.3.0+ compatibility

## Unit Tests (`unit/`)
- Isolated tests for individual functions and handlers
- Tests MQTT command execution, error handling, and edge cases
- Files:
  - `test_mqtt_commands.py` — MQTT command handlers (start/stop brew, brightness, profile loading, etc.)

## Manual & Dev Scripts

### `dev_scripts/`
Developer scripts for manual testing (not run by automated test suite):
- `test_socketio_events.py` — Monitors Socket.IO events from the machine

### `manual/`
Manual endpoint testing scripts:
- `test_correct_endpoint.py` — Test machine API endpoint connectivity
- `test_profiles_endpoint.py` — Test profile loading endpoint

## Running Tests

### Run all tests
```sh
python tests/run_tests.py
```

### Run a specific test file
```sh
python -m unittest tests/integration/test_addon_integration.py
python -m unittest tests/integration/test_sensor_population.py
python -m unittest tests/unit/test_mqtt_commands.py
```

### Run tests from VS Code
Use the provided task: **Run sensor population integration tests** to execute the test suite.

## Adding New Tests

- **Integration tests** (system-level): Add to `integration/`
- **Unit tests** (individual functions): Add to `unit/`
- Use existing test files as templates for structure and patterns
