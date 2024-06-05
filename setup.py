import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0.0"

REPO_NAME = "text-summaries"
AUTHOR_USER_NAME = "haotran0103"
SRC_REPO = "textSummaries"
AUTHOR_EMAIL = "tranquocho0102@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="a text summary application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haotran0103/text-summaries",
    packages=setuptools.find_packages(where="src"),
    project_urls={
        "Bug tracker": "https://github.com/haotran0103/text-summaries/issues",
    },
    package_dir={"": "src"}
)
