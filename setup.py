import setuptools
import emoji_list_discord

version = emoji_list_discord.__version__
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emoji_list_discord",
    version=version,
    author="8ka1alu",
    author_email="8ka1alu@gmail.com",
    description="List of emojis that can be used on Discord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Project-Rain/emoji_list_discord",
    packages=['emoji_list_discord'],
    keywords='emoji list discord',
)
