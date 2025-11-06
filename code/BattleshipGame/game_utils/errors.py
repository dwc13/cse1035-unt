class Error(Exception):
	"""Base class for other exceptions"""
	pass

class PositionLengthError(Error):
	"""Raised when position length is not equal to 2"""
	pass

class PositionRowError(Error):
	"""Raised when position row type or value is invalid"""
	pass

class PositionColumnError(Error):
	"""Raised when position column type or value is invalid"""
	pass

class DuplicateShotError(Error):
	"""Raised when the same position is shot twice"""
	pass

class InputError(Exception):
    """Raised when user input is invalid."""
    pass