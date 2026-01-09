# Changelog

All notable user-facing changes to this add-on are documented here.

## [0.3.0] - 2026-01-09

### ✨ Features
- Full MQTT discovery integration - sensors and controls automatically appear in Home Assistant
- Real-time machine status updates via Socket.IO
- Polling fallback for non-real-time data (profile, settings, statistics)
- Graceful handling of firmware/library version mismatches

### 🐛 Fixes
- Fixed MQTT broker connectivity issues by removing host network isolation
- Corrected DNS resolution for internal Home Assistant services
- Added MQTT service dependency for proper startup sequencing
- Resolved validation errors from pyMeticulous library mismatches
- Fixed Socket.IO callback threading issues for real-time updates

### 📋 What This Means for Users
You now have full control of your Meticulous Espresso machine from Home Assistant:
- **Sensors**: Temperature, pressure, flow rate, shot weight, timer, and more
- **Controls**: Start/stop brewing, adjust settings, select profiles
- **Automations**: Create routines based on machine state

## [0.2.x] - 2026-01-09

- Fixed startup and stability issues
- Improved security and compatibility
- Simplified configuration

## [0.1.0] - 2026-01-07

- Initial release with MQTT discovery and Meticulous Espresso integration


