import platform

import pytest

import pyyasm
import pyyasm.exception


def test_assemble():
    """Test working assembly"""
    mnemonics = b"""
        pushfd
        pushad
        popad
        popfd
    """
    expected_assembled = b'f\x9cf`faf\x9d'
    assembled = pyyasm.assemble(mnemonics)
    assert assembled == expected_assembled


def test_version():
    """Test version method"""
    version = pyyasm.version()
    # 1.3.0
    assert len(version.split('.')) == 3


def test_assemble_wrong_type():
    """Test invalid mnemonics type"""
    mnemonics = """
        pushfd
        pushad
        popad
        popfd
    """
    with pytest.raises(pyyasm.exception.PyYasmTypeError):
        assembled = pyyasm.assemble(mnemonics)


def test_architecture():
    """Monkey patch platform.architecture to make pyyasm raise exception
    and then restore the original method
    """
    # monkey patch platform.architecture
    def patched_platform_architecture():
        return ('64bit', 'ELF')
    orig_platform_architecture = platform.architecture
    platform.architecture = patched_platform_architecture

    mnemonics = b"""
        pushfd
        pushad
        popad
        popfd
    """
    with pytest.raises(pyyasm.exception.PyYasmArchitectureError):
        assembled = pyyasm.assemble(mnemonics)
    # restore platform.architecture
    platform.architecture = orig_platform_architecture
    