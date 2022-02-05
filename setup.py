from setuptools import setup, find_packages

setup(name='blockchain explorer',
    version='1.11',
    description='Python bitcoin blockchain tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Marco Della Rosa',
    license='MIT',
    author_email='marcodellarosa80@gmail.com',
    url='https://github.com/dellarosamarco/Blockchain-Explorer',
    packages=find_packages(exclude=("test",)),
    include_package_data=True,
    install_requires=["base58","ecdsa","mnemonic","bip32utils","requests"],
    python_requires='>=3',
    keywords=["python", "bitcoin", "blockchain", "crypto"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography',
    ],
)