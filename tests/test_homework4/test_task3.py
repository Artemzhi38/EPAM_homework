from homeworks.homework4.task3 import my_precious_logger


# Positive tests
def test_stderr_case(capsys):
    """Testing that function given a string that starts
     with "error" writes this string to stderr"""
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"
    assert captured.out == ""


def test_stdout_case(capsys):
    """Testing that function given a string that does not
    start with "error" writes this string to stdout"""
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"
    assert captured.err == ""
