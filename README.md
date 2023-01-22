# fsl_gotSportScrapper


Pip install the required modules into <b>fsl_gotSportScrapper_data</b>
This folder will end up getting a copy of lambda_function when its deployed to AWS.

https://aws.amazon.com/premiumsupport/knowledge-center/lambda-python-package-compatible/

pip install \
    --platform manylinux2014_x86_64 \
    --target=fsl_gotSportScrapper_data \
    --implementation cp \
    --python 3.9 \
    --only-binary=:all: --upgrade \
    requests

pip install \
    --platform manylinux2014_x86_64 \
    --target=fsl_gotSportScrapper_data \
    --implementation cp \
    --python 3.9 \
    --only-binary=:all: --upgrade \
    beautifulsoup4


https://dev.to/aissalaribi/how-to-use-beautiful-soup-in-aws-lambda-for-web-scrapping-1gh8