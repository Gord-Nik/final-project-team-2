from setuptools import setup, find_namespace_packages

setup(
    name='final-project',
    version='1',
    description='Final project team 2',
    url='https://github.com/Gord-Nik/final-project-team-2',
    author='Nikita Hordiienko, Nataliya Traxler, Roman Koreshniak, Yevhenii Stakhovskyi ',
    author_email='ua.gord.nik@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['docutils', 'prompt_toolkit'],
    entry_points={'console_scripts': ['bot_assistant = src.cli_bot:main']}
)