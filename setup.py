from setuptools import setup, find_packages

setup(name='blockchain explorer',
    version='1.0',
    description='Python bitcoin blockchain tools',
    long_description=open('README.md').read(),
    author='Marco Della Rosa',
    licene='MIT',
    #author_email='',
    url='https://github.com/dellarosamarco/Blockchain-Explorer',
    install_requires=["hashlib","base58","ecdsa","mnemonic","bip32utils","requests"],
    keywords=["python", "bitcoin", "blockchain", "crypto"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
)