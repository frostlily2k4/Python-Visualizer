import io
import contextlib


def run_python_code(code: str):
    """
    Executes Python code safely and captures the output.
    Returns:
        success (bool)
        output (str)
    """

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})

        return True, output.getvalue()

    except Exception as e:
        return False, str(e)