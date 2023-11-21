# nox is installed outside of poetry. VS Code is using Poetry Python interpreter,
# which does not know nox. Hence, use the terminal to run nox.
# TODO: apply some of this: https://github.com/cjolowicz/hypermodern-python/blob/master/noxfile.py#L14
# especially look at roughly line 51, flake/lint
import nox

nox.options.sessions = ["black", "ruff"]


@nox.session
def black(session):
    session.install("black")
    session.run("black", "./src/crewcal")


@nox.session
def ruff(session):
    session.install("ruff")
    session.run("ruff", "check", "./src/crewcal", "./tests/", "pyproject.toml")


@nox.session
def toml_sort(session):
    session.install("toml-sort")
    session.run("toml-sort", "--in-place", "pyproject.toml")


@nox.session
def test(session):
    # Not certain this is a good approach. But it currently works.
    session.run("pytest", "--cov=./src/crewcal", "tests/")
