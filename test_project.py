from project import new_track, open_track, add_row, convert_track, choose_track

from unittest import mock


@mock.patch("project.input")
def test_new_track(mocked_input, capfd):
    mocked_input.side_effect = ["joan", "38.5", "ibuprofen", "150"]
    new_track()
    out, err = capfd.readouterr()

    assert "joan" in out
    assert "38.5" in out
    assert "ibuprofen" in out
    assert "150" in out


@mock.patch("project.input")
def test_add_row(mocked_input, capfd):
    f = "test.csv"
    mocked_input.side_effect = ["39", "", ""]
    add_row(f)
    out, err = capfd.readouterr()

    assert "joan" in out
    assert "38.5" in out
    assert "ibuprofen" in out
    assert "150" in out
    assert "39" in out

@mock.patch("project.input")
def test_open_track(mocked_input, capfd):
    f = "test.csv"
    mocked_input.side_effect = ["y"]
    open_track(f)
    out, err = capfd.readouterr()

    assert "joan" in out
    assert "38.5" in out
    assert "ibuprofen" in out
    assert "150" in out
    assert "39" in out


def test_convert_track(capfd):
    f = "test.csv"
    convert_track(f)
    out, err = capfd.readouterr()

    assert "You can find test.pdf in the pdf files folder" in out


@mock.patch("project.input")
def test_choose_track(mocked_input):
    csv_files = ["test.csv"]
    mocked_input.side_effect = ["1"]
    assert choose_track(csv_files) == 0