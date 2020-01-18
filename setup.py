from setuptools import setup

setup(
    name="jp.co.coworker.nlp_knock_handson",
    version="0.0.1",
    install_requires=[
        'jupyter',
        'pytest',
        'scikit-learn',
    ],
    # extras_require={
    #     'test': [
    #         'pytest',
    #     ],
    # },
    entry_points={
        'console_scripts': [
            "polarity-analyser = jp.co.coworker.nlp_knock_handson.ch8.main:main",
        ],
    }
)
