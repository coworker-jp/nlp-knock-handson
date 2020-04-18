from setuptools import setup

setup(
    name="jp.co.coworker.nlp_knock_handson",
    version="0.0.1",
    install_requires=[
        'jupyter==1.0.0',
        'nltk==3.5',
        'pytest==5.3.3',
        'scikit-learn==0.22.1',
        'matplotlib==3.2.1',
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
