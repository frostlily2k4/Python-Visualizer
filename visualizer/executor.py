import io
import contextlib


def run_python_code(code: str):
    """
    Executes Python code and returns:
    success -> bool
    output -> str
    variables -> dict
    """

    output = io.StringIO()

    variables = {}

    try:

        with contextlib.redirect_stdout(output):
            exec(code, {}, variables)

        return True, output.getvalue(), variables

    except Exception as e:

        return False, str(e), {}