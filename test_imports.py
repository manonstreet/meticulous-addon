"""Test script to verify basic imports work."""
import sys
import os

# Add rootfs/usr/bin to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'rootfs', 'usr', 'bin'))

print("Testing imports...")

try:
    import mqtt_commands
    print("✓ mqtt_commands imported successfully")
    print(f"  Functions: {[f for f in dir(mqtt_commands) if not f.startswith('_')]}")
except ImportError as e:
    print(f"✗ mqtt_commands import failed: {e}")

print("\nTesting mqtt_commands functions...")
try:
    # Check that required functions exist
    assert hasattr(mqtt_commands, 'mqtt_on_message')
    assert hasattr(mqtt_commands, 'handle_command_start_brew')
    assert hasattr(mqtt_commands, 'handle_command_stop_brew')
    assert hasattr(mqtt_commands, 'handle_command_preheat')
    assert hasattr(mqtt_commands, 'handle_command_tare_scale')
    assert hasattr(mqtt_commands, 'handle_command_load_profile')
    assert hasattr(mqtt_commands, 'handle_command_set_brightness')
    assert hasattr(mqtt_commands, 'handle_command_enable_sounds')
    print("✓ All required command handler functions found")
except AssertionError as e:
    print(f"✗ Missing required functions: {e}")

print("\nAll basic import tests passed!")
