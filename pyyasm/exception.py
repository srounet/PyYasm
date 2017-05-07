"""pyyasm Exceptions"""


class PyYasmError(Exception):
    """Global pyyasm Exception"""
    pass


class PyYasmArchitectureError(PyYasmError):
    """Exception in case the client architecture is not supported"""
    pass


class PyYasmVersionError(PyYasmError):
    """Exception in case we could not find version"""
    pass


class PyYasmTypeError(PyYasmError):
    """Exception in case mnemonics type is wrong"""
    pass