#!/usr/bin/env python3
"""Unit tests for machine port configuration and base URL construction.

The firmware serves the REST API and Socket.IO through nginx on port 80. The
backend's own 8080 listener binds to localhost and is unreachable over the
network, so 80 is the default and 8080 is only an override for an emulated
backend run without nginx.
"""
import sys
from pathlib import Path
from unittest.mock import patch

# Add rootfs/usr/bin to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "rootfs" / "usr" / "bin"))

# Import after path is set
from run import DEFAULT_MACHINE_PORT, MeticulousAddon  # noqa: E402


def _addon(config):
    """Build an addon instance with a stubbed config."""
    with patch.object(MeticulousAddon, "_load_config", return_value=config):
        return MeticulousAddon()


class TestParseMachinePort:
    """Tests for _parse_machine_port()."""

    def test_default_is_80(self):
        assert DEFAULT_MACHINE_PORT == 80

    def test_absent_option_uses_default(self):
        assert _addon({"machine_ip": "1.2.3.4"}).machine_port == 80

    def test_explicit_override(self):
        addon = _addon({"machine_ip": "1.2.3.4", "machine_port": 8080})
        assert addon.machine_port == 8080

    def test_string_value_is_coerced(self):
        addon = _addon({"machine_ip": "1.2.3.4", "machine_port": " 8080 "})
        assert addon.machine_port == 8080

    def test_garbage_falls_back_to_default(self):
        for bad in ["", "abc", None, [], {}]:
            addon = _addon({"machine_ip": "1.2.3.4", "machine_port": bad})
            assert addon.machine_port == 80, f"{bad!r} should fall back"

    def test_out_of_range_falls_back_to_default(self):
        for bad in [0, -1, 65536, 999999]:
            addon = _addon({"machine_ip": "1.2.3.4", "machine_port": bad})
            assert addon.machine_port == 80, f"{bad} should fall back"


class TestBaseUrl:
    """Tests for the base_url property."""

    def test_default_port_omitted_from_url(self):
        addon = _addon({"machine_ip": "192.168.4.8"})
        assert addon.base_url == "http://192.168.4.8"

    def test_override_port_included(self):
        addon = _addon({"machine_ip": "192.168.4.8", "machine_port": 8080})
        assert addon.base_url == "http://192.168.4.8:8080"

    def test_no_trailing_slash(self):
        """Raw fallbacks append '/api/v1/...', so base must not end in '/'."""
        assert not _addon({"machine_ip": "1.2.3.4"}).base_url.endswith("/")

    def test_hostname_works(self):
        addon = _addon({"machine_ip": "meticulous.local"})
        assert addon.base_url == "http://meticulous.local"

    def test_builds_expected_endpoint(self):
        addon = _addon({"machine_ip": "192.168.4.8"})
        url = f"{addon.base_url}/api/v1/history/last"
        assert url == "http://192.168.4.8/api/v1/history/last"


class TestNoHardcodedPort:
    """Guard against reintroducing a hardcoded port."""

    def test_run_py_has_no_hardcoded_8080_urls(self):
        src = (
            Path(__file__).parent.parent.parent
            / "rootfs" / "usr" / "bin" / "run.py"
        ).read_text()
        offenders = [
            line.strip()
            for line in src.splitlines()
            if ":8080" in line and not line.strip().startswith("#")
        ]
        assert not offenders, f"hardcoded :8080 found: {offenders}"
