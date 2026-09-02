"""Smoke tests: the package and its modules import cleanly."""

import importlib

import pytest


@pytest.mark.parametrize(
    "module",
    [
        "capcup",
        "capcup.udp_receiver",
        "capcup.simulator.probe",
        "capcup.jubilee.offset_generator",
    ],
)
def test_import(module):
    importlib.import_module(module)
