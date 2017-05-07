"""Python wrapper for yasm x86/x64
"""

import os
import platform
import re
import subprocess
import tempfile

import pyyasm.exception


VERSION_PATTERN = r'yasm (?P<version>.*?)\s.*'
SUPPORTED_ARCHITECTURE = ['WindowsPE']

def _execute(*args):
    """Call yasm.exe with extra args.

        :param args: A tuple with extra args for yasm.exe
        :type name: tuple
    """
    bits, linkage = platform.architecture()
    if not linkage in SUPPORTED_ARCHITECTURE:
        raise pyyasm.exception.PyYasmArchitectureError(
            "{} is not a supported architecture".format(linkage)
        )
    path = os.path.dirname(os.path.abspath(__file__))
    yasm_filename = 'yasm_{}.exe'.format(bits)
    yasm_executable_filepath = os.path.join(path, 'ressources', yasm_filename)
    args = [yasm_executable_filepath] + list(args)
    ret = subprocess.check_output(args)
    ret = ret.decode('ascii')
    return ret


def version():
    """Returns yasm version"""
    ret = _execute("--version")
    groups = re.match(VERSION_PATTERN, ret, re.IGNORECASE)
    if not groups:
        raise pyyasm.exception.PyYasmVersionError("Could not find version")
    v = groups.groupdict()['version']
    return v


def assemble(mnemonics):
    """Assemble mnemonics with yasm and returns the assembled bytes.

        :param mnemonics: mnemonics to be assembled with yasm
        :type mnemonics: bytes
        :return: the assembled mnemonics
        :rtype: bytes
    """
    if not isinstance(mnemonics, bytes):
        raise pyyasm.exception.PyYasmTypeError("mnemonics as to be a byte string")
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(mnemonics)
    f.close()
    out_filepath = '{}.pyyasm'.format(f.name)
    _execute("-fbin", "-o{}".format(out_filepath), f.name)
    with open(out_filepath, 'rb') as out_f:
        content = out_f.read()
    os.unlink(f.name)
    os.unlink(out_filepath)
    return content