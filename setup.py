from setuptools import find_packages, setup


install_requires = [
    "tw2.core >= 2.0",
    "tw2.jquery >= 2.0",
]

tests_require = [
    "nose",
    "sieve",
    "coverage",
    "WebTest",
]


setup(
    name="tw2.jqplugins.sizeeq",
    version="0",
    description="TW2 pseudo widget to equalize sizes of selected elements",
    author="Nils Philippsen",
    author_email="nils@tiptoe.de",
    #url=
    #download_url=
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="nose.collector",
    packages=find_packages(),
    namespace_packages=['tw2', 'tw2.jqplugins'],
    zip_safe=False,
    include_package_data=True,
    package_data={"tw2.jqplugins.sizeeq": ["static/*"]},
    entry_points="""
        [tw2.widgets]
        widgets = tw2.jqplugins.sizeeq
    """,
    keywords=["tw2.widgets"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Web Environment :: ToscaWidgets",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Widget Sets",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
