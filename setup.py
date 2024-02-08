import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="video2chars",
    version="0.6.6",
    author="Ryan Yin",
    author_email="xiaoyin_c@qq.com",
    description="Convert video to character art animation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuansuye/video2chars",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "moviepy",
        "numpy>=1.17.3",
        "pillow<10.0.0,>=9.5.0",
        "click",
        "requests",
        "imageio_ffmpeg>=0.2.0",
    ],
    package_data={
        "video2chars": ["DroidSansMono.ttf"],
    },
    entry_points={  # Optional
        "console_scripts": [
            "video2chars=video2chars:convert",
        ],
    },
)
